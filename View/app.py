import tkinter as tk
from tkinter import *
from tkinter import ttk

# THIS LINE IS FOR IMPORT PILLOW = from PIL import ImageTk, Image

class Screen():
    def __init__(self):
        self.root = tk.Tk() 
        self.root.geometry('800x500')
        self.root.resizable(0,0)
        self.root.title('TaskLab')
        self.root.config(bg='#4287f5')
        # THIS LINE IS FOR THE ICON OF THE ROOT = self.icon = ImageTk.PhotoImage(Image.open('ruta_de_imagen'))
        # THIS LINE IS FOR INSERT THE ICON IN THE ROOT = self.root.iconphoto(False, self.icon)
        self.screen_widgets()
        self.root.mainloop()

    def screen_widgets(self):
        tittle_task = Label(self.root, text='Welcome to TaskLab', bg='#4287f5', width='500').pack(side=TOP)
        tasks_area = Frame(self.root, bd=10, bg='#87fffd', relief=GROOVE, padx=3, pady=3)
        tasks_area.pack(side=TOP, fill=BOTH)

        self.tree = ttk.Treeview(tasks_area, columns=('Task','Date','Time'), height=15)

        self.tree.column('#0', width= 80)
        self.tree.column('Task', width= 320, anchor= CENTER)
        self.tree.column('Date', width= 170, anchor=CENTER)
        self.tree.column('Time', width= 140, anchor=CENTER)

        self.tree.heading('#0', text='Id', anchor=CENTER)
        self.tree.heading('Task', text='Task', anchor=CENTER)
        self.tree.heading('Date', text='Date', anchor=CENTER)
        self.tree.heading('Time', text='Time', anchor=CENTER)
        self.tree.pack(padx=30, pady=30, fill=BOTH)


Screen()


