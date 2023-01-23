# blob class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import random

# FILES IMPORTS
import constants

class Blob:
    def __init__(self) -> None:
        self.posx = random.randint(0, constants.WIDTH)
        self.posy = random.randint(0, constants.HEIGHT)
        self.value = random.randint(1, 10)
    
    def __str__(self) -> str:
        return f"Blob({self.posx}, {self.posy}, {self.value})"
