# -*- encoding: utf-8 -*-

"""Function for Plotting"""

import seaborn as sns
from IPython import display
from typing import Iterable
import matplotlib.pyplot as plt

plt.ion() # interactive
sns.set_style('whitegrid');
plt.style.use('default-style');

def plot(x_args : Iterable[Iterable], title : str = "Model Training", **kwargs):
    """Plot Figure in Interactive Mode"""

    display.clear_output(wait = True)
    display.display(plt.gcf()) # get cur. fig.

    plt.clf() # clear cur. fig.

    plt.title(title)
    plt.xlabel(kwargs.get("xlabel", "epochs"))
    plt.ylabel(kwargs.get("ylabel", "scores"))

    for idx, xs in enumerate(x_args):
        # * while plotting lines, send line label for identification
        # ! else line label is dynamically allocated as number (idx)
        cur_label = kwargs.get("labels", list(range(1, len(xs) + 1)))[idx]
        plt.plot(xs, label = cur_label) # plot n-lines w/o changing function

    # auto set xlimits and ylimits
    # else, have provision for dynamic allocation
    plt.xlim(kwargs.get("xlim", [0, max(map(len, x_args))]))
    plt.ylim(kwargs.get("ylim", [0, max(map(max, x_args))]))

    plt.show(block = False)
    plt.pause(0.1)
