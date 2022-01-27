# -*- encoding: utf-8 -*-

import json
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
        self.display.fill(self.BACKGROUND)

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
        self._create_ui_()

    
    def _place_food_(self) -> None:
        """Randomly Place a Food in the Board"""

        x = randint(0, (self.width - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE
        y = randint(0, (self.width - self.BLOCK_SIZE) // self.BLOCK_SIZE) * self.BLOCK_SIZE

        self.food = self.point(x, y)
        if self.food in self.snake:
            self._place_food_()

        return None


    def _create_ui_(self) -> None:
        """Create Front-End, i.e. Draw Snake, Food and Scoreboard"""

        for pt in self.snake:
            pygame.draw.rect(self.display, self.SNAKECOLOR1, pygame.Rect(pt.x, pt.y, self.BLOCK_SIZE, self.BLOCK_SIZE))
            pygame.draw.rect(self.display, self.SNAKECOLOR2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, self.FOODCOLOR, pygame.Rect(self.food.x, self.food.y, self.BLOCK_SIZE, self.BLOCK_SIZE))

        # score board
        text = self.font.render(f"Score: {self.score}", True, self.FOREGROUND)
        self.display.blit(text, [0, 0])
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


if __name__ == "__main__":
    pass
