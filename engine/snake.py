# -*- encoding: utf-8 -*-

"""
Snake Game

A simple game of 'snake' built in python (using `pygame`).
The game can be played by an enduser by running the file directly as:

```python
python snake.py
```

@author:  Debmalya Pramanik
@Contact: dPramanik.official@gmail.com
@version: 1.0.1
"""

import json
import pygame
import numpy as np
from enum import Enum
from random import randint
from typing import Iterable
from collections import namedtuple
from os.path import abspath, dirname, join

pygame.init() # initialize gaming module

class DIRECTION(Enum):
    """define direction of movements"""

    RIGHT = 1
    LEFT  = 2
    UP    = 3
    DOWN  = 4

class SnakeGame(object):
    """Snake Game AI and Mechanics"""

    font  = pygame.font.Font(join(abspath(dirname(__file__)), "..", "static", "fonts", "Oswald-ExtraLight.ttf"), 17)
    point = namedtuple("point", "x, y")

    def __init__(self, width : int = 640, height : int = 480, enableAI : bool = False, **kwargs) -> None:
        self.width = width
        self.height = height

        # all types of DeepQ/NN functionality should be controlled via enableAI
        self.enableAI = enableAI

        # load configurations
        self._load_config_()

        # initialize display
        self.display = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake Game")

        # * initialize game with initial parameters
        self.initial_snake_length = kwargs.get("initial_snake_length", 3)
        self._init_game_()


    def _init_game_(self) -> None:
        # TODO randomize start point, direction
        self.direction = DIRECTION.RIGHT
        self.snakeHead = self.point(self.width / 2, self.height / 2)

        self.snake = [self.snakeHead]
        for idx in range(self.initial_snake_length - 1):
            self.snake.append(self.point(self.snakeHead.x - (idx + 1) * self.BLOCK_SIZE, self.snakeHead.y))

        self.score = 0
        self.food = None
        self._place_food_() # place food randomly, and initialize food

        # ! set a frame/loop counter
        # * this is useful to stop game when the system falls inside a infinit-loop
        self.num_frames = 0 # this is ignored when `self.enableAI = False`

        return None

    
    def _place_food_(self) -> None:
        """Randomly Place a Food in the Board"""

        x = randint(0, (self.width - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE
        y = randint(0, (self.height - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE

        self.food = self.point(x, y)
        if self.food in self.snake:
            self._place_food_()

        return None


    def _update_ui_(self) -> None:
        """Create Front-End, i.e. Draw Snake, Food and Scoreboard"""

        self.display.fill(self.BACKGROUND) # ! redraw gameboard on each run

        for pt in self.snake:
            pygame.draw.rect(self.display, self.SNAKECOLOR1, pygame.Rect(pt.x, pt.y, self.BLOCK_SIZE, self.BLOCK_SIZE))
            pygame.draw.rect(self.display, self.SNAKECOLOR2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, self.FOODCOLOR, pygame.Rect(self.food.x, self.food.y, self.BLOCK_SIZE, self.BLOCK_SIZE))

        # adding a boundary wall of `int(self.BLOCK_SIZE / 2)` on all sides
        pygame.draw.line(self.display, self.BOUNDARY, (0, 0), (self.width, 0), width = int(self.BLOCK_SIZE / 2))
        pygame.draw.line(self.display, self.BOUNDARY, (self.width, 0), (self.width, self.height), width = int(self.BLOCK_SIZE / 2))
        pygame.draw.line(self.display, self.BOUNDARY, (self.width, self.height), (0, self.height), width = int(self.BLOCK_SIZE / 2))
        pygame.draw.line(self.display, self.BOUNDARY, (0, self.height), (0, 0), width = int(self.BLOCK_SIZE / 2))

        # score board
        text = self.font.render(f"Score: {self.score}", True, self.FOREGROUND)
        self.display.blit(text, [int(self.BLOCK_SIZE / 2) + 1, int(self.BLOCK_SIZE / 2) + 1]) # leave space for wall-boundary
        pygame.display.flip()

        return None
 

    def _load_config_(self) -> None:
        """Load Configurations and Load as Class Attributes"""

        with open(join(abspath(dirname(__file__)), "..", "config", "snake.json"), "r") as f:
            _config = json.load(f)

        self.SPEED = _config["SPEED"]
        self.BLOCK_SIZE = _config["BLOCK_SIZE"]
        
        for attr, value in _config["COLORS"].items():
            # set all color attributes with `setattr`
            # the color attributes are defined, for more information/control
            # check documentation.
            # TODO update code such that color/config on initialization
            setattr(self, attr, value)

        return None


    def playGame(self, actions : Iterable = None):
        """Return a Function Based on AI Parameter"""

        if not self.enableAI:
            return self._play_game_via_keys_()

        return self._play_game_via_auto_(actions) # return function when ai is enabled
        
        
    def _play_game_via_auto_(self, actions : Iterable[int]):
        """Play Snake Game via AI Control"""

        reward = 0
        self.num_frames += 1

        ### collect user input ###
        for event in pygame.event.get():
            # * no user input is required however, we may need
            # to close when `QUIT` button is pressed - i.e. exit out program
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ### define clockwise moving direction ###
        clockwise = [DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT, DIRECTION.UP]
        idx = clockwise.index(self.direction)
        
        ### find next direction ###
        if np.array_equal(actions, [1, 0, 0]):
            self.direction = clockwise[idx] # no change
        elif np.array_equal(actions, [0, 1, 0]):
            self.direction = clockwise[(idx + 1) % 4] # right turn
        else:
            self.direction = clockwise[(idx - 1) % 4] # left turn

        ### move snake as per actions/states ###
        self._move_snake_(self.direction) # update snake head
        self.snake.insert(0, self.snakeHead)

        ### check if game over ###
        if (self._is_collision_()) or (len(self.snake) * 100 <= self.num_frames): # TODO dynamic allocation
            reward -= 10 # penalize the nn-model
            return reward, True, self.score # True > game is over due to collision

        ### place food when eaten ###
        if self.snakeHead == self.food:
            reward = 10 # reward the nn-model
            self.score += 1 # update score on eaten
            self._place_food_()
        else:
            self.snake.pop()

        ### update ui and game-clock ###
        self._update_ui_()
        self.clock.tick(self.SPEED)

        return reward, False, self.score # False > game is not over
    
    def _play_game_via_keys_(self):
        """Play Snake Game with `arrowkeys` and Enjoy!"""

        ### collect user input ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                # check keystrokes
                # only `arrowkeys` are allowed/registered
                if event.key == pygame.K_LEFT:
                    self.direction = DIRECTION.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = DIRECTION.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = DIRECTION.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DIRECTION.DOWN
                else:
                    pass # do nothing

            else:
                # ! this should not happen
                pass

        ### move snake as per keystroke ###
        self._move_snake_(self.direction) # update snake head
        self.snake.insert(0, self.snakeHead)

        ### check if game over ###
        if self._is_collision_():
            pygame.quit()
            return None, True, self.score # True > game is over due to collision

        ### place food when eaten ###
        if self.snakeHead == self.food:
            self.score += 1 # update score on eaten
            self._place_food_()
        else:
            self.snake.pop()

        ### update ui and game-clock ###
        self._update_ui_()
        self.clock.tick(self.SPEED)

        return None, False, self.score # False > game is not over


    def _is_collision_(self, pt = None) -> bool:
        """Check if the Snake Collides with the Boundary or Bites Self"""

        if not pt:
            # ! define point if already not define
            # * if defined, check if collision occurs on the given point
            # * this is useful when the `agent` needs to understand the environment
            pt = self.snakeHead

        # boundary condition
        if (pt.x > self.width - self.BLOCK_SIZE) or (pt.x < 0) or \
           (pt.y > self.height- self.BLOCK_SIZE) or (pt.y < 0):
            return True

        # if snake eats self
        if self.snakeHead in self.snake[1:]:
            return True

        return False # no game over condition


    def _move_snake_(self, direction) -> None:
        x = self.snakeHead.x
        y = self.snakeHead.y

        if direction == DIRECTION.RIGHT:
            x += self.BLOCK_SIZE
        elif direction == DIRECTION.LEFT:
            x -= self.BLOCK_SIZE
        elif direction == DIRECTION.UP:
            y -= self.BLOCK_SIZE
        elif direction == DIRECTION.DOWN:
            y += self.BLOCK_SIZE
        else:
            raise ValueError("Internal Error, this direction should not be registered")

        self.snakeHead = self.point(x, y)


if __name__ == "__main__":
    game = SnakeGame()

    # start game, run unless game ends
    while True:
        _, gameOver, score = game.playGame()

        if gameOver:
            break

    print(f"Final Score: {score}")
