#Brian Weed February 2019
#Text based Apex Legends Simulator
#definitely not finished

from random import randint
import time

print("Are you ready to be the Apex Champion?")
time.sleep(2)
print("Choose Your Squad.")

Legends = {"Bloodhound":0.1,"Gibraltar":0.05, "Lifeline":0.15, "Pathfinder":0.1, "Wraith":0.15, "Bangalore":0.25, "Caustic":0.07, "Mirage":0.1, "Hyper":1}
#Legends to choose from and their individual win multiplier

squad1 = ""
squad2 = ""
squad3 = ""

HighTierLoot = ["Artillery","Relay","The Pit","Runoff","Bunker","Airbase","Swamps","Repulsor","Thunderdome","Water Treatment"] #going to expand on multiplier for certain random drops in the future
MidTierLoot = ["Slum Lakes", "Cascades","Wetlands","Bridges","Skull Town"]
LowTierLoot = ["Hydro Dam","Market"]

dropArea = randint(0,9) #variables required for the next multiplier
dropAreaMulti = 0
baseline_squad_multi = 0
SquadAll = []  #Keeps a list of the squad names, could be useful later


def choose_squad():
    global squad1
    global squad2
    global squad3
    global baseline_squad_multi
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
    baseline_squad_multi = Legends[squad1] + Legends[squad2] + Legends[squad3]


def get_dropzone():
    global dropAreaMulti
    if dropArea <= 2:
        time.sleep(1)
        print("You\'re dropping in: " + LowTierLoot[randint(0,1)] + "!")
        dropAreaMulti = 0.1
    if  2 < dropArea <= 6:
        time.sleep(1)
        print("You\'re dropping in: " + MidTierLoot[randint(0,4)] + "!")
        dropAreaMulti = 0.25
    if dropArea > 6:
        time.sleep(2)
        print("You\'re dropping in: " + HighTierLoot[randint(0,9)] + "!")
        dropAreaMulti = 0.5







choose_squad();
time.sleep(2)
print("The squad is all set, lets see where we're dropping.")
get_dropzone();
print(SquadAll)





