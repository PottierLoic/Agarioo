# agar.io 
# Author : Loïc Pottier
# Creation date : 23/01/2022

# IMPORTS
import math
from tkinter import *

# FILES IMPORTS
from game import Game
from constants import *

def graphics():
    canvas.delete("all")
    for p in g.players:
        # calculate the dimension/position of the g.players and draw them
        canvas.create_oval(p.x - p.radius, p.y - p.radius, p.x + p.radius, p.y + p.radius, fill=p.color, tag="player", outline=p.color)
        canvas.create_text(p.x, p.y, text=p.name, fill="black", tag="player")
    for b in g.blobs:
        # calculate the dimension/position of the g.blobs and draw them
        canvas.create_oval(b.x - b.radius, b.y - b.radius, b.x + b.radius, b.y + b.radius, fill=b.color, tag="blob", outline=b.color)
    if RECT_DISPLAY:
        g.qtree.draw(canvas)

def mousePosition():
    for i in range(len(g.players)):
        if g.players[i].name == "loic":
            mousex = window.winfo_pointerx() - window.winfo_rootx()
            mousey = window.winfo_pointery() - window.winfo_rooty()
            angle = math.atan2(mousey - g.players[i].y, mousex - g.players[i].x)
            g.players[i].direction = angle
            break
    

def update():
    mousePosition()
    g.update()
    graphics()
    window.after(DELAY, update)

if __name__ == "__main__":
    # WINDOW AND TKINTER SECTION
    window = Tk()
    window.title("Agar.io")
    window.resizable(False, False)

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    window.update()

    # VARIABLES
    g = Game()
    g.newPlayer("loic")

    mousex = 0
    mousey = 0

    update()

    window.mainloop()
