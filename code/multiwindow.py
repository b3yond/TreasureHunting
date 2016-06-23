#! /usr/bin/env python3

__author__ = 'medusa'
# IMPORTS
from tkinter import *
# from tkinter import messagebox
# from tkinter import imagetk
from random import randint
import time

# GUI
textwin = Tk()
textwin.geometry("310x180+70+100")
textwin.title("Ausgabe - Treasure Hunting")
battlefield = Tk()
battlefield.geometry('+380+100')
battlefield.title("Schlachtfeld - Treasure Hunting")

# # # # # #
# IMAGES  #
# # # # # #
logo = PhotoImage(file="Images/player.gif")
gifplayer = logo
logo = PhotoImage(file="Images/1one.gif")
gifone = logo
logo = PhotoImage(file="Images/2two.gif")
giftwo = logo
logo = PhotoImage(file="Images/3three.gif")
gifthree = logo
logo = PhotoImage(file="Images/4four.gif")
giffour = logo
logo = PhotoImage(file="Images/5five.gif")
giffive = logo
logo = PhotoImage(file="Images/6six.gif")
gifsix = logo
logo = PhotoImage(file="Images/7seven.gif")
gifseven = logo
logo = PhotoImage(file="Images/8eight.gif")
gifeight = logo
logo = PhotoImage(file="Images/9nine.gif")
gifnine = logo
logo = PhotoImage(file="Images/wall.gif")
gifwall = logo
logo = PhotoImage(file="Images/angel.gif")
gifangel = logo
logo = PhotoImage(file="Images/vampire.gif")
gifvampire = logo
logo = PhotoImage(file="Images/werewolf.gif")
gifwerewolf = logo
logo = PhotoImage(file="Images/loot.gif")
gifloot = logo
logo = PhotoImage(file="Images/barricada.gif")
gifbarricada = logo
logo = PhotoImage(file="Images/treasure.gif")
giftreasure = logo
logo = PhotoImage(file="Images/0leer.gif")
gifleer = logo
logo = PhotoImage(file="Images/door.gif")
gifdoor = logo

# # # # #
# ITEMS #
# # # # #
# Swords
nosword = ["Faust", 0, 0.0, 0.3, 0, False]
teli = ["Teleskopschlagstock", 20, 0.0, 0.3, 20, False]
knife = ["Messer", 30, 0.2, 0.0, 20, False]
shortsword = ["Kurzschwert", 50, 0.3, 0.0, 40, False]
longsword = ["Langschwert", 70, 0.4, 0.1, 70, False]
nunchaku = ["Nun-Chakus", 50, 0.1, 0.7, 70, False]
mace = ["Streitkolben", 70, 0.1, 0.5, 70, False]
claymore = ["Zweihänder", 120, 0.3, 0.2, 120, False]
katana = ["Katana", 75, 0.6, 0.1, 100, False]
silversword = ["Silberschwert", 50, 0.3, 0.2, 90, True]
silverdagger = ["Silberdolch", 30, 0.2, 0.0, 40, True]
whip = ["Silberpeitsche", 30, 0.7, 0.8, 60, True]
krallen = ["Krallen", 30, 0.3, 0.6, 9999, False]
silverkrallen = ["Silberkrallen", 30, 0.4, 0.7, 150, True]
# Guns
nogun = ["Keine", 0, 0, 0, 0]
glock = ["Glock", 2, 10, 4, 30]
uzi = ["Uzi", 4, 10, 3, 50]
ak74 = ["Ak-74", 2, 30, 5, 80]
p90 = ["P90", 3, 15, 4, 60]
abgesägte_shotgun = ["Abgesägte Schrotflinte", 1, 50, 2, 30]
shotgun = ["Schrotflinte", 1, 70, 3, 80]
awp = ["AWP", 1, 90, 8, 140]
m4 = ["m4", 3, 25, 6, 110]
lmg = ["LMG", 7, 10, 4, 130]


# # # # # #
# CLASSES #
# # # # # #
class Player(): # playable character class
    def __init__(self, name, race, kon, srg, ges, agi, bitcoins, level, experience, gun, sword, inventar, x, y):
        self.name = name
        self.race = race
        self.kon = kon
        self.srg = srg
        self.ges = ges
        self.agi = agi
        self.bitcoins = bitcoins
        self.hp = self.kon*8 + self.srg*5 + 10
        self.level = level
        self.experience = experience
        self.gun = gun
        self.sword = sword
        self.inventar = inventar
        self.x = x
        self.y = y
class Engel(Player): # race subclass - Engels can give any ally 30 hp
    def __init__(self, name):
        super().__init__(name, "Engel", 4, 3, 7, 7, 50, 1, 0, [nogun, 0, False], nosword, [], 0, 0)
    def heal(self):
        pass
class Vampir(Player): # race subclass - Vampirs can steal 20 hp from all near enemies and add them to their own hp
    def __init__(self, name):
        super().__init__(name, "Vampir", 5, 7, 6, 5, 50, 1, 0, [nogun, 0, False], nosword, [], 0, 0)
    def lifesteal(self):
        pass
class Werwolf(Player): # race subclass - Werwolfs can morph into wolves, which doubles their attributes but disables range combat.
    def __init__(self, name):
        super().__init__(name, "Werwolf", 4, 5, 5, 4, 50, 1, 0, [nogun, 0, False], krallen, [], 0, 0)
    def morph(self):
        pass
class Golem(Player): # race subclass - Golems can stun enemies for 1 round.
    def __init__(self, name):
        super().__init__(name, "Golem", 7, 8, 4, 4, 50, 1, 0, [nogun, 0, False], nosword, [], 0, 0)
    def stun(self):
        pass

# ENEMYS
class Enemy():
    def __init__(self, name, race, kon, srg, ges, agi, gun, sword, loot, experience):
        self.name = name
        self.race = race
        self.kon = kon
        self.srg = srg
        self.ges = ges
        self.agi = agi
        self.gun = gun
        self.sword = sword
        self.loot = loot
        self.experience = experience

    def ai_turn(self, foelist, id):
        if foelist[id][5] > 0:  # stun test and removal
            foelist[id][5] -= 1
        else:
            pass  # here comes the enemy turn

    def showinfo(self):
        pass  # open an infobox with info about the enemy on right-click


class Police(Enemy):
    def __init__(self):
        super().__init__("Polizist", "human", 4, 5, 5, 4, "glock", "teli", randint(5, 10), 5)
class Security(Enemy):
    def __init__(self):
        super().__init__("Private Security", "human", 5, 7, 5, 4, "random", "teli", randint(1, 10), 6)
class Mercenary(Enemy):
    def __init__(self):
        super().__init__("Söldner", "human", 6, 8, 8, 6, "ak74", "knife", randint(5, 20), 7)
class Soldier(Enemy):
    def __init__(self):
        super().__init__("Soldat", "human", 7, 8, 8, 7, "random", "knife", randint(10, 20), 8)
class Taskforce(Enemy):
    def __init__(self):
        super().__init__("Spezialeinheit", "human", 9, 10, 10, 9, "random", "random", randint(10, 5), 10)
class Criminal(Enemy):
    def __init__(self):
        super().__init__("Krimineller", "human", 5, 6, 7, 7, "random", "random", randint(1, 15), 6)
class Terrorist(Enemy):
    def __init__(self):
        super().__init__("Terrorist", "human", 5, 7, 9, 8, "random", "random", randint(1, 15), 7)
class Silver1(Enemy):
    def __init__(self):
        super().__init__("Verschwörungstheoretiker", "human", 4, 5, 5, 4, "random", "silversword", randint(1, 10), 7)
class Silver2(Enemy):
    def __init__(self):
        super().__init__("Atheist", "human", 8, 10, 8, 5, "random", "whip", randint(10, 20), 11)
class Angel1(Enemy):
    def __init__(self):
        super().__init__("Engel", "angel", 5, 3, 8, 7, "random", "random", randint(10, 15), 8)
class Angel2(Enemy):
    def __init__(self):
        super().__init__("Engel", "angel", 6, 4, 10, 8, "random", "random", randint(15, 25), 12)
class Vampire1(Enemy):
    def __init__(self):
        super().__init__("Vampir", "vampire", 7, 9, 5, 5, "random", "random", randint(10, 15), 8)
class Vampire2(Enemy):
    def __init__(self):
        super().__init__("Vampir", "vampire", 8, 11, 6, 6, "random", "random", randint(15, 25), 12)
class Werewolf1(Enemy):
    def __init__(self):
        super().__init__("Werwolf", "werewolf", 4, 5, 6, 5, "random", "krallen", randint(10, 15), 8)
class Werewolf2(Enemy):
    def __init__(self):
        super().__init__("Werwolf", "werewolf", 5, 8, 6, 6, "random", " silverkrallen", randint(15, 25), 12)

# # # # #
# MAPS  #
# # # # #
# mission list:
chapter_one = [["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "T", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "O", "O", "O", "W"],
               ["W", "O", "O",  1 , "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O",  4 , "O", "L", "O", "O", "W"],
               ["W", "O",  1 , "O", "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "B", "B", "B", "W", "W", "W",  2 ,  2 , "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W", "W", "W", "W"],
               ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",  3 , "W", "W", "W"],
               ["W", "O", "O", "O",  4 , "O", "O", "O", "O",  1 , "O",  1 , "O", "O", "O", "O", "O", "W", "W", "W", "W"],
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
2:"D",
3:"D",
4:"angel1"
}
























def build_battlefield(mission, mission_foes, players):
    widgetlist = []
    for x in range(len(mission)):
        widgetlist.append([])
        for y in range(len(mission[x])):
            if mission[x][y] == 0:
                i1 = Button(battlefield, image = gifplayer)
                for p in players:
                    players[p].x = x
                    players[p].y = y
                return players
            elif mission[x][y] == 1:
                i1 = Button(battlefield, image = gifone)
            elif mission[x][y] == 2:
                i1 = Button(battlefield, image = giftwo)
            elif mission[x][y] == 3:
                i1 = Button(battlefield, image = gifthree)
            elif mission[x][y] == 4:
                i1 = Button(battlefield, image = giffour)
            elif mission[x][y] == 5:
                i1 = Button(battlefield, image = giffive)
            elif mission[x][y] == 6:
                i1 = Button(battlefield, image = gifsix)
            elif mission[x][y] == 7:
                i1 = Button(battlefield, image = gifseven)
            elif mission[x][y] == 8:
                i1 = Button(battlefield, image = gifeight)
            elif mission[x][y] == 9:
                i1 = Button(battlefield, image = gifnine)
            elif mission[x][y] == "W":
                i1 = Button(battlefield, image = gifwall)
            elif mission[x][y] == "O":
                i1 = Button(battlefield, image = gifleer)
            elif mission[x][y] == "B":
                i1 = Button(battlefield, image = gifbarricada)
            elif mission[x][y] == "T":
                i1 = Button(battlefield, image = giftreasure)
            elif mission[x][y] == "L":
                i1 = Button(battlefield, image = gifloot)
            elif mission[x][y] == "R":
                i1 = Button(battlefield, image = gifwerewolf)
            elif mission[x][y] == "V":
                i1 = Button(battlefield, image = gifvampire)
            elif mission[x][y] == "E":
                i1 = Button(battlefield, image = gifangel)
            else:
                try:
                    if mission_foes[mission[x][y]] == "D":
                        i1 = Button(battlefield, image = gifdoor)
                except KeyError:
                    pass
            i1.grid(row = x, column = y)
            widgetlist[y][x].append(i1)
    return widgetlist



def race_choice2(e1, r1, r2, r3, r4, race, players):
    name = e1.get()
    e1.grid_forget()
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    if race == 0:
        player = Engel(name)
        players.append(player)
    if race == 1:
        player = Vampir(name)
        players.append(player)
    if race == 2:
        player = Werwolf(name)
        players.append(player)
    if race == 3:
        player = Golem(name)
        players.append(player)
    else:
        print("Error - no race or name chosen")
    return players

def race_choice(l1, b1, r1, r2, r3, r4, o):
    players = []
    l1.grid_forget()
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    for i in range(int(o)):
        l1 = Label(textwin, text = "Und wer und was bist du überhaupt? (Spieler {})".format(i))
        l1.grid(row = 0)
        # Radiobutton(race) - Engel, Vampir, Werwolf, Golem
        race = StringVar()
        r1 = Radiobutton(textwin, text = "Engel", value = 1, variable = race)
        r1.grid(row = 1)
        r2 = Radiobutton(textwin, text = "Vampir", value = 2, variable = race)
        r2.grid(row = 2)
        r3 = Radiobutton(textwin, text = "Werwolf", value = 3, variable = race)
        r3.grid(row = 3)
        r4 = Radiobutton(textwin, text = "Golem", value = 4, variable = race)
        r4.grid(row = 4)
        # Textfeld - name
        name = StringVar()
        e1 = Entry(textwin, textvariable = name).grid(row = 5)
        b1.grid_forget()
        b1 = Button(textwin, text = "Bestätigen", command=lambda: race_choice2(e1, r1, r2, r3, r4, race, players))
        b1.grid(row = 3)
    l1.grid_forget()
    l1 = Label(textwin, text = "Glückwunsch zu eurer neuen Gruppe. jetzt \n kann man euch endlich auf die Welt loslassen.... \n "
                               "Aber wohin genau? (LEVELWAHL)")
    l1.grid(row = 0)
    # radiobutton.grid_forget()
    b1.grid_forget()
    b1 = Button(textwin, text = "Level 1", command = lambda: build_battlefield(chapter_one, chapter_one_foes, players))
    b1.grid(row = 19)

def intro4(l1, b1):
    l1.grid_forget()
    l1 = Label(textwin, text = "Aber kommen wir zu den wirklich wichtigen \nFragen des Lebens: wie viele seid ihr überhaupt?")
    l1.grid(row = 0)
    b1.grid_forget()
    # Radiobutton(o)
    v = IntVar()
    r1 = Radiobutton(textwin, text = "Einer", value = 1, variable = v)
    r1.grid(row = 1)
    r2 = Radiobutton(textwin, text = "Zwei", value = 2, variable = v)
    r2.grid(row = 2)
    r3 = Radiobutton(textwin, text = "Drei", value = 3, variable = v)
    r3.grid(row = 3)
    r4 = Radiobutton(textwin, text = "Vier", value = 4, variable = v)
    r4.grid(row = 4)
    b1 = Button(textwin, text = "Weiter", command = lambda: race_choice(l1, b1, r1, r2, r3, r4, v))
    b1.grid(row = 9, column = 0)

def intro3(l1, b1):
    l1.grid_forget()
    l1 = Label(textwin, text = "Aber bevor ihr gleich desillusioniert werdet, weil \neuer kurzes Leben keinen "
                               "Sinn macht \n(Ihr wisst das, ihr kennt das Leben nach dem Tod)\n denkt daran, "
                               "die Menschheit hat sich eine Menge \ntoller Dinge einfallen lassen, die man mit Geld\n"
                               "kaufen kann.")
    l1.grid(row = 0)
    b1.grid_forget()
    b1 = Button(textwin, text = "Weiter", command = lambda: intro4(l1, b1))
    b1.grid(row = 1)


def intro2(l1, b1):
    l1.grid_forget()
    l1 = Label(textwin, text = "Statt nun irgendetwas sinnvolles zu tun, tolles \n übernatürliches Zeug, "
                               "besteht euer Alltag in \n nichts, außer euer übernatürliches Leben \n für Geld aufs Spiel zu setzen.\n")
    l1.grid(row = 0)
    b1.grid_forget()
    b1 = Button(textwin, text = "Weiter", command = lambda: intro3(l1, b1))
    b1.grid(row = 1)

def intro1():
    l1 = Label(textwin, text = "Das hier ist Treasure Hunting. Ihr seid über-\n natürliche Wesen, auf die Erde gesandt von \nIHM.\n")
    l1.grid(row = 0)
    b1 = Button(textwin, text = "Weiter", command = lambda: intro2(l1, b1))
    b1.grid(row = 1)

def main():
    pass


intro1()
#test:
players = []
player1 = Engel("Emil")
players.append(player1)
build_battlefield(chapter_one, chapter_one_foes, players)
print(player1.x, player1.y, player1.name, player1.race)

mainloop()