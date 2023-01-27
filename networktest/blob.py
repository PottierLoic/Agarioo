# blob class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import random

# FILES IMPORTS
from constants import *

class Blob:
    def __init__(self) -> None:
        self.posx = random.randint(0, WIDTH)
        self.posy = random.randint(0, HEIGHT)
        self.value = random.randint(BLOB_MIN_SIZE, BLOB_MAX_SIZE)
        self.color = random.choice(BLOB_COLORS)

    def __str__(self) -> str:
        return f"Blob({self.posx}, {self.posy}, {self.value})"
