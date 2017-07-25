#! /usr/bin/env python3


# IMPORTS
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
# from tkinter import imagetk

# WINDOW FUNCTIONS
def mquit():
    mexit = messagebox.askyesno(title = "Quit", message="Wirklich beenden?")
    if mexit > 0:
        battlefield.destroy()

# MAIN FRAME
battlefield = Tk()
battlefield.geometry('+350+100')
battlefield.title("Schlachtfeld - Treasure Hunting")

# MENU
# menubar = Menu(battlefield)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "Close", command = mquit)
# menubar.add_cascade(label = "File", menu=filemenu)
# battlefield.config(menu = menubar)

# MENU LABELS
"""
menulabel1 = Label(battlefield, text = "~HAUPTMENÜ~").place(x= 250, y=50)
newgamebutton = Button(battlefield, text = "Neues Spiel").place(x = 140, y=100)
loadgamebutton = Button(battlefield, text = "Spiel Laden").place(x = 290, y=170)
exitbutton = Button(battlefield, text = "Spiel Beenden",command = mquit).place(x = 240, y=280)
"""

# BUILD BATTLEFIELD FUNCTION
# mission has to be a list of lists: first columns, then rows. each variable in the list(s) is a placeholder for one field.
# mission_foes is a dictionary: it gives various integers the str(names) of the enemy, which stands there.
'''
def place_foe(mission_foes, mission, x, y):
    #try:
        if mission[y][x] == 1:
            logo = PhotoImage(file="Images/1one.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 2:
            logo = PhotoImage(file="Images/2two.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 3:
            logo = PhotoImage(file="Images/3three.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 4:
            logo = PhotoImage(file="Images/4four.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 5:
            logo = PhotoImage(file="Images/5five.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 6:
            logo = PhotoImage(file="Images/6six.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 7:
            logo = PhotoImage(file="Images/7seven.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 8:
            logo = PhotoImage(file="Images/8eight.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
        elif mission_foes[mission[y][x]] == 9:
            logo = PhotoImage(file="Images/9nine.gif")
            w1 = Label(battlefield, image = logo)
            w1.logo = logo
            w1.grid(row = x, column = y)
    #except KeyError:
    #    pass
'''
def build_battlefield(mission, mission_foes):
    for y in range(len(mission)):
        for x in range(len(mission[y])): # place the new field at .grid(row = x, column = y)
            if mission[y][x] == 0:
                logo = PhotoImage(file="Images/player.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y) # place a starting Point - image of the player
                playerx = x
                playery = y
            elif mission[y][x] == 1:
                logo = PhotoImage(file="Images/1one.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 2:
                logo = PhotoImage(file="Images/2two.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 3:
                logo = PhotoImage(file="Images/3three.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 4:
                logo = PhotoImage(file="Images/4four.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 5:
                logo = PhotoImage(file="Images/5five.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 6:
                logo = PhotoImage(file="Images/6six.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 7:
                logo = PhotoImage(file="Images/7seven.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 8:
                logo = PhotoImage(file="Images/8eight.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 9:
                logo = PhotoImage(file="Images/9nine.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == 'W':
                logo = PhotoImage(file="Images/wall.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == "E":
                logo = PhotoImage(file="Images/angel.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == "V":
                logo = PhotoImage(file="Images/vampire.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == "R":
                logo = PhotoImage(file="Images/werewolf.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)
            elif mission[y][x] == "L":
                logo = PhotoImage(file="Images/loot.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y) # place a loot image: generate random loot.
            elif mission[y][x] == "B":
                logo = PhotoImage(file="Images/barricada.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)# place a barricade
            elif mission[y][x] == "T":
                logo = PhotoImage(file="Images/treasure.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y) # place the Treasure
            elif mission[y][x] == "O":
                logo = PhotoImage(file="Images/0leer.gif")
                w1 = Label(battlefield, image = logo)
                w1.logo = logo
                w1.grid(row = x, column = y)# place an empty field
            else:
                try:
                    if str(mission_foes[str(mission[y][x])]) == "D" or mission[y][x] == IntVar:
                        logo = PhotoImage(file="Images/door.gif")
                        w1 = Label(battlefield, image = logo)
                        w1.logo = logo
                        w1.grid(row = x, column = y)
                    elif mission[y][x] == IntVar:
                        place_foe(mission_foes, mission, x, y)
                except KeyError:
                    pass
    return playerx, playery # return the player coordinates


# TEST PARAGRAPH
# mission list:
chapter_one = [["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "T", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O",  1 , "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "E", "O", "L", "O", "O", "W"],
               ["W", "O",  1 , "O", "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "B", "B", "B", "W", "W", "W",  "main" ,  "main" , "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",  "police" , "W", "W", "W"],
               ["W", "O", "O", "O", "E", "O", "O", "O", "O",  1 , "O",  1 , "O", "O", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",  1 , "O", "O", "O",  1 , "O", "O", "O", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "B", "B", "B", "B", "B", "B", "B", "O", "O", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "W"],
               ["W", "O", "O", "O", "O", "O",  1 , "O", "O", "O",  1 , "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "W",  0 , "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]]
# missions_foes dictionary:
chapter_one_foes = {
1:"police",
"main":"D",
"police":"D",
"E":"angel1",
"W":0,
"V":"vampire1",
"O":0,
"B":0,
"T":0,
"L":0,
"R":"werewolf1"
}
playerx, playery = build_battlefield(chapter_one, chapter_one_foes)

# has to be at the end
battlefield.mainloop()