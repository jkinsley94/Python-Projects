import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

root = tk.Tk()
frm=ttk.Root(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello world!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)