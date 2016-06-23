#! /usr/bin/env python3

__author__ = 'medusa'
# IMPORTS
from tkinter import *
from tkinter import messagebox
from random import randint
import time
# from tkinter import imagetk

# WINDOW FUNCTIONS
def mquit():
    mexit = messagebox.askyesno(title="Quit", message="Wirklich beenden?")
    if mexit > 0:
        battlefield.destroy()

# MAIN FRAME
battlefield = Tk()
battlefield.geometry('+680+100')
battlefield.title("Schlachtfeld - Treasure Hunting")

# MENU
# menubar = Menu(battlefield)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "Close", command = mquit)
# menubar.add_cascade(label = "File", menu=filemenu)
# battlefield.config(menu = menubar)

# TEXTLINES
blackline = Label(bg = "black") # black line to separate battlefield from textlines
blackline.grid(row = 99)
line1 = Label(text = " ") # first text line
line1.grid(row = 100)
line2 = Label(text = " ") # second text line
line2.grid(row = 101)
line3 = Label(text = " ") # third text line
line3.grid(row = 102)

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
# Gun-Upgrades
def longrifle(player, gun):
    if gun[1] < 2:
        gun[0][3] += 2
        gun[1] += 1
        return player.inventar.remove("Verlängerter Lauf"), gun
        print("Diese Waffe hat jetzt einen verlängerten Lauf.")
    else:
        print("Diese Waffe ist bereits zu modifiziert.")


def longrifleminus(player, gun):
    gun[0][3] -= 2
    gun[1] -= 1
    return player.inventar.append("Verlängerter Lauf"), gun
    print("Der verlängerte Lauf wurde abgenommen.")


def expanding(player, gun):
    if gun[1] < 2:
        gun[0][2] += 5
        gun[1] += 1
        return player.inventar.remove("Laufbeschleuniger"), gun
        print("Diese Waffe hat jetzt einen Laufbeschleuniger.")
    else:
        print("Diese Waffe ist bereits zu modifiziert.")


def expandingminus(player, gun):
    gun[0][2] -= 5
    gun[1] -= 1
    return player.inventar.append("Laufbeschleuniger"), gun
    print("Der Laufbeschleuniger wurde ausgebaut.")


def mechanics(player, gun):
    if gun[1] < 2:
        gun[0][1] += 1
        gun[1] += 1
        return player.inventar.remove("Verbesserte Mechanik"), gun
        print("Diese Waffe hat jetzt eine verbesserte Mechanik.")
    else:
        print("Diese Waffe ist bereits zu modifiziert.")


def mechanicsminus(player, gun):
    gun[0][1] -= 1
    gun[1] -= 1
    return player.inventar.append("Verbesserte Mechanik"), gun
    print("Die verbesserte Mechanik wurde ausgebaut.")


def lightgun(player, gun):
    if gun[1] < 2:
        player.movement += 1
        gun[1] += 1
        return player.inventar.remove("Teilmantelgeschosse"), gun, player.movement
        print("Diese Waffe ist jetzt leichter.")
    else:
        print("Diese Waffe ist bereits zu modifiziert.")


def lightgunminus(player, gun):
    player.movement -= 1
    gun[1] -= 1
    return player.inventar.append("Teilmantelgeschosse"), gun, player.movement
    print("Die Waffe wurde wieder schwerer.")


def silverbullets(player, gun):
    if gun[1] < 2:
        gun[2] = True
        gun[1] += 1
        return player.inventar.remove("Silberkugeln"), gun
        print("Diese Waffe schießt jetzt mit Silberkugeln.")
    else:
        print("Diese Waffe ist bereits zu modifiziert.")


def silverbulletsminus(player, gun):
    gun[2] = False
    gun[1] -= 1
    return player.inventar.append("Silberkugeln"), gun
    print("Die Silberkugeln wurden ausgetauscht.")


# Tech-Upgrades




# # # # # #
# CLASSES #
# # # # # #
# Characters
class Character():
    # This is the main character class, not only for player characters
    def __init__(self, name, race, kon, srg, ges, agi):
        self.name = name
        self.race = race
        self.kon = kon  # Constitution
        self.srg = srg  # Strength
        self.ges = ges  # ABility
        self.agi = agi  # AGility
        self.hp = self.kon * 8 + self.srg * 5 + 10  # Health Points

    inventar = []
    bitcoins = 50
    level = 1
    experience = 0
    gun = [nogun, 0, False]
    sword = nosword

    def print_char(self, name, race, kon, srg, ges, agi, hp, level, bitcoins):
        # print out character
        print("----- Spielercharakter -----")
        print("NAME: {}   LEVEL: {}   RASSE: {}".format(name, str(level), race))
        print("Bitcoins: {}".format(str(bitcoins)))
        print('WERTE: ')
        print("Leben: {} / {}".format(str(hp), str(kon * 8 + srg * 5 + 10)))
        print("Bewegung: {}".format(str(movement(agi, kon, race))))
        print("Nahkampf: {}".format(str(melee_skill(srg, ges))))
        print("Fernkampf: {}".format(str(gun_skill(agi, ges))))
        print("ATTRIBUTE: ".format())
        print("Konstitution: {}".format(str(kon)))
        print("Stärke: {}".format(str(srg)))
        print("Geschicklichkeit: {}".format(str(ges)))
        print("Schnelligkeit: {}".format(str(agi)))
        print("----------------------------")

    def level_up(level, experience):
        # has to be called every time the player earns experience. need to add a skill system in this function
        if experience >= level * 5 + 20:
            experience -= level * 5 + 20
            level += 1
            return level, experience


# RACES
class Vampire(Character):
    # race subclass
    def __init__(self, name):
        super().__init__(name, "Vampir", 6, 8, 5, 5)


class Angel(Character):
    # race subclass
    def __init__(self, name):
        super().__init__(name, "Engel", 4, 3, 7, 7)


class Human(Character):
    # race subclass
    def __init__(self, name):
        super().__init__(name, "Mensch", 4, 5, 5, 4)


class Werewolf(Character):
    # race subclass
    def __init__(self, name):
        super().__init__(name, "Werwolf", 4, 5, 5, 4)
        self.morph = True
        self.inventar = ["krallen"]


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
        super().__init__("Werwolf", "werewolf", 5, 8, 6, 6, "random", "silverkrallen", randint(15, 25), 12)


# WERTE
def movement(agi, kon, race):
    if race == "Engel":
        return int((kon * 3 + agi * 8) / 10) + 1
    else:
        return int((kon * 3 + agi * 8) / 10)


def melee_skill(srg, ges):
    return int(srg * 5 + ges * 3)


def gun_skill(agi, ges):
    return int(agi * 3 + ges * 7)


# ACTIONS
def race_choice(new_race):
    # race choice function
    if new_race == "1":
        new_race = "Vampir"
    elif new_race == "2":
        new_race = "Werwolf"
    elif new_race == "3":
        new_race = "Engel"
    else:
        # this is for wrong input, but i think this is a bad solution
        print('Erzuerne IHN nicht mit einer falschen Angabe!')
        new_race = input("Welcher Rasse soll es angehoeren? 1: Vampir \n 2: Werwolf \n 3:Engel")
        race_choice(new_race)
    return new_race


def char_create():
    # Player Character Creation. here is the place where legends are born. and taunted.
    charwin = Tk()
    charwin.geometry('+680+400')
    charwin.title("Charakter - Treasure Hunting")
    intro = Label(charwin, text = "Und wieder schickt ER einen seiner Diener auf die Erde.\n "
                         "Sie leben mitten unter den Menschen, ohne dass sie etwas\n"
                         "davon ahnen. Wie alle SEINER Wesen vor ihm hat er nur\n"
                         "ein Ziel:\n"
                         "\n"
                         "UNHEIL.")
    intro.grid()
    new_name = input("Wie soll das neue Wesen heissen? ")
    new_race = input("Welcher Rasse soll es angehoeren? \n 1: Vampir \n 2: Werwolf \n 3: Engel \n")
    new_race = race_choice(new_race)
    print()
    if new_race == "Vampir":
        print("Eine weise Wahl. Du Fetischist.")
        player = Vampire(new_name)
    elif new_race == "Werwolf":
        print("Aah, ein Rowdy!")
        player = Werewolf(new_name)
    else:
        print("Schwuchtel.")
        player = Angel(new_name)
    print()
    print()
    print("Du erwachst nach einem langen Flug...")
    print()
    return player


def show_foes(mission, mission_foes):  # returns a list of enemies at the beginning of the game
    result = []
    i = -1
    for x in range(len(mission)):
        for y in range(len(mission[x])):
            if mission[x][y] == 1:
                i += 1
                result.append(
                    [i, str(mission_foes[1]), x, y, 0, 0])  # id, name, y-coordinate, x-coordinate, damage taken, stun
            elif mission[x][y] == 2:
                i += 1
                result.append([i, str(mission_foes[2]), x, y, 0, 0])
            elif mission[x][y] == 3:
                i += 1
                result.append([i, str(mission_foes[3]), x, y, 0, 0])
            elif mission[x][y] == 4:
                i += 1
                result.append([i, str(mission_foes[4]), x, y, 0, 0])
            elif mission[x][y] == 5:
                i += 1
                result.append([i, str(mission_foes[5]), x, y, 0, 0])
            elif mission[x][y] == 6:
                i += 1
                result.append([i, str(mission_foes[6]), x, y, 0, 0])
            elif mission[x][y] == 7:
                i += 1
                result.append([i, str(mission_foes[7]), x, y, 0, 0])
            elif mission[x][y] == 8:
                i += 1
                result.append([i, str(mission_foes[8]), x, y, 0, 0])
            elif mission[x][y] == 9:
                i += 1
                result.append([i, str(mission_foes[9]), x, y, 0, 0])
            elif mission[x][y] == "E":
                i += 1
                result.append([i, str(mission_foes["E"]), x, y, 0, 0])
            elif mission[x][y] == "V":
                i += 1
                result.append([i, str(mission_foes["V"]), x, y, 0, 0])
            elif mission[x][y] == "R":
                i += 1
                result.append([i, str(mission_foes["R"]), x, y, 0, 0])
    return result  # returns list of all enemies on the battlefield aka foelist


def near(playerx, playery, id, foelist):  # tests if the enemy is near the player
    if playerx + 1 == foelist[id][2] or playerx - 1 == foelist[id][2] and playery + 1 == foelist[id][3] or playery - 1 == foelist[id][3]:
        return True
    else:
        return False


def sight(playerx, playery, foelist):  # tests if the player can see an enemy, returns a list of enemies
    pass


def melee_damage(player, id, foelist, target):  # deals melee damage
    damage = player.srg * 5 + player.sword[1]  # Damage the player deals
    if randint(0, 10) < player.sword[2] * 10:  # critical hit
        damage *= 2
    elif target.race == "angel" or target.race == "vampire" or target.race == "werewolf" and player.sword[6] == True:
        damage *= 2
    if randint(0, 10) < player.sword[3] * 10:
        foelist[id][5] += 1
        print("Dein Gegner taumelt!")
    return damage


def gun_damage(player, id, foelist, target):  # deals range damage
    damage = player.gun[2]
    if target.race == "angel" or target.race == "vampire" or target.race == "werewolf" and player.gun[2] == True:
        damage *= 2
    print("you dealed {} damage.".format(str(damage)))
    return damage


def dead(player, id, foelist, target, mission):  # tests if an enemy is dead and removes him
    if foelist[id][4] >= target.kon * 8 + target.srg * 5 + 10:
        x = foelist[id][2]
        y = foelist[id][3]
        player.experience += target.experience  # Experience gain
        player.level_up(player.level, player.experience)  # test for Level up
        money = target.loot  # Gain Loot
        player.bitcoins += money
        print("Dein Gegner ist gestorben. Du erhältst {} Erfahrung und {} Bitcoins.".format(target.experience, money))
        mission[x][y] = "O"  # erase enemy from missionlist
        widgetlist[x][y].grid_remove()  # erase enemy from GUI
        logo = PhotoImage(file="Images/0leer.gif")
        w1 = Label(battlefield, image=logo)
        w1.logo = logo
        w1.grid(row=x, column=y)  # place an empty field
        foelist.remove(id)  # erase enemy from foelist
        return player, foelist, mission


def attack(player, action, foelist, mission):  # processes a single attack
    id = int(action) - 1
    if action == 0:
        pass
    else:
        if foelist[id][1] == "police":
            target = Police()
        if foelist[id][1] == "security":
            target = Security()
        if foelist[id][1] == "mercenary":
            target = Mercenary()
        if foelist[id][1] == "soldier":
            target = Soldier()
        if foelist[id][1] == "taskforce":
            target = Taskforce()
        if foelist[id][1] == "criminal":
            target = Criminal()
        if foelist[id][1] == "terrorist":
            target = Terrorist()
        if foelist[id][1] == "silver1":
            target = Silver1()
        if foelist[id][1] == "silver2":
            target = Silver2()
        if foelist[id][1] == "angel1":
            target = Angel1()
        if foelist[id][1] == "angel2":
            target = Angel2()
        if foelist[id][1] == "vampire1":
            target = Vampire1()
        if foelist[id][1] == "vampire2":
            target = Vampire2()
        if foelist[id][1] == "werewolf1":
            target = Werewolf1()
        if foelist[id][1] == "werewolf2":
            target = Werewolf2()
        if near(playerx, playery, id,
                foelist) == True:  # direct attack, with the melee_skill and the sword of the player.
            if melee_skill(player.srg, player.ges) + randint(0, 50) > melee_skill(target.srg, target.ges) + randint(0,
                                                                                                                    20):
                if randint(1, 100) > 10:
                    damage = melee_damage(player, id, foelist, target)
                    print("Du hast getroffen!")
            else:
                print("Daneben!")
        else:
            if 100 - gun_skill(player.agi, player.ges) < randint(0, 100):
                if randint(1, 100) > 10:
                    print("Du hast getroffen!")
                    damage = gun_damage(player, id, foelist, target)
            else:
                print("Daneben!")
        foelist[id][4] += damage  # Here comes the damage!!
        dead(player, id, foelist, target, mission)


def walk(playerx, playery, steps, mission,
         mission_foes):  # walk from player coordinates to the point where steps[] directs
    for i in range(len(steps)):
        time.sleep(0.2)
        try:
            if steps[i] == "w":
                if mission[playery-1][playerx] == "O":
                    widgetlist[playery][playerx].configure(image = gifleer)  # remove player from GUI
                    widgetlist[playery-1][playerx].configure(image = gifplayer)  # remove target from GUI
                    mission[playery-1][playerx] = 0  # player missionlist entry
                    mission[playery][playerx] = "O"  # left place missionlist entry
                    playery -= 1
                elif mission_foes[mission[playery-1][playerx]] == "D":
                    pass  # go to target level
                else:
                    pass
            elif steps[i] == "a":
                if mission[playery][playerx-1] == "O":
                    widgetlist[playery][playerx].configure(image = gifleer)  # remove player from GUI
                    widgetlist[playery][playerx-1].configure(image = gifplayer)  # remove target from GUI
                    mission[playery][playerx-1] = 0  # player missionlist entry
                    mission[playery][playerx] = "O"  # left place missionlist entry
                    playerx -= 1
                elif mission_foes[mission[playery][playerx-1]] == "D":
                    pass  # go to target level
                else:
                    pass
            elif steps[i] == "d":
                if mission[playery][playerx+1] == "O":
                    widgetlist[playery][playerx].configure(image = gifleer)  # remove player from GUI
                    widgetlist[playery][playerx+1].configure(image = gifplayer)  # remove target from GUI
                    mission[playery][playerx+1] = 0  # player missionlist entry
                    mission[playery][playerx] = "O"  # left place missionlist entry
                    playerx += 1
                elif mission_foes[mission[playery][playerx+1]] == "D":
                    pass  # go to target level
                else:
                    pass
            if steps[i] == "s":
                if mission[playery+1][playerx] == "O":
                    widgetlist[playery][playerx].configure(image = gifleer)  # remove player from GUI
                    widgetlist[playery+1][playerx].configure(image = gifplayer)  # remove target from GUI
                    mission[playery+1][playerx] = 0  # player missionlist entry
                    mission[playery][playerx] = "O"  # left place missionlist entry
                    playery += 1
                elif mission_foes[mission[playery+1][playerx]] == "D":
                    pass  # go to target level
                else:
                    pass
        except KeyError:
            pass
    return playerx, playery, mission

def morph(y, n):
    morphed = True
    y.grid_forget()
    n.grid_forget()
    return morphed
def morph1(y, n):
    morphed = False
    y.grid_forget()
    n.grid_forget()
    return morphed

def your_turn(player, foelist, mission, mission_foes):
    move = True
    shoot_fight = True
    try:
        if player.morph == True:
            line1.configure(battlefield, text = "willst du dich verwandeln?")
            y = Button(battlefield, text = "Verwandeln", command = lambda: morph(y, n))
            y.grid(row = 103, column = 0)
            n = Button(battlefield, text = "Menschlich bleiben", command = lambda: morph1(y, n))
            n.grid(row = 103, column = 1)
            if morphed == True:
                move = False
                shoot_fight = False
                print("Du verwandelst dich in einen Werwolf!")
            else:
                print("Deine Instinkte schlafen weiter und du bleibst menschlich.")
    except AttributeError:
        pass
    if move == True:
        print("Wohin willst du gehen? du hast %s Schritte." % (str(movement(player.agi, player.kon, player.race))))
        s = input("wasd: ")
        s.lower()
        steps = []
        for i in range(movement(player.agi, player.kon, player.race)):
            try:
                if s[i] in "wasd":
                    steps.append(s[i])
            except IndexError:
                pass
        walk(playerx, playery, steps, mission, mission_foes)  # call walk-function with steps-list
    if shoot_fight == True:
        print("Wen willst du angreifen?")
        print("0: nichts tun")
        # testen ob ein Gegner dem Spieler nah ist - nah oder fernkampf, wieviel Schuss?
        # auf Befehl des Spielers warten
        # klick des Spielers einlesen
        # attack(), damage(), dead()
        '''for i in range(len(foelist)):  # This is not ready yet... i should test it (haha), i think here are some logical bugs.
            # this for-loop.... i think right now you get one attack a turn for every enemy on the field.
            if near(playerx, playery, i, foelist) == True:
                directcombat = True  # is the enemy in range? shoot or fight him? maybe you cant shoot if you are in direct combat?
                print(str(foelist[i][0] + 1) + ": angreifen")
                action = input()
                attack(player, action, foelist, mission)
            elif sight(playerx, playery, foelist[i]) == True:
                shots = range(player.gun[1])
                print("Du hast diese Runde {} Schuss!".format(str(player.gun[0[1]])))
                while shots >= 0:
                    if directcombat == False:  # is the enemy in sight line? then you can shoot him:
                        print(str(foelist[i][0] + 1) + ": schiessen")
                        action = input()
                        attack(player, action, foelist, mission)
                        print("Du hast noch {} Schüsse übrig!".format(str(shots)))
                        shots -= 1
                    else:
                        pass
        '''
    print("Deine Gegner sind am Zug...")
    print()


# BUILD BATTLEFIELD FUNCTION
# mission has to be a list of lists: first columns, then rows. each variable in the list(s) is a placeholder for one field.
# mission_foes is a dictionary: it gives various integers the str(names) of the enemy, which stands there.
def build_battlefield(mission, mission_foes):
    widgetlist = []
    for x in range(len(mission)):
        widgetlist.append([])
        for y in range(len(mission[x])):  # place the new field at .grid(row = x, column = y)
            if mission[x][y] == 0:
                w1 = Button(battlefield, image=gifplayer)
                w1.grid(row=x, column=y)
                global playerx
                playerx = x
                global playery
                playery = y
            elif mission[x][y] == 1:
                w1 = Button(battlefield, image=gifone)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 2:
                w1 = Button(battlefield, image=giftwo)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 3:
                w1 = Button(battlefield, image=gifthree)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 4:
                w1 = Button(battlefield, image=giffour)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 5:
                w1 = Button(battlefield, image=giffive)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 6:
                w1 = Button(battlefield, image=gifsix)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 7:
                w1 = Button(battlefield, image=gifseven)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 8:
                w1 = Button(battlefield, image=gifeight)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 9:
                w1 = Button(battlefield, image=gifnine)
                w1.grid(row=x, column=y)
            elif mission[x][y] == 'W':
                w1 = Button(battlefield, image=gifwall)
                w1.grid(row=x, column=y)
            elif mission[x][y] == "E":
                w1 = Button(battlefield, image=gifangel)
                w1.grid(row=x, column=y)
            elif mission[x][y] == "V":
                w1 = Button(battlefield, image=gifvampire)
                w1.grid(row=x, column=y)
            elif mission[x][y] == "R":
                w1 = Button(battlefield, image=gifwerewolf)
                w1.grid(row=x, column=y)
            elif mission[x][y] == "L":
                w1 = Button(battlefield, image=gifloot)
                w1.grid(row=x, column=y)  # place a loot image: generate random loot.
            elif mission[x][y] == "B":
                w1 = Button(battlefield, image=gifbarricada)
                w1.grid(row=x, column=y)  # place a barricade
            elif mission[x][y] == "T":
                w1 = Button(battlefield, image=giftreasure)
                w1.grid(row=x, column=y)  # place the Treasure
            elif mission[x][y] == "O":
                w1 = Button(battlefield, image=gifleer)
                w1.grid(row=x, column=y)  # place an empty field
            else:
                try:
                    if str(mission_foes[str(mission[x][y])]) == "D":
                        w1 = Button(battlefield, image=gifdoor)
                        w1.grid(row=x, column=y)
                except KeyError:
                    pass
            widgetlist[x].append(w1)
    return widgetlist  # return the player coordinates


def show_legend():
    legend = Tk()
    legend.geometry('+250+100')
    legend.title("Legende - Treasure Hunting")
    w1 = Label(legend, image=gifwall)
    w1.grid(row=0, column=0)
    w1 = Label(legend, text="Mauer").grid(row=0, column=1)
    w1 = Label(legend, image=gifleer)
    w1.grid(row=1, column=0)
    w1 = Label(legend, text="Boden").grid(row=1, column=1)
    w1 = Label(legend, image=gifbarricada)
    w1.grid(row=1, column=0)
    w1 = Label(legend, text="Stacheldraht").grid(row=1, column=1)

    # legend.mainloop()


# TEST PARAGRAPH
# mission list:
chapter_one = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "O", "O", "O", "T", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "O", "O", 1, "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "E", "O", "L", "O", "O", "W"],
    ["W", "O", 1, "O", "O", "W", "W", "W", "W", "W", "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
    ["W", "O", "B", "B", "B", "W", "W", "W", "main", "main", "W", "W", "W", "W", "O", "O", "O", "W", "W", "W", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W", "W", "W", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "police", "W", "W", "W"],
    ["W", "O", "O", "O", "E", "O", "O", "O", "O", 1, "O", 1, "O", "O", "O", "O", "O", "W", "W", "W", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W", "W", "W", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", 1, "O", "O", "O", 1, "O", "O", "O", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "B", "B", "B", "B", "B", "B", "B", "O", "O", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "W"],
    ["W", "O", "O", "O", "O", "O", 1, "O", "O", "O", 1, "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "W", 0, "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]]
# missions_foes dictionary:
chapter_one_foes = {
    1: "police",
    "main": "D",
    "police": "D",
    "E": "angel1",
    "W": 0,
    "V": "vampire1",
    "O": 0,
    "B": 0,
    "T": 0,
    "L": 0,
    "R": "werewolf1"
}

# Game
# character creation
# show_legend()
player = char_create()
widgetlist = build_battlefield(chapter_one, chapter_one_foes)
foelist = show_foes(chapter_one, chapter_one_foes)
your_turn(player, foelist, chapter_one, chapter_one_foes)
your_turn(player, foelist, chapter_one, chapter_one_foes)
your_turn(player, foelist, chapter_one, chapter_one_foes)
your_turn(player, foelist, chapter_one, chapter_one_foes)


# has to be at the end
# battlefield.
mainloop()




