import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
def my_application():
    root = Tk()
    root.title("TKInter demo hello world")
    # canvas = tk.Canvas(root, width=800, height=600)
    # canvas.grid(columnspan=3,rowspan=3)
    fontface = "Arial"
    fontsize = 40

    frm = ttk.Frame(root, padding=10)
    frm.grid(column=1,row=1)

    image = ImageTk.PhotoImage(Image.open("images/rabbit1.jpg"))
    logo_label = tk.Label(frm, image=image)
    logo_label.pack(side=LEFT)

    header_label = tk.Label(root, text="This is my photo application", font=(fontface, fontsize))
    header_label.grid(column=0, columnspan=3, row=0,sticky=E)

    root.mainloop()


if __name__ == "__main__":
    my_application()