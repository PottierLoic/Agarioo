# game class for agar.io 
# will be used when network will be implemented
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import math

# FILES IMPORTS
from blob import Blob
from player import Player
from constants import *

class Game():
    def __init__(self) -> None:
        blobs = []
        players = []
        for blob in range(10):
            blobs.append(Blob())

    def addPlayer(self, name):
        self.players.append(Player(name))
    
    def collide(self):
        for player in self.players:
            for b in self.blobs:
                if player.value/2 + b.value/2 >= math.sqrt((b.posx - player.posx)**2 + (b.posy - player.posy)**2):
                    player.eat(b.value)
                    self.blobs.remove(b)

    def update(self):
        for player in self.players:
            player.updatePosition()
        self.collide()

