# player class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import random
import math

# FILE IMPORTS
from constants import *

class Player:
    def __init__(self, name) -> None:
        self.type = "player"
        self.name = name
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.mass = 10
        self.radius = math.sqrt(self.mass*100)
        self.direction = (0, 0)
        self.color = random.choice(PLAYER_COLORS)

    def eat(self, value):
        self.mass += value
        self.radius = math.sqrt(self.mass*100)

    def updatePosition(self):
        self.x += self.direction[0] * PLAYER_SPEED
        self.y += self.direction[1] * PLAYER_SPEED
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT
        
