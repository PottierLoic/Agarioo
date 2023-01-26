# agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import math
from tkinter import *

# FILES IMPORTS
import blob
import player
from constants import *

def graphics():
    canvas.delete("blob", "player")
    for player in players:
        # calculate the dimension/position of the players and draw them
        radius = player.value/2
        px0 = player.posx - radius
        py0 = player.posy - radius
        px1 = player.posx + radius
        py1 = player.posy + radius
        canvas.create_oval(px0, py0, px1, py1, fill=player.color, tag="player", outline=player.color)
        canvas.create_text(player.posx, player.posy, text=player.name, fill="black", tag="player")
    for blob in blobs:
        # calculate the dimension/position of the blobs and draw them
        bx0 = blob.posx - blob.value/2
        by0 = blob.posy - blob.value/2
        bx1 = blob.posx + blob.value/2
        by1 = blob.posy + blob.value/2
        canvas.create_oval(bx0, by0, bx1, by1, fill=blob.color, tag="blob", outline=blob.color)
    
def mousePosition():
    mousex = window.winfo_pointerx() - window.winfo_rootx()
    mousey = window.winfo_pointery() - window.winfo_rooty()
    angle = math.atan2(mousey - players[0].posy, mousex - players[0].posx)
    players[0].direction = (math.cos(angle), math.sin(angle))

def collide():
    for player in players:
        for b in blobs:
            if player.value/2 + b.value/2 >= math.sqrt((b.posx - player.posx)**2 + (b.posy - player.posy)**2):
                player.eat(b.value)
                blobs.remove(b)

def update():
    global timeCount
    mousePosition()
    timeCount+=1
    if timeCount == max:
        blobs.append(blob.Blob())
        timeCount = 0
    for player in players:
        player.updatePosition()
    collide()
    graphics()
    window.after(PLAYER_SPEED, update)

if __name__ == "__main__":
    # WINDOW AND TKINTER SECTION
    window = Tk()
    window.title("Agar.io")
    window.resizable(False, False)

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    window.update()

    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

    # VARIABLES
    mousex = 0
    mousey = 0
    timeCount = 0
    max = int(SPAWN_RATE / PLAYER_SPEED)

    # GAME SECTION
    players = []
    blobs = []
    for i in range(10):
        blobs.append(blob.Blob())
    for i in range(10):
        players.append(player.Player("Loic UWU"))

    update()
    graphics()


    window.mainloop()
