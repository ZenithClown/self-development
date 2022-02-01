# -*- encoding: utf-8 -*-

"""
DeepQ Learning is a Reinforcement Learning Platform where AI Learns to Play Games

In this project, I'm trying to develop some 'Q-Learning Algorithms' where the
neural network will learn to play various games. The `engine` is specifically
designed to build games that can be used to train and test the models. The game
engines are also built such that an user can self play without any overhead.

List of Games Available:
  1. Classic Snake Game (`snake.py`)

@author:  Debmalya Pramanik
@Contact: dPramanik.official@gmail.com
"""

# init-time options registrations
from .snake import SnakeGame
