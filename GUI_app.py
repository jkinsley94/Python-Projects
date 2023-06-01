import tkinter
from tkinter import *
from tkinter import ttk


root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()
    return

myButton = Button(root, text="click me!", command=myClick)
myButton.pack()

root.mainloop

print("ebans")