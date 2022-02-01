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
@version: 1.0.0
"""

import json
from turtle import width
import pygame
from enum import Enum
from random import randint
from collections import namedtuple
from os.path import abspath, dirname, join

class DIRECTION(Enum):
    """define direction of movements"""

    RIGHT = 1
    LEFT  = 2
    UP    = 3
    DOWN  = 4

class SnakeGame(object):
    """Snake Game AI and Mechanics"""

    pygame.init() # initialize gaming module
    font  = pygame.font.Font("Oswald-ExtraLight.ttf", 17)
    point = namedtuple("point", "x, y")

    def __init__(self, width : int = 640, height : int = 480) -> None:
        self.width = width
        self.height = height

        # load configurations
        self._load_config_()

        # initialize display
        self.display = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake Game")

        # initialize game state
        # TODO randomize start point, direction
        self.direction = DIRECTION.RIGHT
        self.snakeHead = self.point(self.width / 2, self.height / 2)

        self.snake = [
            self.snakeHead,
            self.point(self.snakeHead.x - self.BLOCK_SIZE, self.snakeHead.y),
            self.point(self.snakeHead.x - (2 * self.BLOCK_SIZE), self.snakeHead.y)
        ]

        self.score = 0
        self._place_food_() # place food randomly, and initialize food

    
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

        with open(join(abspath(dirname(__file__)), "config.json"), "r") as f:
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


    def playGame(self):
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
            return True, self.score # True > game is over due to collision

        ### place food when eaten ###
        if self.snakeHead == self.food:
            self.score += 1 # update score on eaten
            self._place_food_()
        else:
            self.snake.pop()

        ### update ui and game-clock ###
        self._update_ui_()
        self.clock.tick(self.SPEED)

        return False, self.score # False > game is not over


    def _is_collision_(self) -> bool:
        """Check if the Snake Collides with the Boundary or Bites Self"""

        # boundary condition
        if (self.snakeHead.x > self.width - self.BLOCK_SIZE) or (self.snakeHead.x < 0) or \
           (self.snakeHead.y > self.height- self.BLOCK_SIZE) or (self.snakeHead.y < 0):
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
        return None


if __name__ == "__main__":
    game = SnakeGame()

    # start game, run unless game ends
    while True:
        gameOver, score = game.playGame()

        if gameOver:
            break

    print(f"Final Score: {score}")
