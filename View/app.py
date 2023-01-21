from Controller.controller import Worker # Import the controller to allow the functionality

import tkinter as tk    # Tkinter is used for the complete creation of the graphic interface.
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image # This module is for use Images.

class Screen():     # This class contains all the methods for the creation of the graphic interface.
    def __init__(self):
        self._root = tk.Tk()    # This is the root.

        # CENTER THE ROOT ON THE SCREEN

        # We define 2 variables that will tell the root where is the center of the screen.
        width_total = self._root.winfo_screenwidth()
        height_total = self._root.winfo_screenheight()

        # This is the geometry that we want for the root.
        width_root = 800
        height_root = 500

        # Here, we calculate the position on the screen for the root.
        pwidth = round(width_total / 2 - width_root / 2)
        pheight = round((height_total / 2 - height_root / 2) - 20)

        # Finally, we set the geometry:
        self._root.geometry(f'{width_root}x{height_root}+{pwidth}+{pheight}')

        self._root.resizable(0,0) # This is to forbid the user changes the geometry.
        self._root.title('TaskLab')
        self._root.config(bg='#312c27')
        self._icon = ImageTk.PhotoImage(Image.open('View/images/icono_day_manager.png')) # This is the icon of the app.
        self._root.iconphoto(False, self._icon)
        self.screen_widgets() # Here, the class call the 'screen_widgets' method for initialize the widgets.
        self.initial_view() # Here, the class read the database and insert the data on the Treeview.
                                   
        self._root.mainloop() # Here, the class open the root and shows it on the screen.

    def screen_widgets(self): # This function creates the widgets and positions them on the root.
        # TITLE
        _tittle_task = Label(self._root, text='Welcome to TaskLab', bg='#1c1917', fg='#ffffff', width='500', font='Bahnschrift')
        _tittle_task.pack(side=TOP)

        # FRAME
        # For the tree
        _tasks_area = Frame(self._root, bd=10, bg='#443b31', relief=GROOVE, padx=3, pady=3)
        _tasks_area.pack(side=TOP, fill=BOTH)

        # For the buttons
        buttons_area = Frame(self._root, bd=10, bg='#443b31', relief=GROOVE, padx=30, pady=30)
        buttons_area.pack(side=BOTTOM, fill=BOTH)

        # TREE
        self._tree = ttk.Treeview(_tasks_area, columns=('Task','Date','Time'), height=13)

        # Here, the columns are designed.

        self._tree.column('#0', width= 80, anchor=CENTER)
        self._tree.column('Task', width= 320, anchor= CENTER)
        self._tree.column('Date', width= 170, anchor=CENTER)
        self._tree.column('Time', width= 140, anchor=CENTER, stretch=True)

        # Here, the head of the columns are designed.

        self._tree.heading('#0', text='Id', anchor=CENTER)
        self._tree.heading('Task', text='Task', anchor=CENTER)
        self._tree.heading('Date', text='Date', anchor=CENTER)
        self._tree.heading('Time', text='Time', anchor=CENTER)

        self._tree.pack(padx=20, pady=30, side=LEFT)

        # Here, we define the scrollbar to scroll the treeview.
        self.scrollbar = Scrollbar(_tasks_area, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self._tree.config(yscrollcommand=self.scrollbar.set) # Set the scroll command.
        self.scrollbar.config(command=self._tree.yview)

        # BUTTONS

        _button_add = Button(buttons_area, bd=4, height=1, width=10, text='Add Task', justify=CENTER,
        relief=RAISED, font=('Bahnschrift', 10), command= lambda : self.send_data('add'))
        _button_add.grid(row=0, column=0) 

        _button_edit = Button(buttons_area, bd=4, height=1, width=10, text='Edit Task', justify=CENTER,
        relief=RAISED, font=('Bahnschrift', 10), command= lambda : self.send_data('edit'))
        _button_edit.grid(row=0, column=1, padx=15)

        _button_delete = Button(buttons_area, bd=4, height=1, width=10, text='Delete Task', justify=CENTER,
        relief=RAISED, font=('Bahnschrift', 10), command= lambda : self.send_data('delete'))
        _button_delete.grid(row=0, column=2)

        _button_delete_all = Button(buttons_area, bd=4, height=1, width=10, text='Delete All', justify=CENTER,
        relief=RAISED, font=('Bahnschrift', 10), command= lambda : self.send_data('delete_all'))
        _button_delete_all.grid(row=0, column=3, padx=15)

        # ENTRYS

        # Task

        self._entry_task = Entry(buttons_area, width=20, font='Bahnschrift')
        self._entry_task.place(x=500, y=-25)

        # Date

        days = []   # Vars
        months = []
        years = []

        for day in range(1, 32):
            days.append(day)
            day += 1

        for month in range(1, 13):
            months.append(month)
            month += 1
        
        for year in range(2023, 2051):
            years.append(year)
            year += 1

        self._list_day = ttk.Combobox(buttons_area, values=days, state='readonly', width=6)
        self._list_day.place(x=500, y=1) # Day

        self._list_month = ttk.Combobox(buttons_area, values=months, state='readonly', width=6)
        self._list_month.place(x=563, y=1) # Month

        self._list_year = ttk.Combobox(buttons_area, values=years, state='readonly', width=6)
        self._list_year.place(x=626, y=1) # Year

        # Time

        hours = [] # Vars
        minutes = []

        for hour in range(1, 25):
            hours.append(hour)
            hour += 1

        for minute in range(0, 61):
            minutes.append(minute)
            minute += 1

        self._list_hour = ttk.Combobox(buttons_area, values=hours, state='readonly', width=4)
        self._list_hour.place(x=540, y=26) # Hour

        _label_for_time = Label(buttons_area, text=':', font='Bahnschrift', bg='#443b31', fg='white')
        _label_for_time.place(x=589, y=22)  # Label ':'

        self._list_minute = ttk.Combobox(buttons_area, values=minutes, state='readonly', width=4)
        self._list_minute.place(x=600, y=26) # Minutes

        # LABELS FOR ENTRYS

        self._label_task = Label(buttons_area, font='Bahnschrift', text='Task:', width=8)
        self._label_task.place(x=420, y=-26) 

        self._label_date = Label(buttons_area, font='Bahnschrift', text='Date:', width=8)
        self._label_date.place(x=420, y=0)

        self._label_time = Label(buttons_area, font='Bahnschrift', text='Time:', width=8)
        self._label_time.place(x=420, y=26)

    def initial_view(self): # This function initializes the Controller.
        Worker(self._tree, END) # This line sends the data for insert the registers on the treeview when it is opened.

    def send_data(self, order): # This function is responsible for sending all the data to the Controller.
        Worker.make_order(self, self._tree, END, order, self._entry_task, self._list_day, self._list_month,
        self._list_year, self._list_hour, self._list_minute)

        # As you can see, the function send_data() receives "order" as a parameter. It is for know
        # wich task the Controller going to do.



