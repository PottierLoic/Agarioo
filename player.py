# player class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import constants

# FILE IMPORTS
import constants

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.posx = 100
        self.posy = 100
        self.value = 25
        self.direction = (0, 0)

    def updatePosition(self):
        self.posx += self.direction[0]
        self.posy += self.direction[1]
        if self.posx < 0:
            self.posx = 0
        if self.posx > constants.WIDTH:
            self.posx = constants.WIDTH
        if self.posy < 0:
            self.posy = 0
        if self.posy > constants.HEIGHT:
            self.posy = constants.HEIGHT
        
    

    def __str__(self) -> str:
        return f"Player({self.posx}, {self.posy})"

