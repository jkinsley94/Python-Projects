import random as ran
import tkinter as tk
from tkinter import filedialog, Text
import os


#GUI goes here
root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="gray")
canvas.pack()

frame = tk.Frame(root, bg="white")

frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


#classes, weapons go here
h_Weapons = []
l_Weapons = []

#input here
