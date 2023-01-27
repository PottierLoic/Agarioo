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
        self.name = name
        self.posx = random.randint(0, WIDTH)
        self.posy = random.randint(0, HEIGHT)
        self.value = 50
        self.score = 50
        self.direction = (0, 0)
        self.color = random.choice(PLAYER_COLORS)

    def eat(self, value):
        self.score+=value
        self.value+=math.log(value)

    def updatePosition(self):
        self.posx += self.direction[0]
        self.posy += self.direction[1]
        if self.posx < 0:
            self.posx = 0
        if self.posx > WIDTH:
            self.posx = WIDTH
        if self.posy < 0:
            self.posy = 0
        if self.posy > HEIGHT:
            self.posy = HEIGHT
        
    def __str__(self) -> str:
        return f"Player({self.posx}, {self.posy})"

