# player class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import random
import math

# FILE IMPORTS
from constants import *

class Player:
    def __init__(self, name, isBot) -> None:
        self.type = "player"
        self.isBot = isBot
        self.name = name
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.mass = 10
        self.radius = math.sqrt(self.mass*100)
        if self.isBot:
            self.direction = random.random()*math.pi*2
        self.color = random.choice(PLAYER_COLORS)

    def eat(self, value):
        self.mass += value
        self.radius = math.sqrt(self.mass*100)

    def updatePosition(self):
        if self.isBot:
            self.direction += random.random()-0.5
        self.x += math.cos(self.direction) * PLAYER_SPEED
        self.y += math.sin(self.direction) * PLAYER_SPEED
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT
        
