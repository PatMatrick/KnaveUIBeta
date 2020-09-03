
import math
import random
import os
import pickle
import sys

physiquetraits = ["Athletic", "Brawny", "Corpulent", "Delicate", "Gaunt", "Hulking", "Lanky", "Ripped", "Rugged",
                  "Scrawny", "Short", "Sinewy", "Slender", "Flabby", "Statuesque", "Stout", "Tiny", "Towering",
                  "Willowy", "Wiry"]
facetraits = ["Bloated", "Blunt", "Bony", "Chiseled", "Delicate", "Elongated", "Patrician", "Pinched", "Hawkish",
              "Broken", "Impish", "Narrow", "Ratlike", "Round", "Sunken", "Sharp", "Soft", "Square", "Wide", "Wolfish"]
skintraits = ["Battle Scar", "Birthmark", "Burn Scar", "Dark", "Makeup", "Oily", "Pale", "Perfect", "Pierced",
              "Pockmarked", "Reeking", "Tattooed", "Rosy", "Rough", "Sallow", "Sunburned", "Tanned", "War Paint",
              "Weathered", "Whip Scar"]
hairtraits = ["Bald", "Braided", "Bristly", "Cropped", "Curly", "Disheveled", "Dreadlocks", "Filthy", "Frizzy",
              "Greased", "Limp", "Long", "Luxurious", "Mohawk", "Oily", "Ponytail", "Silky", "Topknot", "Wavy", "Wispy"]
clothingtraits = ["Antique", "Bloody", "Ceremonials", "Decorated", "Eccentric", "Elegant", "Fashionable", "Filthy",
                  "Flamboyant", "Stained", "Foreign", "Frayed", "Frumpy", "Livery", "Oversized", "Patched", "Perfumed",
                  "Rancid", "Torn", "Undersized"]
virtuetraits = ["Ambitious", "Cautious", "Courageous", "Courteous", "Curious", "Disciplined", "Focused", "Generous",
                "Gregarious", "Honest", "Honorable", "Humble", "Idealistic", "Just", "Loyal", "Merciful", "Righteous",
                "Serene", "Stoic", "Tolerant"]
vicetraits = ["Aggressive", "Arrogant", "Bitter", "Cowardly", "Cruel", "Deceitful", "Flippant", "Gluttonous", "Greedy",
              "Irascible", "Lazy", "Nervous", "Prejudiced", "Reckless", "Rude", "Suspicious", "Vain", "Vengeful",
              "Wasteful", "Whiny"]
speechtraits = ["Blunt", "Booming", "Breathy", "Cryptic", "Drawling", "Droning", "Flowery", "Formal", "Gravelly",
                "Hoarse", "Mumbling", "Precise", "Quaint", "Rambling", "Rapid-Fire", "Dialect", "Slow", "Squeaky",
                "Stuttering", "Whispery"]
backgroundtraits = ["Alchemist", "Beggar", "Butcher", "Burglar", "Charlatan", "Cleric", "Cook", "Cultist", "Gambler",
                    "Herbalist", "Magician", "Mariner", "Mercenary", "Merchant", "Outlaw", "Performer", "Pickpocket",
                    "Smuggler", "Student", "Tracker"]
misfortunetraits = ["Abandoned", "Addicted", "Blackmailed", "Condemned", "Cursed", "Defrauded", "Demoted", "Discredited",
                    "Disowned", "Exiled", "Framed", "Haunted", "Kidnapped", "Mutilated", "Poor", "Pursued", "Rejected",
                    "Replaced", "Robbed", "Suspected"]
alignmenttrait = ["Law", "Neutrality", "Chaos"]

startingarmortrait = ["No armor", "Gambeson", "Brigandine", "Chain"]

helmetsandshield = ["None", "Helmet", "Shield", "Helmet and Shield"]

dungeongear = ["Rope, 50ft", "Pulleys", "Candles, 5", "Chain, 10ft", "Chalk, 10", "Crowbar", "Tinderbox", "Grapling Hook",
               "Hammer", "Waterskin", "Lantern", "Lamp Oil", "Padlock", "Manacles", "Mirror", "Pole, 10ft", "Sack",
               "Tent", "Spikes, 5", "Torches, 5"]
generalgear1 = ["Air Bladder", "Bear Trap", "Shovel", "Bellows", "Grease", "Saw", "Bucket", "Caltrops", "Chisel",
                "Drill", "Fishing Rod", "Marbles", "Glue", "Pick", "Hourglass", "Net", "Tongs", "Lockpicks",
                "Metal file", "Nails"]
generalgear2 = ["Incense", "Sponge", "Lens", "Perfume", "Horn", "Bottle", "Soap", "Spyglass", "Tar Pot", "Twine",
                "Fake Jewels", "Blank Book", "Card Deck", "Dice Set", "Cook Pots", "Face Paint", "Whistle",
                "Instrument", "Quill & Ink", "Small Bell"]
strstatlist = []
dexstatlist = []
constatlist = []
intstatlist = []
wisstatlist = []
chastatlist = []
alignmentnum = []
armornum= []
helmandshieldnum= []












global PlayerIG

class Player:
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.strbonus = 0
        self.dex = 0
        self.dexbonus = 0
        self.con = 0
        self.conbonus = 0
        self.intel = 0
        self.intelbonus = 0
        self.wis = 0
        self.wisbonus = 0
        self.cha = 0
        self.chabonus = 0
        self.hp = 0
        self.maxhp = 0
        self.armor = 0
        self.level = 0
        self.xp = 0
        self.inventory = {"Basic Clothes": 0}
        self.physique = " "
        self.face = " "
        self.skin = " "
        self.hair = " "
        self.clothing = " "
        self.virtue = " "
        self.vice = " "
        self.speech = " "
        self.background = " "
        self.misfortune = " "
        self.alignment = " "
        self.copper = 0
        self.inventoryslots = 0
        self.currentinventory = 0
        self.rations = 0
        self.currentarmor = ""
        self.helmet = ""
        self.armor = ""
        self.packanimal = ""
        self.animalinventory = {}
        self.animalmaxslots = 0
        self.animalslotsfilled = 0
        self.animal = ""



def startmenu():
    print("                               _  ___   _     __      ________ _    _ _____")
    print("                              | |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("                              | ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("                              |  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("                              | . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("                              |_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
    print("\n")
    print("\n")
    print("                                     Version Beta 1.2 Developed by:")
    print("\n")
    print("                                                 PyRev")
    print("\n")
    print("\n")
    print("                         Hello and Welcome to the Knave Interactive Character Sheet!")
    print("                                       Select an option to continue.")
    print("\n")
    print("                                     1.) Create a new character")
    print("                                     2.) Load Current Character")
    print("                                     3.) Randomly Generate Character")
    option = input("-> ")
    if option == "1":
        startup()
    if option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open("savefile", "rb") as f:
                os.getcwd()
                global PlayerIG
                PlayerIG = pickle.load(f)
                print("Loaded save state...your journey continues!")
                input("->")
                mainscreen()
        else:
            print("No saved data.")
            startmenu()
    if option == "3":
        startuprandom()
    else:
        startmenu()



def randomchar():
    strstatlist.append(random.randint(1, 6) + 10)
    strstatlist.append(random.randint(1, 6) + 10)
    strstatlist.append(random.randint(1, 6) + 10)
    strstatlist.sort()
    PlayerIG.strength = strstatlist[0]
    PlayerIG.strbonus = strstatlist[0] - 10
    dexstatlist.append(random.randint(1, 6) + 10)
    dexstatlist.append(random.randint(1, 6) + 10)
    dexstatlist.append(random.randint(1, 6) + 10)
    dexstatlist.sort()
    PlayerIG.dex = dexstatlist[0]
    PlayerIG.dexbonus = dexstatlist[0] - 10
    constatlist.append(random.randint(1, 6) + 10)
    constatlist.append(random.randint(1, 6) + 10)
    constatlist.append(random.randint(1, 6) + 10)
    constatlist.sort()
    PlayerIG.con = constatlist[0]
    PlayerIG.conbonus = constatlist[0] - 10
    intstatlist.append(random.randint(1, 6) + 10)
    intstatlist.append(random.randint(1, 6) + 10)
    intstatlist.append(random.randint(1, 6) + 10)
    intstatlist.sort()
    PlayerIG.intel = intstatlist[0]
    PlayerIG.intelbonus = intstatlist[0] - 10
    wisstatlist.append(random.randint(1, 6) + 10)
    wisstatlist.append(random.randint(1, 6) + 10)
    wisstatlist.append(random.randint(1, 6) + 10)
    wisstatlist.sort()
    PlayerIG.wis = wisstatlist[0]
    PlayerIG.wisbonus = wisstatlist[0] - 10
    chastatlist.append(random.randint(1, 6) + 10)
    chastatlist.append(random.randint(1, 6) + 10)
    chastatlist.append(random.randint(1, 6) + 10)
    chastatlist.sort()
    PlayerIG.cha = chastatlist[0]
    PlayerIG.chabonus = chastatlist[0] - 10
    PlayerIG.physique = physiquetraits[random.randint(0, 19)]
    PlayerIG.face = facetraits[random.randint(0, 19)]
    PlayerIG.skin = skintraits[random.randint(0, 19)]
    PlayerIG.hair = hairtraits[random.randint(0, 19)]
    PlayerIG.clothing = clothingtraits[random.randint(0, 19)]
    PlayerIG.virtue = virtuetraits[random.randint(0, 19)]
    PlayerIG.vice = vicetraits[random.randint(0, 19)]
    PlayerIG.speech = speechtraits[random.randint(0, 19)]
    PlayerIG.background = backgroundtraits[random.randint(0, 19)]
    PlayerIG.misfortune = misfortunetraits[random.randint(0, 19)]
    alignmentnum.append(random.randint(1, 20))
    if alignmentnum[0] <= 5:
        PlayerIG.alignment = "Law"
    if (alignmentnum[0] > 5) and (alignmentnum[0] <= 15):
        PlayerIG.alignment = "Neutraility"
    if alignmentnum[0] > 15:
        PlayerIG.alignment = "Chaos"
    armornum.append(random.randint(1, 20))
    if armornum[0] <= 3:
        PlayerIG.currentarmor = "None"
        PlayerIG.armor = 11
    if (armornum[0] > 3) and (armornum[0] <= 14):
        PlayerIG.currentarmor = "Gambeson"
        PlayerIG.armor = 12
        PlayerIG.inventory.update({"Gambeson" : int(1)})
    if (armornum[0] >= 15) and (armornum[0] <= 19):
        PlayerIG.currentarmor = "Brigandine"
        PlayerIG.armor = 13
        PlayerIG.inventory.update({"Brigandine" : int(1)})
    if armornum[0] == 20:
        PlayerIG.currentarmor = "Chain"
        PlayerIG.armor = 14
        PlayerIG.inventory.update({"Chain" : int(1)})
    PlayerIG.inventory.update({dungeongear[random.randint(0, 19)] : int(1)})
    PlayerIG.inventory.update({dungeongear[random.randint(0, 19)] : int(1)})
    PlayerIG.inventory.update({generalgear1[random.randint(0,19)] : int(1)})
    PlayerIG.inventory.update({generalgear2[random.randint(0, 19)] : int(1)})
    PlayerIG.rations = 2
    helmandshieldnum.append(random.randint(1, 20))
    if helmandshieldnum[0] <= 13:
        PlayerIG.helmet = "None"
        PlayerIG.shield = "None"
    if (helmandshieldnum[0] > 13) and (helmandshieldnum[0] <= 16):
        PlayerIG.helmet = "Equipped"
        PlayerIG.shield = "None"
        PlayerIG.inventory.update({"Helmet" : int(1)})
    if (helmandshieldnum[0] > 16) and (helmandshieldnum[0] <= 19):
        PlayerIG.helmet = "None"
        PlayerIG.shield = "Equipped"
        PlayerIG.inventory.update({"Shield" : int(1)})
    if helmandshieldnum[0] == 20:
        PlayerIG.helmet = "Equipped"
        PlayerIG.shield = "Equipped"
        PlayerIG.inventory.update({"Helmet" : int(1)})
        PlayerIG.inventory.update({"Shield" : int(1)})
    PlayerIG.inventoryslots = PlayerIG.con
    PlayerIG.copper = 0
    PlayerIG.level = 1
    PlayerIG.maxhp = random.randint(5, 8)
    PlayerIG.hp = PlayerIG.maxhp
    PlayerIG.animal = "None"
    PlayerIG.animalmaxslots = 0
    PlayerIG.animalslotsfilled = 0
    mainscreen()









def startup():
    print("NOTE: WHEN ASKED FOR A NUMBER ENTER A NUMBER, WHEN ASKED FOR A TRAIT, USE LETTERS. FAILURE TO DO SO WILL CAUSE CRASH.")
    print("Let's make a new character! You will need to roll up you stats and enter them here. Enter your name and click enter to continue.")
    option = input("->")
    global PlayerIG
    PlayerIG = Player(option)
    newchar()

def startuprandom():
    print("NOTE: WHEN ASKED FOR A NUMBER ENTER A NUMBER, WHEN ASKED FOR A TRAIT, USE LETTERS. FAILURE TO DO SO WILL CAUSE CRASH.")
    print("Let's make a new character! You will need to roll up you stats and enter them here. Enter your name and click enter to continue.")
    option = input("->")
    global PlayerIG
    PlayerIG = Player(option)
    randomchar()


def newchar():
    print("What is your strength stat?")
    PlayerIG.strength = int(input("->"))
    print("What is your strength bonus?")
    PlayerIG.strbonus = int(input("->"))
    print("What is your dexterity stat?")
    PlayerIG.dex = int(input("->"))
    print("What is your dexterity bonus?")
    PlayerIG.dexbonus = int(input("->"))
    print("What is your constitution stat?")
    PlayerIG.con = int(input("->"))
    print("What is your constitution bonus?")
    PlayerIG.conbonus = int(input("->"))
    print("What is your intelligence stat?")
    PlayerIG.intel = int(input("->"))
    print("What is your intelligence bonus?")
    PlayerIG.intelbonus = int(input("->"))
    print("What is your wisdom stat?")
    PlayerIG.wis = int(input("->"))
    print("What is your wisdom bonus?")
    PlayerIG.wisbonus = int(input("->"))
    print("What is your charisma stat?")
    PlayerIG.cha = int(input("->"))
    print("What is your charisma bonus?")
    PlayerIG.chabonus = int(input("->"))
    print("What is your level?")
    PlayerIG.level = int(input("->"))
    print("What is your xp?")
    PlayerIG.xp = int(input("->"))
    print("What is your physique")
    PlayerIG.physique = input("->")
    print("What is your face?")
    PlayerIG.face = input("->")
    print("What is your skin?")
    PlayerIG.skin = input("->")
    print("What is your hair?")
    PlayerIG.hair = input("->")
    print("What is your clothing?")
    PlayerIG.clothing = input("->")
    print("What is your virtue?")
    PlayerIG.virtue = input("->")
    print("What is your vice?")
    PlayerIG.vice = input("->")
    print("What is your speech?")
    PlayerIG.speech = input("->")
    print("What is your background?")
    PlayerIG.background = input("->")
    print("What is your misfortune?")
    PlayerIG.misfortune = input("->")
    print("What is your alignment?")
    PlayerIG.alignment = input("->")
    print("What is your armor stat?")
    PlayerIG.armor = int(input("->"))
    print("What is your max HP?")
    PlayerIG.maxhp = int(input("->"))
    print("How many rations do your start with?")
    PlayerIG.rations = int(input("->"))
    print("How many copper do you start with?")
    PlayerIG.copper = int(input("->"))
    print("How many Inventory Slots do you start with?")
    PlayerIG.inventoryslots = int(input("->"))
    print("Do you have an animal? Yes or No.")
    option = input("->")
    print("Do you have an animal? Yes or No.")
    option = input("->")
    if option.lower().strip() == "yes":
        print("Type the animal and click enter.")
        option = input("->")
        PlayerIG.animal = option
        print("How many inventory slots does it have?")
        option = input("->")
        PlayerIG.animalmaxslots = int(option)
    if option.lower().strip() == "no":
        PlayerIG.animal = "None"
        PlayerIG.animalmaxslots = 0
    print("What armor do you have?")
    PlayerIG.currentarmor = input("->")
    print("Do you have a helmet? Type Yes or No.")
    option = input("->")
    if option.lower().strip() == "yes":
        PlayerIG.helmet = "Equipped"
        PlayerIG.inventory.update({"Helmet": 1})
    if option.lower().strip() == "no":
        PlayerIG.helmet = "None"
    else:
        PlayerIG.helmet = "None"
    print("Do you have a shield? Yes or No?")
    option = input("->")
    if option.lower().strip() == "yes":
        PlayerIG.shield = "Equipped"
        PlayerIG.inventory.update({"Shield": 1})
    if option.lower().strip() == "no":
        PlayerIG.shield = "None"
    else:
        PlayerIG.shield = "None"
    PlayerIG.hp = PlayerIG.maxhp
    PlayerIG.inventory = {"Basic Clothes": 0}
    mainscreen()


def mainscreen():
    global PlayerIG
    os.system('cls')
    if PlayerIG.hp <= 0:
        dead()
    if PlayerIG.hp > PlayerIG.maxhp:
        PlayerIG.hp = PlayerIG.maxhp
    if PlayerIG.hp <= 0:
        dead()
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    armor = "Armor: " + str(PlayerIG.armor)
    armorbonus = "Armor Bonus: " + str(PlayerIG.armor - 10)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    commandoptions1 = "1.) Dice Roller and Attack"
    commandoptions2 = "2.) Change HP"
    commandoptions3 = "3.) Change Level and Exp"
    commandoptions4 = "4.) Change Copper Amount"
    commandoptions5 = "5.) Change Stats or Armor Equipped"
    commandoptions6 = "6.) Change Ration Amount"
    commandoptions7 = "7.) View Inventory"
    commandoptions8 = "8.) Change Inventory"
    commandoptions9 = "9.) Save Current State"
    commandoptions10 = "10.) Add Animal"
    print("                               _  ___   _     __      ________ _    _ _____")
    print("                              | |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("                              | ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("                              |  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("                              | . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("                              |_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
    print("\n")
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    physique = "Physique: " + (PlayerIG.physique)
    face = "Face: " + (PlayerIG.face)
    skin = "Skin: " + (PlayerIG.skin)
    hair = "Hair: " + (PlayerIG.hair)
    clothing = "Clothing " + (PlayerIG.clothing)
    virtue = "Virtue: " + (PlayerIG.virtue)
    vice = "Vice: " + (PlayerIG.vice)
    speech = "Speech: " + (PlayerIG.speech)
    background = "Background: " + (PlayerIG.background)
    misfortune = "Misfortune: " + (PlayerIG.misfortune)
    alignment = "Alignment: " + (PlayerIG.alignment)
    features = "   TRAITS"
    exp = "Experience: " + str(PlayerIG.xp)
    helmstatus = "Helmet: " + PlayerIG.helmet
    shieldstatus = "Shield: " + PlayerIG.shield
    armorstatus = "Current Armor: " + PlayerIG.currentarmor
    fixer = "------------"
    animal = "Animal: " + PlayerIG.animal
    animalslots1 = "Animal Slots: " + str(PlayerIG.animalslotsfilled) + "/" + str(PlayerIG.animalmaxslots)
    print(statindicators.center(100, " ") + features.ljust(10, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " ") + physique.rjust(48, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " ") + face.rjust(48, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " ") + skin.rjust(48, " "))
    print(money.ljust(40, " ") + intline.center(20, " ") + hair.rjust(48, " "))
    print(food.ljust(40, " ") + wisline.center(20, " ") + clothing.rjust(48, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " ") + virtue.rjust(48, " "))
    print(armor.ljust(40, " ") + vice.rjust(71, " "))
    print(armorbonus.ljust(40, " ") + speech.rjust(71, " "))
    print(exp.ljust(40, " ") + background.rjust(71, " "))
    print(helmstatus.ljust(40, " ") + misfortune.rjust(71, " "))
    print(shieldstatus.ljust(40, " ") + alignment.rjust(71, " "))
    print(armorstatus.ljust(40, " ") + fixer.rjust(71, " "))
    print(animal.ljust(40, " "))
    print(animalslots1.ljust(40, " "))
    print()
    print("\n")
    print(commandoptions1.center(100, " "))
    print(commandoptions2.center(100, " "))
    print(commandoptions3.center(100, " "))
    print(commandoptions4.center(100, " "))
    print(commandoptions5.center(100, " "))
    print(commandoptions6.center(100, " "))
    print(commandoptions7.center(100, " "))
    print(commandoptions8.center(100, " "))
    print(commandoptions9.center(100, " "))
    print(commandoptions10.center(100, " "))
    print("Select command option by selecting a number.")
    option = input("->")
    if option == "1":
        attack()
    if option == "2":
        changehp()
    if option == "3":
        changelevel()
    if option == "4":
        changecopper()
    if option == "5":
        changestats()
    if option == "6":
        changeration()
    if option == "7":
        viewinventory()
    if option == "8":
        changeinventory()
    if option == "9":
        f = open('savefile', 'wb')
        pickle.dump(PlayerIG, f)
        print("\n Game has been saved! And so has your soul!\n")
        f.close()
        input("->")
        mainscreen()
    if option.strip() == "10":
        changeanimal()
    else:
        mainscreen()

def changeanimal():
    print("Add animal? Or Delete current animal?")
    print("1.) Add")
    print("2.) Delete")
    option = input("->")
    if option.strip() == "1":
        print("Type the name of the animal. CLick enter.")
        option = input("->")
        PlayerIG.animal = option
        print("How many slots does it have?")
        option2 = input("->")
        PlayerIG.animalmaxslots = int(option2)
        print("Animal added!")
        input("->")
        mainscreen()
    if option.strip() == "2":
        print("Your active animal is a " + PlayerIG.animal)
        print("Would you like to delete it? Type Yes or No")
        option = input("->")
        if option.strip.lower() == "yes":
            PlayerIG.animal = "None"
            PlayerIG.animalslotsfilled = 0
            PlayerIG.animalmaxslots = 0
        if option.lower().strip() == "no":
            changeanimal()
        else:
            changeanimal()
    else:
        changeanimal()





def viewinventory():
    print("Which inventory?")
    print("1.) Personal Inventory")
    print("2.) Animal Inventory")
    option = input("->")
    if option == "1":
        inventorydisplay = PlayerIG.inventory
        print("You open your bag and check your inventory. Press b to return.")
        print("Item is on the left column, number of Inventory Slots is on the right")
        print("\n")
        for key, value in inventorydisplay.items():
            print(key, " : ", value)
        option = input("->")
        if option.strip().lower() == "b":
            mainscreen()
        else:
            viewinventory()
    if option == "2":
        animalslots = PlayerIG.animalinventory
        print("You look in the pack on your animal and find...")
        print("\n")
        for key, value in animalslots.items():
            print(key, " : ", value)
        option = input("->")
        if option.strip().lower() == "b":
            mainscreen()
        else:
            viewinventory()




def changeinventory():
    slotsremaining = PlayerIG.inventoryslots - sum(PlayerIG.inventory.values())
    if PlayerIG.animal != "None":
        animalslotsremaining = PlayerIG.animalmaxslots - PlayerIG.animalslotsfilled
    inventorydisplay = PlayerIG.inventory
    animalslots = PlayerIG.animalinventory
    print("Are you removing or adding something? Press b and enter to return.")
    print("1.) Removing")
    print("2.) Adding")
    option = input("->")
    if option.strip() == "1":
        print("From where?")
        print("1.) Personal Inventory")
        print("2.) Animal Inventory")
        option = input("->")
        if option.strip() == "1":
            print("Animal Inventory")
            print("Item:           Slots")
            for key, value in inventorydisplay.items():
                print(key, " : ", value)
            print("Type the item you wish to remove.")
            option = input("->")
            if option in PlayerIG.inventory:
                    PlayerIG.inventory.pop(option)
                    print("Item Removed!")
                    input("->")
            else:
                print("Item not in inventory, try again.")
                changeinventory()
        if option.strip() == "2":
            if PlayerIG.animal == "None":
                print("No animal!")
                mainscreen()
            print("Animal Inventory")
            print("Item:            Slots")
        for key, value in animalslots.items():
            print(key, " : ", value)
        print("Type the item you wish to remove")
        option = input("->")
        if option in PlayerIG.animalinventory:
            PlayerIG.animalinventory.pop(option)
            print("Item Removed!")
            input("->")
    if option == "2":
        print("From where?")
        print("1.) Personal Inventory")
        print("2.) Animal Inventory")
        option = input("->")
        if option == "1":
            print("Personal Inventory")
            print("Item:           Slots")
            for key, value in inventorydisplay.items():
                print(key, " : ", value)
            print("Type the item you wish to add.")
            option = input("->")
            print("Type the number of slots it takes up.")
            option2 = input("->")
            if int(option2) > slotsremaining:
                print("Not enough space! Remove items and try again!")
            else:
                PlayerIG.inventory.update({str(option): int(option2)})
                print("Item Added!")
                input("->")
                mainscreen()
        if option.strip().lower() == "b":
            mainscreen()
        if option == "2":
            if PlayerIG.animal == "None":
                print("No animal!")
                input("->")
                mainscreen()
            print("Animal Inventory")
            print("Item:          Slots")
            for key, value in animalslots.items():
                print(key, " : ", value)
            print("Type the Item you wish to add.")
            option = input("->")
            print("Type the number of slots it takes up.")
            option2 = input("->")
            if int(option2) > animalslotsremaining:
                print("Not enough space! Remove items and try again.")
            else:
                PlayerIG.animalinventory.update({str(option): int(option2)})
                PlayerIG.animalslotsfilled = int(option2)
                print("Item Added!")
                input("->")
                mainscreen()
        else:
            changeinventory()
    if option.strip().lower() == "b":
        mainscreen()





def changeration():
    print("What would you like to do? Press b to return")
    print("1.) Consume ration")
    print("2.) Add rations")
    option = input("->")
    if option.strip() == "1":
        PlayerIG.rations -= 1
        mainscreen()
    if option.strip() == "2":
        print("How many? Enter a number to continue.")
        option = input("->")
        if option.strip().lower() == "b":
            changeration()
        else:
            PlayerIG.rations += int(option)
            mainscreen()







def changestats():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    helmstatus = "Helmet: " + PlayerIG.helmet
    shieldstatus = "Shield: " + PlayerIG.shield
    armorstatus = "Current Armor: " + PlayerIG.currentarmor
    fixer = "------------"
    armor = "Armor: " + str(PlayerIG.armor)
    armorbonus = "Armor Bonus: " + str(PlayerIG.armor - 10)
    face = "Face: " + (PlayerIG.face)
    skin = "Skin: " + (PlayerIG.skin)
    hair = "Hair: " + (PlayerIG.hair)
    clothing = "Clothing " + (PlayerIG.clothing)
    virtue = "Virtue: " + (PlayerIG.virtue)
    vice = "Vice: " + (PlayerIG.vice)
    speech = "Speech: " + (PlayerIG.speech)
    background = "Background: " + (PlayerIG.background)
    misfortune = "Misfortune: " + (PlayerIG.misfortune)
    alignment = "Alignment: " + (PlayerIG.alignment)
    features = "   TRAITS"
    exp = "Experience: " + str(PlayerIG.xp)
    helmstatus = "Helmet: " + PlayerIG.helmet
    shieldstatus = "Shield: " + PlayerIG.shield
    armorstatus = "Current Armor: " + PlayerIG.currentarmor
    fixer = "------------"
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print(armor.ljust(40, " "))
    print(armorbonus.ljust(40, " "))
    print(exp.ljust(40, " "))
    print(helmstatus.ljust(40, " "))
    print(shieldstatus.ljust(40, " "))
    print(armorstatus.ljust(40, " "))
    print("Which stat would you like to change? To change your equipped armor, press 8. Press b to return")
    print("1.) Strength")
    print("2.) Dexterity")
    print("3.) Constitution")
    print("4.) Intelligence")
    print("5.) Wisdom")
    print("6.) Charisma")
    print("7.) Armor")
    print("8.) Change Equipment")
    option = input("->")
    if option.strip() == "1":
        print("What is your new strength stat?")
        option2 = int(input("->"))
        PlayerIG.strength = option2
        PlayerIG.strbonus = PlayerIG.strength - 10
        mainscreen()
    if option.strip() == "2":
        print("What is your new dexterity stat?")
        option = int(input("->"))
        PlayerIG.dex = option
        PlayerIG.dexbonus = PlayerIG.dex - 10
        mainscreen()
    if option.strip() == "3":
        print("What is your new constitution stat?")
        option = int(input("->"))
        PlayerIG.con = option
        PlayerIG.conbonus = PlayerIG.con - 10
        mainscreen()
    if option.strip() == "4":
        print("What is your new intelligence stat?")
        option = int(input("->"))
        PlayerIG.intel = option
        PlayerIG.intelbonus = PlayerIG.intel - 10
        mainscreen()
    if option.strip() == "5":
        print("What is your new wisdom stat?")
        option = int(input("->"))
        PlayerIG.wis = option
        PlayerIG.wisbonus = PlayerIG.wis - 10
        mainscreen()
    if option.strip() == "6":
        print("What is your new charisma stat?")
        option = int(input("->"))
        PlayerIG.cha = option
        PlayerIG.chabonus = PlayerIG.cha - 10
        mainscreen()
    if option.strip() == "7":
        print("What is your armor stat?")
        option = int(input("->"))
        PlayerIG.armor = option
        mainscreen()
    if option.strip().lower() == "b":
        mainscreen()
    if option.strip() == "8":
        print("What armor would you like to change?")
        print("1.) Main Armor")
        print("2.) Equip Helmet")
        print("3.) Unequip Helmet")
        print("4.) Equip Shield")
        print("5.) Unequip Shield")
        option = input("->")
        if option == "1":
            print("What armor would you like to change to? Type None to unequip main armor. (DON'T FORGET TO CHANGE YOUR ARMOR STAT)")
            option = input("->")
            if option in PlayerIG.inventory or option == "None":
                PlayerIG.currentarmor = option
                mainscreen()
            else:
                print("You don't have that armor! Press enter to continue!")
                input("->")
                changestats()
        if option == "2":
            if PlayerIG.helmet == "Unequipped" or PlayerIG.helmet == "None" and {"Helmet": 1} in PlayerIG.inventory:
                PlayerIG.helmet = "Equipped"
                mainscreen()
            else:
                print("Invalid choice. Click enter to continue")
                input("->")
                changestats()
        if option == "3":
            if PlayerIG.helmet == "Equipped":
                PlayerIG.helmet = "Unequipped"
                mainscreen()
        if option == "4":
            if PlayerIG.shield == "Unequipped" or PlayerIG.shield == "None" and {"Shield": 1} in PlayerIG.inventory:
                PlayerIG.shield = "Equipped"
                mainscreen()
            else:
                print("Invalid. Click enter to continue.")
                changestats()
        if option == "5":
            if PlayerIG.shield == "Equipped":
                PlayerIG.shield = "Unequipped"
                mainscreen()

    else:
        print("Invalid response, try again.")
        changestats()



def changecopper():
    print("Increase or decreasing copper? Press b to return")
    print("1.) Increase")
    print("2.) Decrease")
    option = input("->")
    if option.strip() == "1":
        print("By how much?")
        option2 = int(input("->"))
        PlayerIG.copper += option2
        mainscreen()
    if option.strip() == "2":
        print("By how much?")
        option3 = int(input("->"))
        PlayerIG.copper -= option3
        mainscreen()
    if option.lower().strip() == "b":
        mainscreen()
    else:
        print("Invalid choice, try again.")
        changecopper()




def changelevel():
    print("Change Level or XP?")
    print("1.) Level")
    print("2.) XP")
    option = input("->")
    if option == "1":
        print("Level Up or Level Down? Press b to return")
        print("1.) Level Up")
        print("2.) Level Down")
        option = input("->")
        if option.strip() == "1":
            PlayerIG.level += 1
            mainscreen()
        if option.strip() == "2":
            PlayerIG.level -= 1
        mainscreen()
        if option.lower().strip() == "b":
            mainscreen()
        else:
            print("Invalid choice, try again.")
            changelevel()
    if option == "2":
        print("What is your current exp?")
        option = int(input("->"))
        Player.xp = option
        mainscreen()
    else:
        print("Invalid choice, try again.")
        changelevel()


def savegame():
    with open('savefile', 'wb') as f:
        pickle.dump(PlayerIG, f)
        print("\n Game has been saved! And so has your soul!\n")
        input("->")
        mainscreen()



def load():
    if os.path.exists("savefile") == True:
        with open("savefile", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
            print("Loaded save state...your journey continues!")
            input("->")
            mainscreen()


def changehp():
    print("Max HP or Current HP? Select b and enter to go back.")
    print("1.) Max HP")
    print("2.) Current HP")
    option1 = input("->")
    if option1.strip() == "1":
        print("What is your new max hp? (Enter a number)")
        option = int(input("->"))
        PlayerIG.maxhp = option
        print("Your new max HP has been saved!")
        mainscreen()
    if option1.strip() == "2":
        print("Increase or Decrease?")
        print("1.) Increase")
        print("2.) Decrease")
        option2 = input("->")
        if option2.strip() == "1":
            print("By how much? (Enter a number)")
            option3 = int(input("->"))
            PlayerIG.hp += option3
            print("Your HP has increased")
            input("->")
            mainscreen()
        if option2.strip() == "2":
            print("By how much? (Enter a number)")
            option4 = int(input("->"))
            PlayerIG.hp -= option4
            print("Your HP has decreased")
            input("->")
            mainscreen()
    if option1.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid option try again.")
        changehp()


def attack():
    start()

def start():
    print("Hello! Welcome to the KnaveUI dice roller! Which dice would you like to roll? (Press b to return)")
    print("1.) D4")
    print("2.) D6")
    print("3.) D8")
    print("4.) D10")
    print("5.) D12")
    print("6.) D20")
    print("7.) D100")
    option = input("-> ")
    if option.strip() == "1":
        dicerolld4()
    elif option.strip() == "2":
        dicerolld6()
    elif option.strip() == "3":
        dicerolld8()
    elif option.strip() == "4":
        dicerolld10()
    elif option.strip() == "5":
        dicerolld12()
    elif option.strip() == "6":
        dicerolld20()
    elif option.strip() == "7":
        dicerolld100()
    elif option.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid Option")
        start()


def dicerolld10():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d10 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 10))

    dicerolld10()


def dicerolld20():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d20 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 20))

    dicerolld20()


def dicerolld4():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d4 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 4))

    dicerolld4()


def dicerolld6():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d6 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 6))

    dicerolld6()


def dicerolld8():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d8 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 8))

    dicerolld8()


def dicerolld12():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d12 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 12))

    dicerolld12()



def dicerolld100():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d100 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 100))

    dicerolld100()

















def dead():
    print("You dead sucka! Time to roll up a new one! Click Enter to restart")
    input("->")
    PlayerIG.hp = PlayerIG.maxhp
    mainscreen()




startmenu()
