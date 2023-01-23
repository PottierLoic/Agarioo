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
    for blob in blobs:
        canvas.create_oval(blob.posx - blob.value/2, blob.posy - blob.value/2, blob.posx + blob.value/2 , blob.posy + blob.value/2, fill="white", tag="blob")
    for player in players:
        radius = player.value/2
        canvas.create_oval(player.posx - radius, player.posy - radius, player.posx + radius, player.posy + radius, fill="red", tag="player")
    
def mousePosition():
    mousex = window.winfo_pointerx() - window.winfo_rootx()
    mousey = window.winfo_pointery() - window.winfo_rooty()
    angle = math.atan2(mousey - players[0].posy, mousex - players[0].posx)
    players[0].direction = (math.cos(angle), math.sin(angle))

# TODO: fix collision detection (actually it check collision like if the player and blobs were squares) 
#       and collision box increase faster than the real size of the player
def collide():
    for player in players:
        for b in blobs:
            if math.sqrt((player.posx - b.posx)**2 + (player.posy - b.posy)**2) < player.value + b.value:
                if player.value > b.value:
                    player.value += b.value
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

    label = Label(window, text="Agar.io", font=("consolas", 10))
    label.pack()

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
    for i in range(1):
        players.append(player.Player("name"))

    update()
    graphics()


    window.mainloop()
