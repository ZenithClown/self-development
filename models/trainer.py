# -*- encoding: utf-8 -*-

"""List of Model Trainers"""

import torch
import torch.nn as nn
import torch.optim as optim

class QTrainer(object):
    """Defination of a QTrainer, a Trainer for Q-Learning"""
    
    def __init__(self, model, lr, gamma) -> None:
        """
        Create an instance of QTrainer with `trainer = QTrainer(model, lr, gamma)`
        that understands the `environment` and sets attributes to the `agent`s' which
        performs certain tasks.
        
        :param model: A neural network model (using `pytorch`) that will be used for
                      training and validation.
                      
        :param lr: Learning rate of the model.
        
        :param gamma: Discount parameter of the QNet.
        """
        
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(model.parameters(), lr = self.lr)
        
        
    def train_step(self, states, action, reward, next_state, gameOver) -> float:
        states = torch.tensor(states, dtype = torch.float)
        action = torch.tensor(action, dtype = torch.float)
        reward = torch.tensor(reward, dtype = torch.float)
        next_state = torch.tensor(next_state, dtype = torch.float)
        
        if len(states.shape) == 1:
            # (1, x); else (n, x)
            # learn with a particular random information
            states = torch.unsqueeze(states, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            next_state = torch.unsqueeze(next_state, 0)
            
            gameOver = (gameOver, )
            
        ### predict Q-Value with current state ###
        prediction = self.model(states) # perform forward operation
        
        target = prediction.clone().detach()
        for idx in range(len(gameOver)):
            QNew = reward[idx]
            
            # print(target)
            if not gameOver[idx]:
                QNew = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))
            
            # print(target)
            target[idx][torch.argmax(action[idx]).item()] = QNew
            # print(target)
            
        ### update nn based on Q-Value ###
        self.optimizer.zero_grad()
        losses = self.criterion(target, prediction)
        # print(losses)
        losses.backward() # gradient descent
        self.optimizer.step()
        
        return round(float(losses), 3)
