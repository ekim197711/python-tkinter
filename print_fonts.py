import tkinter as tk
import tkFont
from tkinter import font

def list_fonts():
    font.families()
    for f in list(font.families()):
        print("Font: ", f)


root = tk.Tk()
btn = tk.Button(root, text="List families", command=list_fonts)
btn.grid(row=0, column=0)
root.mainloop()
