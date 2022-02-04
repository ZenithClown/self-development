# -*- encoding: utf-8 -*-

"""List of Linear Models developed using PyTorch"""

import os
import torch
import torch.nn as nn
import torch.nn.functional as F

class LinearQNet(nn.Module):
    """
    LinearQNet - A Linear Q-Learning Neural Network
    
    A simplified linear neural network is sufficient to train most
    types of agents, infact more the simple the model is the better!
    This neural network will serve as the backbone of the `agent`
    that will learn to play the snake game.
    """
    
    def __init__(self, input_size : int, hidden_size : int, output_size : int) -> None:
        super().__init__()
        
        # layer definations
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)
        
    
    def forward(self, x) -> torch.Tensor:
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        
        return x
    
    
    def save(self, directory : str, filename : str = "model.pth"):
        # output path is `join(directory, filename)`
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        fullpath = os.path.join(directory, filename)
        torch.save(self.state_dict(), fullpath)
