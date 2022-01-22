import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
def my_application():
    root = Tk()
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.grid(columnspan=12,rowspan=3)
    fontface = "Arial"
    # frm = ttk.Frame(root, padding=10)
    # frm.grid()
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    image = ImageTk.PhotoImage(Image.open("images/rabbit1.jpg"))
    logo_label = tk.Label(root, image=image)
    # logo_label.
    logo_label.grid(column=4,columnspan=4,row=1)
    header_label = tk.Label(root, text="This is my photo application", font=fontface)
    header_label.grid(column=2,columnspan=4, row=0)


    # canvas.create_image(10,10, anchor=NW, image=image)
    root.mainloop()


if __name__ == "__main__":
    my_application()