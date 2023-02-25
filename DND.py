import random
import sys

def hello():
    name=str(input("what's thy name?\n "))
    print("Hello " + str(name) + "!")
    return



def choices():
    choice=(input("Would you like a random weapon? y/n: "))
    if choice == "y":
        print(random.choice(weapons) + " of " + random.choice(conditions))
        
        
    else:
        if choice == "n":
            print("Very well.")

def races():
    choice=input("Would you like a random race? y/n: ")
    if choice == "y":
        print(random.choice(race) + "is your character race.")

    else:
        if choice == "n":
            print("Very well.")    
            
race=[
    'Dwarf', 'Dragonborn', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Orc', 'Half-Orc', 'Human', 'Tiefling'
]

weapons=[
    'Bow', 'Axe', 'Greatsword', 'Javelin', 'Dagger', 'Scimitar', 'Rapier', 'Quarterstaff'
]


conditions=[
    'ice', 'earth', 'wind', 'fire',  'sickness' 'bleeding', 'blinding', 'fear', 'exhaustion', 'constipation', 'poison', 'madness', ''
]

def stats():
    const=random.randint(5,20)
    strength=random.randint(5,20)
    dex=random.randint(5,20)
    intel=random.randint(5,20)
    wisd=random.randint(5,20)
    charisma=random.randint(5,20)
    print("here are your stats!")
    print(const, strength, dex, intel, wisd, charisma)




hello()
choices()
races()
stats()
