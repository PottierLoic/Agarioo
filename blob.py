# blob class for agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import random
import math

# FILES IMPORTS
from constants import *

class Blob:
    def __init__(self) -> None:
        self.type = "blob"
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.mass = random.uniform(BLOB_MIN_MASS, BLOB_MAX_MASS)
        self.radius = math.sqrt(self.mass*100)
        self.color = random.choice(BLOB_COLORS)