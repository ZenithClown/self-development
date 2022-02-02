# -*- encoding: utf-8 -*-

"""Agent for the Snake Game"""

import sys
import json
import torch
import random
import numpy as np
from typing import Iterable
from collections import deque
from os.path import abspath, dirname, join

# append engine directory
sys.path.append(join(dirname(abspath(__file__)), ".."))
from engine import SnakeGame, DIRECTION

class SnakeAgent(object):
    """An Agent to Train an AI to Learn to Play Snake Game"""

    def __init__(self, model, trainer, **kwargs) -> None:
        self.n_games = 0
        self.epsilon = kwargs.get("epsilon", 0) # randomness
        self.gamma = kwargs.get("epsilon", 0.9) # discount rate
        self.memory = deque(maxlen = kwargs.get("MAX_MEMORY", int(1e6))) # popleft()

        self.BLOCK_SIZE = kwargs.get("BLOCK_SIZE") # `attr` must be loaded from config
        self.BATCH_SIZE = kwargs.get("BLOCK_SIZE", int(1e3)) # torch/nn models' batch size

        ### define `model` and `trainer` attributes ###
        # defined from model params such that loading/changing is easy
        self.model = model
        self.trainer = trainer


    ### define lambdas/short-functions ###
    _store_history_ : lambda self, states, action, reward, next_state, _is_game_over_ : \
        self.memory.append(states, action, reward, next_state, _is_game_over_)

    train_short_memory : lambda self, states, action, reward, next_state, _is_game_over_ : \
        self.trainer.train_setp(states, action, reward, next_state, _is_game_over_) # w/o batch


    ### definations of other functions ###
    def _read_environment_(self, game) -> np.ndarray:
        """
        An efficient agent understand its environment based on certain informations. This
        function is defined such that the `agent` i.e. the snake learns about its
        environment - which in this case are the following:
          * `danger` : from the direction of the current movement, is there a danger
          immediately infron, left/right of the snake.
          * `current direction` of movement
          * `food location` from the current snake head position

        For efficiency purpose, the snake is not allowed to move in reverse, as that
        is always an instant death. The movement is defined as:
          * `straight` - continue to move in the same direction
          * `left` - from the current head position move left, counter-clockwise
          the movement is: r -> u -> l -> d
          * `right` - from the current head position move right, clockwise the
          movement is: r -> d -> l -> u

        where, `l` = left, `r` = right, `u` = up and `d` = down. Thus, from the
        defination, `environment` is a array of the above mentioned elements.
        """

        head = game.snakeHead
        point = game.point # namedtuple

        point_l = point(head.x - self.BLOCK_SIZE, head.y)
        point_r = point(head.x + self.BLOCK_SIZE, head.y)
        point_u = point(head.x, head.y - self.BLOCK_SIZE)
        point_d = point(head.x, head.y + self.BLOCK_SIZE)

        dir_l = game.direction == DIRECTION.LEFT
        dir_r = game.direction == DIRECTION.RIGHT
        dir_u = game.direction == DIRECTION.UP
        dir_d = game.direction == DIRECTION.DOWN

        states = [
            # danger straight
            (dir_r and game._is_collision_(point_r)) or 
            (dir_l and game._is_collision_(point_l)) or 
            (dir_u and game._is_collision_(point_u)) or 
            (dir_d and game._is_collision_(point_d)),

            # danger right
            (dir_u and game._is_collision_(point_r)) or 
            (dir_d and game._is_collision_(point_l)) or 
            (dir_l and game._is_collision_(point_u)) or 
            (dir_r and game._is_collision_(point_d)),

            # danger left
            (dir_d and game._is_collision_(point_r)) or 
            (dir_u and game._is_collision_(point_l)) or 
            (dir_r and game._is_collision_(point_u)) or 
            (dir_l and game._is_collision_(point_d)),

            # current movement direction
            dir_l, dir_r, dir_u, dir_d,

            # food location
            game.food.x < game.snakeHead.x,  # food left
            game.food.x > game.snakeHead.x,  # food right
            game.food.y < game.snakeHead.y,  # food up
            game.food.y > game.snakeHead.y  # food down
        ]

        return np.array(states, dtype = np.int8)


    def train_long_memory(self) -> None:
        """TODO Documentations"""

        if len(self.memory) > self.BATCH_SIZE:
            mini_sample = random.sample(self.memory, self.BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, action, reward, next_state, _is_game_over_ = zip(*mini_sample)
        self.trainer.train_setp(states, action, reward, next_state, _is_game_over_)


    def get_action(self, states : np.ndarray) -> Iterable:
        """Get Action based on States"""

        self.epsilon = 80 - self.n_games # tradeoff explore/exploit
        final_move = [0, 0, 0]

        if random.randint(0, 200) < self.epsilon:
            final_move[random.randint(0, 2)] = 1
        else:
            state0 = torch.tensor(states, dtype = torch.float)
            prediction = self.model(state0)

            final_move[torch.argmax(prediction).item()]

        return final_move


if __name__ == "__main__":
    with open(join(abspath(dirname(__file__)), "..", "config", "snake.json"), "r") as f:
        # * read and create attributes from snake configurations
        config = json.load(f) # read config file

    BLOCK_SIZE = config["BLOCK_SIZE"]

    ### define params to keep track of model performance ###
    scores = []
    mean_scores = []
    
    cur_score = 0
    best_score = 0

    ### define models, agents, etc. and start training ###
    game = SnakeGame(enableAI = True)
    agent = SnakeAgent(None, None, BLOCK_SIZE = BLOCK_SIZE)

    # start game, run unless game ends
    while True:
        _, gameOver, score = game.playGame()
        print(agent._read_environment_(game))

        if gameOver:
            break

    print(f"Final Score: {score}")
