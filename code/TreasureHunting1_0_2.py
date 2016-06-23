#! /usr/bin/env python3


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
        print('Erz\xfcrne IHN nicht mit einer falschen Angabe!')
        new_race = input("Welcher Rasse soll es angehoeren? 1: Vampir \n 2: Werwolf \n 3:Engel")
        race_choice(new_race)
    return new_race


def char_create():
    # Player Character Creation. here is the place where legends are born. and taunted.
    print("Und wieder schickt ER einen seiner Diener auf die Erde.")
    print("Wie es schon tausendmal passiert ist, ohne dass der gewoehnliche Mensch davon etwas mitbekommen würde.")
    print("Wie alle anderen Astralwesen davor hat er nur ein Ziel...")
    input("Press Enter to continue...")
    print()
    print("UNHEIL.")
    print()
    input("Press enter to continue")
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


def movement(agi, kon, race):
    if race == "Engel":
        return int((kon * 3 + agi * 8) / 10) + 1
    else:
        return int((kon * 3 + agi * 8) / 10)


def melee_skill(srg, ges):
    return int(srg * 5 + ges * 3)


def gun_skill(agi, ges):
    return int(agi * 3 + ges * 7)


def level_up(level, experience):
    # has to be called every time the player earns experience. need to add a skill system in this function
    if experience >= level * 5 + 20:
        experience -= level * 5 + 20
        level += 1
        lst = [level, experience]
        return lst


def main_menu():
    # why is this still in english?
    print("   ####################")
    print("#### Treasure Hunting ####")
    print("   ####################")
    print()
    print("(n)ew game")
    print("(l)oad game")
    print("(e)xit")
    i = input()
    if i == "n":
        start_game()
    if i == "l":
        pass
    # load savegame file and proceed to the actual game?
    if i == "e":
        print("Good bye!")
        quit()
    else:
        # goddamn, i really need a better solution for this...
        main_menu()


# Turn
def your_turn(player):
    move = True
    shoot_fight = True
    if player.morph == True:
        morphed = input("Willst du dich verwandeln? y/n")
        if morphed == "y":
            morphed = True
            move = False
            shoot_fight = False
        else:
            morphed = False
    if move == True:
        print("Wohin willst du gehen? du hast %s Schritte." % (str(movement(player))))
        s = [input("wasd: ")]
        steps = []
        for i in range(movement(player)):
            if s[i] in "wasd":
                steps.append(s[i])
            # call walk-function with steps-list
    if shoot_fight == True:
        foes = show_foes()
        print("Wen willst du angreifen?")
        print("0: nichts tun")
        for i in foes:
            if near(foes[i]) == True:
                # is the enemy in range? shoot or fight him? maybe you cant shoot if you are in direct combat?
                print(str(foes[i]) + ": angreifen")
            elif sight(foes[i]) == True:
                # is the enemy in sight line? then you can shoot him:
                print(str(foes[i]) + ": schiessen")
        action = input()
        attack(action)  # function has to be build
    print("Deine Gegner sind am Zug...")
    print()


def show_foes():
    # returns a list of enemies on the map
    pass


'''
now we could use a simple gui to display the battlefield in a different window - lets take tkinter, even if i have no clue how to use it <3

# print out the battlefield - GUI?
from tkinter import *
def new_window():
	# das Fenster selbst festlegen
	top = Tk()
	F = Frame(top)
	F.pack()
	F.master.title("Schlachtfeld - Treasure Hunting")
	
	# die Widgets hinzufügen
	lHello = Label(F, text="Hier sollte man eig das Schlachtfeld sehen...")
	lHello.pack()
	bQuit = Button(F, text="Quit", command=F.quit)
	bQuit.pack()
	
	# bringt die Schleife ans Laufen
	top.mainloop()
'''

'''
OK, enough with functions and classes! 
let's get started with the actual game!
'''


def start_game():  # is called by main_menu-function - base architecture?
    player = char_create()
    player.print_char(player.name, player.race, player.kon, player.srg, player.ges, player.agi, player.hp, player.level, player.bitcoins)
    main_menu()

main_menu()



