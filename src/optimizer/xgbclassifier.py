# -*- encoding: utf-8 -*-

"""Perform Parameter Optimization for XGBClassifiers"""

import numpy as np

from typing import Iterable
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

def objective(trial : object, data : Iterable, target : Iterable, **kwargs) -> float:
    """
    A well defined an parameterized (generalized) objective function that can be used
    for hyperparameter tuning of `xgboost.XGBClassifier` model. For more information
    on `xgboost` check documentation: https://xgboost.readthedocs.io/.

    The function currently defines a set of most commonly required parameters, that is
    used to find optimal value. To use the model, just:

    ```python
       # create a lambda function, to pass additional arguments to `objective`
       func = lambda trial : objective(trial, x_train, y_train)

       OPTUNA_STUDY_NAME = "XGBClassifier-ESR150"
       study = optuna.create_study(
           direction = "maximize", # to minimize or maximize
           study_name = OPTUNA_STUDY_NAME, # to understand later
           storage = f"sqlite:///{OPTUNA_STUDY_NAME}.db" # save to disk
       )

       study.optimize(func, n_trials = 3) # use `func` as the argument
    ```

    :type  trial: object
    :param trial: The `trial` object stores each and every information related to
                  each specific trials. This object can later be accessed to find
                  or understand how the model is performing.

    :type  data, target: object
    :param data, target: Typically a `pd.DataFrame` or a `np.ndarray` which has
                         n-features (i.e. dimensions) with one target output.
    """

    param = {
        "tree_method" : "gpu_hist", # suggests using gpu, as available
        
        "alpha" : trial.suggest_loguniform("alpha", 1e-4, 1e-3), # L1 regularization
        "lambda" : trial.suggest_loguniform("lambda", 0.7, 10.0), # L2 regularization
        
        "subsample" : trial.suggest_categorical("subsample", np.arange(0.3, 1.01, 0.1)),
        "learning_rate" : trial.suggest_categorical("learning_rate", np.arange(8e-3, 2.1e-2, 1e-3)),
        "colsample_bytree" : trial.suggest_categorical("colsample_bytree", np.arange(0.3, 1.01, 0.1)), # tree sub-sample ratio
        
        "max_depth" : trial.suggest_int("max_depth", 2, 20),
        "n_estimators" : trial.suggest_int("n_estimators", 50, 10000),
        "min_child_weight" : trial.suggest_int("min_child_weight", 1, 300)
    }
    
    x_train_, x_test_, y_train_ , y_test_ = train_test_split(data, target, test_size = 0.3, random_state = 7) # should be no name conflict
    model = XGBClassifier(**param) # `param` list of all parameters that needs tuning
    
    # fit model, with early stopping
    model.fit(x_train_, y_train_, eval_set = [(x_test_, y_test_)], early_stopping_rounds = 150, verbose = False)
    
    # check predictions, and return `auc` score
    predictions = model.predict_proba(x_test_)[:, 1]
    return roc_auc_score(y_test_, predictions)

if __name__ == "__main__":
    # perform optimization on a given data set
    import sys # to get command line arguments from users
    import optuna # robust hyperparameter tuning and optimization

    from time import ctime

    # disable all warnings that might be displayed by `optuna`
    from warnings import simplefilter
    simplefilter("ignore", category = UserWarning)

    print(f"{ctime()} Starting XGBClassifier Optimization")

    # the following arguments are required from the users
    # `datapath` : training dataset, with target values in order
    # `model_save_dir` : path to save the study file in a SQLite3 database
    _, datapath, model_save_dir = sys.argv

    # currently only `np` objects is defined to load
    # https://numpy.org/doc/stable/reference/generated/numpy.save.html
    # TODO `pd.DataFrame` or using more robust `pickle` objects
    with open(datapath, "rb") as f:
        x_train = np.load(f)
        y_train = np.load(f)

    print(f"{ctime()} All files are now loaded into memory.")

    # perform model parameter tuning
    func = lambda trial : objective(trial, x_train, y_train)
    OPTUNA_STUDY_NAME = "XGBClassifier-ESR150" # TODO parameterize study name

    study = optuna.create_study(
        direction = "maximize", # to minimize or maximize
        study_name = OPTUNA_STUDY_NAME, # to understand later
        storage = f"sqlite:///{model_save_dir}/{OPTUNA_STUDY_NAME}.db" # save to disk
    )
    
    study.optimize(
        func,
        n_trials = 41,
        callbacks = [
            # define a list of `callbacks` for added performance
            # https://optuna.readthedocs.io/en/latest/tutorial/20_recipes/007_optuna_callback.html
            # currently adding a print callback, to display the best value and accuracy score
            # https://github.com/optuna/optuna/issues/2073
            lambda study, trial : print(f"Trial: {trial.number}, Best Value: Trial-#{study.best_trial.number} = {round(study.best_value, 5)}")
        ]
    )
