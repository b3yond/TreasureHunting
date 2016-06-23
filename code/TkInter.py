#! /usr/bin/env python3

__author__ = 'medusa'
# IMPORTS
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
ment = ""


# FUNCTIONS
def mColour():
    mycolor = colorchooser.askcolor()
    clabel = Label(mGui, text = mycolor).pack()
    alabel = Label(mGui, text = "wow, ein Label!", fg = mycolor).pack()
def button():
    pass #alabel = Label(mGui, text = "wow, ein Label!", fg = myColour()).pack()
def mbox():
    messagebox.showerror(title="BOX", message= "this is a BOX box.")
def mquit():
    mExit = messagebox.askokcancel(title = "Quit", message="Are You sure?")
    if mExit > 0:
        mGui.destroy()
def mOpen():
    myopen = filedialog.askopenfile()
    dlabel = Label(mGui, text = myopen).pack()
mycolor = "red"




# create Window
mGui = Tk()
mGui.geometry('450x450+400+100')
mGui.title("Schlachtfeld - Treasure Hunting")



# MENU
menubar = Menu(mGui)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Box", command = mbox)
filemenu.add_command(label = "Color", command = mColour)
filemenu.add_command(label = "Open", command = mOpen)
filemenu.add_command(label = "Close", command = mquit)

menubar.add_cascade(label = "File", menu=filemenu)

mGui.config(menu = menubar)




# FRAMES
alabel = Label(mGui, text = "wow, ein Label!", fg = mycolor).pack()
abutton = Button(mGui, text = "ok", command = button, fg = "red", bg = "black").pack()
aEntry = Entry(mGui, textvariable = ment).pack()


'''
Label Placement
pack: tut alles in die Mitte
place: tut alles dahin, wo die x/y-koordinaten stehen
grid: ordnet alles in rows und columns an
'''


mGui.mainloop()