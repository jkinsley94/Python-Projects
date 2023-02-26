import random as rnd
import webbrowser as web
from random import randint

#the choices available put in a array.
rps=['Rock', 'Paper', 'Scissors']

#this is how we call our random function for the computer
computer = rps[randint(0,2)]

#we set player to false
player= False

player = input("rock, paper, scissors?")
if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose! " + computer + " covers " + player)
    else:
        print("You win! " + player + " smashes " + computer)
elif player == "Paper":
    if computer == "Scissors":
        print("You lose! " + computer + "cuts" + player)
    else:
        print("You win! " + player + " covers " + computer)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose! " + computer + " crushes " + player)
    else:
        print("You win! " + player + " cuts " + computer)
else:
    print("that's not valid. Try again. Ensure you're spelling and using capitals.")

player = False

computer =rps[randint(0,2)]
    