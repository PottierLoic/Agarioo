# game class for agar.io 
# will be used when network will be implemented
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import time
import math

# FILES IMPORTS
from blob import Blob
from player import Player
from constants import *
from quadtree.qtree import QuadTree
from quadtree.rect import Rect

class Game():
    def __init__(self) -> None:
        self.blobs = []
        self.players = []
        for _ in range(10):
            self.blobs.append(Blob())
        for i in range(10):
            self.players.append(Player("Player "+str(i)))
        self.prevTime = 0
        self.lastTime = 0
        self.respawnDelay = 20
        self.qtree = QuadTree(Rect(1+WIDTH/2, 1+HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)

    def collide(self):
        self.qtree = QuadTree(Rect(1+WIDTH/2, 1+HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for player in self.players:
            self.qtree.insert(player)
        for blob in self.blobs:
            self.qtree.insert(blob)
        nearby = []
        for player in self.players:
            self.qtree.query(Rect(player.x, player.y, player.radius+50, player.radius+50), nearby)
            for obj in nearby:
                if obj != self :
                    if obj.type == "blob":
                        if player.radius + obj.radius >= math.sqrt((obj.x - player.x)**2 + (obj.y - player.y)**2):
                            player.eat(obj.mass)
                            try:
                                self.blobs.remove(obj)
                            except:
                                pass
                    else:
                        if (player.radius + obj.radius)*0.5 >= math.sqrt((obj.x - player.x)**2 + (obj.y - player.y)**2) and player.mass > obj.mass:
                            player.eat(obj.mass)
                            try:
                                self.players.remove(obj)
                            except:
                                pass
        
    def update(self):
        if self.prevTime < PHYSICS_REFRESH_RATE:
            self.prevTime += time.time() - self.lastTime
        else:
            if self.respawnDelay == SPAWN_RATE:
                self.blobs.append(Blob())
                self.respawnDelay = 0
            for player in self.players:
                player.updatePosition()
            self.collide()
            self.respawnDelay += 1
            self.prevTime = 0
            self.players.sort(key=lambda p:p.mass, reverse=False)
        lastTime = time.time


