import random
import sys

def hello():
    name=str(input("what's thy name?\n "))
    print("Hello " + str(name) + "!")
    return

def choices():
    choice=str(input("Would you like a random weapon? y/n: "))
    y=print(random.choice(weapons) + " of " + random.choice(conditions))
    n=print("Very well")
    if choice is y:
        print(y)
    else:
        if choice is n:
            print(n)
                  
        

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
    print(const, strength, dex, intel, wisd, charisma)

hello()
choices()
stats()
