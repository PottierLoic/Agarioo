# game class for agar.io 
# will be used when network will be implemented
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS

# FILES IMPORTS
import blob
import player
from constants import *

class Game():
    def __init__(self) -> None:
        blobs = []
        players = []
        for blob in range(10):
            blobs.append(blob.Blob())
        for player in range(1):
            players.append(player.Player("name"))
    
    def update(self):
        pass

