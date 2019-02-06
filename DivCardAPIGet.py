import requests
import json
import copy
import csv
import pandas

leagueName = "Betrayal"                                                                             #League name easily to update
divCardAPI = "http://poe.ninja/api/Data/GetDivinationCardsOverview?league=" + leagueName
prophecyAPI = "http://poe.ninja/api/Data/GetProphecyOverview?league=" + leagueName
fragmentAPI = "http://poe.ninja/api/Data/GetFragmentOverview?league=" + leagueName
uniqueMapAPI = "http://poe.ninja/api/Data/GetUniqueMapOverview?league=" + leagueName                #all APIs required to parse card outcomes
uniqueAccessoryAPI = "http://poe.ninja/api/Data/GetUniqueAccessoryOverview?league=" + leagueName
uniqueArmourAPI = "http://poe.ninja/api/Data/GetUniqueArmourOverview?league=" + leagueName
uniqueFlaskAPI = "http://poe.ninja/api/Data/GetUniqueFlaskOverview?league=" + leagueName
uniqueWeaponAPI = "http://poe.ninja/api/Data/GetUniqueWeaponOverview?league=" + leagueName

divCardDict = {}
divCardListofDict = []                                                                              #global variables for building lists and dictionaries

#Hand picked cards with parseable outcomes
goodDivCards = ['A Dab of Ink', 'A Mother\'s Parting Gift', 'Anarchy\'s Price', 'Audacity', 'Beauty Through Death', 'Death', 'Forbidden Power', 'Humility',
                'Hunter\'s Reward', 'Immortal Resolve', 'Might is Right', 'Pride Before the Fall', 'Rats', 'Rebirth',
                'The Army of Blood','The Artist','The Beast','The Betrayal','The Blazing Fire','The Brittle Emperor','The Coming Storm',
                'The Conduit','The Cursed King','The Darkest Dream','The Demoness', 'The Doctor','The Dragon','The Dragon\'s Heart','The Drunken Aristocrat',
                'The Endless Darkness', 'The Enlightened', 'The Fathomless Depths','The Feast','The Fiend','The Fletcher','The Formless Seas','The Forsaken', 'The Harvester',
                'The Hermit', 'The Hunger', 'The Immortal', 'The Incantation', 'The Iron Bard', 'The Jeweller\'s Boon', 'The King\'s Heart', 'The Last One Standing', 'The Life Thief',
                'The Lunaris Priestess', 'The Master', 'The Nurse', 'The Oath', 'The Offering', 'The One With All', 'The Pack Leader','The Pact','The Polymath',
                'The Queen', 'The Scarred Meadow', 'The Scavenger','The Soul', 'The Spark and the Flame', 'The Sun', 'The Sword King\'s Salute', 'The Throne',
                'The Valley of Steel Boxes','The Watcher','The Wind', 'The Witch','The Wolf\'s Shadow', 'The Wolven King\'s Bite', 'The World Eater', 'Thunderous Skies', 'Tranquility', 'Wealth and Power']



class APIGet:
    divCardAPIResponse = json.loads(requests.get(divCardAPI).text)  #Calls for the divCardAPI
    # prophecyAPIResponse = json.loads(requests.get(prophecyAPI).text)
    uniqueAccessoryAPIResponse = json.loads(requests.get(uniqueAccessoryAPI).text)
    # uniqueArmourAPIResponse = json.loads(requests.get(uniqueArmourAPI).text)
    # uniqueFlaskAPIResponse = json.loads(requests.get(uniqueFlaskAPI).text)
    # uniqueWeaponAPIResponse = json.loads(requests.get(uniqueWeaponAPI).text)

class DivCardValues:
    def __init__(self, cardname, itemname, value, corrupted):       #setup for appending deserialized values to dictionaries
        self.cardname = cardname
        self.itemname = itemname
        self.value = value
        self.corrupted = corrupted

class ActualItemValue:
    def __init__(self, itemname, item_value, corrupted):
        self.itemname = itemname
        self.item_value = item_value
        self.corrupted = corrupted


for i in APIGet.divCardAPIResponse['lines']:           #parse through initial API list
    if i['name'] in goodDivCards:                           #checks if the card is good
        DivCardValues.cardname = i['name']
        DivCardValues.itemname = str(i['explicitModifiers'][0]['text'])     #setting values to DivCardValues class
        DivCardValues.value = (i['chaosValue']*i['stackSize'])
        if len(i['explicitModifiers']) >= 2:
            DivCardValues.corrupted = True                                      #checking whether the outcome of the card is corrupted or not
            DivCardValues.itemname = "".join(DivCardValues.itemname.rstrip() + 'Corrupted')      #also adds corrupted to the name to differentiate between two of the same items
        else:
            DivCardValues.corrupted = False
        divCardDict['cardname'] = DivCardValues.cardname
        divCardDict['itemname'] = DivCardValues.itemname                #adding keys and values to a temporary dictionary
        divCardDict['value'] = DivCardValues.value
        divCardDict['corrupted'] = DivCardValues.corrupted
        divCardListofDict += [copy.deepcopy(divCardDict)]               #appending the temporary dictionary to the global list of DivCard dictionaries

with open('divcards.csv', 'w') as csv_file:
    fieldnames = ['cardname', 'itemname', 'value','corrupted', 'item_value']   #converts list of dictionaries to a CSV, adds blank field for actual item value.
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in divCardListofDict:
        writer.writerow(i)
colnames = ['cardname','itemname','value','corrupted','item_value']
data = pandas.read_csv('divcards.csv', names=colnames)
itemnames = data.itemname.tolist()

for i in APIGet.uniqueAccessoryAPIResponse['lines']:
    for x in itemnames:
        if i['name'] in x:
            print(i['name'])

