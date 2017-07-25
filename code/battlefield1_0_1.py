#! /usr/bin/env python3


# IMPORTS
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
# from tkinter import imagetk

# WINDOW FUNCTIONS
def mquit():
    mExit = messagebox.askyesno(title = "Quit", message="Wirklich beenden?")
    if mExit > 0:
        battlefield.destroy()

# MAIN FRAME
battlefield = Tk()
battlefield.geometry('600x400+350+100')
battlefield.title("Schlachtfeld - Treasure Hunting")

# MENU
# menubar = Menu(battlefield)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "Close", command = mquit)
# menubar.add_cascade(label = "File", menu=filemenu)
# battlefield.config(menu = menubar)

# MENU LABELS
menulabel1 = Label(battlefield, text = "~HAUPTMENÜ~").place(x= 250, y=50)
newgamebutton = Button(battlefield, text = "Neues Spiel").place(x = 140, y=100)
loadgamebutton = Button(battlefield, text = "Spiel Laden").place(x = 290, y=170)
exitbutton = Button(battlefield, text = "Spiel Beenden",command = mquit).place(x = 240, y=280)


# BUILD BATTLEFIELD FUNCTION
# mission has to be a list of lists: first columns, then rows. each variable in the list(s) is a placeholder for one field.
# mission_foes is a dictionary: it gives various integers the str(names) of the enemy, which stands there.
def build_battlefield(mission, mission_foes):
    for y in mission:
        for x in y: # place the new field at .grid(row = x, column = y)
            if x == 0:
                pass # place a starting Point - image of the player
                playerx = x
                playery = y
            elif x == 'W':
                pass # place a solid wall
            elif x == IntVar:
                for key in mission_foes: # iterate through the keys of the dictionary, and return the name of the enemy
                    # place the image of the enemy
                    if mission_foes[key] == "D":
                        pass # place a door image; the value points where it goes.
            elif x == "B":
                pass # place a barricade
            else:
                pass # place an empty field
    return playerx, playery # return the player coordinates





# has to be at the end
battlefield.mainloop()