#Brian Weed February 2019
#Text based Apex Legends Simulator
#definitely not finished

from random import randint
import time

Legends = {"Bloodhound":0.1,"Gibraltar":0.1, "Lifeline":0.15, "Pathfinder":0.15, "Wraith":0.30, "Bangalore":0.5, "Caustic":0.14, "Mirage":0.20, "Hyper":.80}
#Legends to choose from and their individual win multiplier

squad1 = ""
squad2 = ""
squad3 = ""

HighTierLoot = ["Artillery","Relay","The Pit","Runoff","Bunker","Airbase","Swamps","Repulsor","Thunderdome","Water Treatment"] #going to expand on multiplier for certain random drops in the future
MidTierLoot = ["Slum Lakes", "Cascades","Wetlands","Bridges","Skull Town"]
LowTierLoot = ["Hydro Dam","Market"]

GoodWeapons = ["Wingman", "Spitfire", "R-99", "Peacekeeper", "EVA-8", "Prowler", "R-301"]
OkayWeapons = ["Flatline", "RE-45", "G7 Scout", "Hemlok", "Longbow", "Devotion"]
BadWeapons = ["Triple Take", "Alternator", "P2020", "Mozambique"]
RareWeapons = ["Mastiff", "Kraber"]

Weapon1 = ""
Weapon2 = ""

dropArea = randint(0,9) #variables required for the next multiplier
dropAreaMulti = 0
droppodLuck = 0.1
weaponTierMulti = 0
baselineSquadMulti = 0
SquadAll = []  #Keeps a list of the squad names, could be useful later
fights_won = []

def choose_squad():
    global squad1
    global squad2
    global squad3
    global baselineSquadMulti
    global SquadAll
    squad1 = input("First Legend: (Type \'list\' for all options)")
    while squad1 == 'list' or squad1 not in Legends:
        print("Bloodhound, Gibraltar, Lifeline, Pathfinder, Wraith, Bangalore, Caustic, Mirage") #Gets user input and makes sure its an option
        squad1 = input("First Legend:")
    squad2 = input("Second Legend: (Type \'list\' for all options)")
    while squad2 == 'list' or squad2 not in Legends or squad2 == squad1:
        print("Bloodhound, Gibraltar, Lifeline, Pathfinder, Wraith, Bangalore, Caustic, Mirage")
        squad2 = input("Second Legend:")
    squad3 = input("Third Legend: (Type \'list\' for all options)")
    while squad3 == 'list' or squad3 not in Legends or squad3 == squad2 or squad3 == squad1:
        print("Bloodhound, Gibraltar, Lifeline, Pathfinder, Wraith, Bangalore, Caustic, Mirage")
        squad3 = input("Third Legend:")
    SquadAll.append(squad1)
    SquadAll.append(squad2)
    SquadAll.append(squad3)
    baselineSquadMulti = Legends[squad1] + Legends[squad2] + Legends[squad3]


def get_dropzone():
    global dropAreaMulti
    if dropArea <= 2:
        time.sleep(1)
        print("You\'re dropping in: " + LowTierLoot[randint(0,1)] + "!") #gets a random drop zone, builds suspense for better drop zones
        dropAreaMulti = 0.1                                              #sets a constant variable for the multiplier of loot tier.
    if  2 < dropArea <= 6:
        time.sleep(1)
        print("You\'re dropping in: " + MidTierLoot[randint(0,4)] + "!")
        dropAreaMulti = 0.25
    if dropArea > 6:
        time.sleep(2)
        print("You\'re dropping in: " + HighTierLoot[randint(0,9)] + "!")
        dropAreaMulti = 0.5

def get_win_fight(x,y):
    i = 0
    maxes = {
        0.5:3,
        0.25:2,
        0.1:1,
    }
    global fights_won

    while i < maxes[x]:
        if randint(0,100) <= (y * 100):
            fights_won.append(True)
            i += 1
        else:
            fights_won.append(False)
            i += 1

def hasWins():
    if fights_won.count(False) >= 1:
        return 0
    if fights_won.count(True)>= 0 and fights_won.count(False) == 0:
        return fights_won.count(True)



def get_droppod_luck(z):
    global droppodLuck
    if "Lifeline"in SquadAll:
        droppodLuck += 0.2
    droppodLuck += z/10



def get_weapon_tier():
    global weaponTierMulti
    global Weapon1
    global Weapon2
    if dropAreaMulti == 0.1:
        Weapon1 = OkayWeapons[randint(0,5)]
        Weapon2 = BadWeapons[randint(0,3)]
    if dropAreaMulti == 0.25:
        Weapon1 = GoodWeapons[randint(0,6)]
        Weapon2 = OkayWeapons[randint(0,5)]
    if dropAreaMulti == 0.5:
        Weapon1 = GoodWeapons[randint(0,6)]
        Weapon2 = GoodWeapons[randint(0,5)]
    if droppodLuck >= 0.4:
        Weapon1 = RareWeapons[randint(0,1)]
    print("You found a {0}, and {1}".format(Weapon1,Weapon2))

def was_champion():
    if fights_won.count(False) == 0:
        return "were"
    else:
        return "were not"
    
    
print("Are you ready to be the Apex Champion?")
time.sleep(2)
print("Choose Your Squad.")
choose_squad()
time.sleep(2)
print("The squad is all set, lets see where we're dropping.")
get_dropzone()
get_droppod_luck(fights_won.count(True))
get_win_fight(dropAreaMulti, baselineSquadMulti)
get_weapon_tier()
time.sleep(2)
print("You won {} fights before the final circle".format(hasWins()))
time.sleep(3)
print("You {} the Apex Champion this time.".format(was_champion()))





