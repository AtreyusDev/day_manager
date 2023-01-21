import tkinter as tk # Import tkinter for allow the changes on the Widgets.
from tkinter import *
from tkinter import ttk, messagebox
from Model.connect_bd import DAO # Here, we import the Data Acces Object. It contains the database.

class Worker(): # This is the Controller of the app.                                                  
    def __init__(self, tree, position):
        DAO() # Initialize DAO.
        # Insert all the registers of the table when the root is opened.
        _columns = DAO.view_table(self)
        for row in _columns:
            tree.insert('', position, text=row[0], values=(row[1], row[2], row[3]))
    
    def make_order(self, tree, position, order, entry_task, day, month, year, hour, minute):
        # Get entry values. 

        _task_value = entry_task.get()
        _day_value = day.get()
        _month_value = month.get()
        _year_value = year.get()
        _hour_value = hour.get()
        _minute_value = minute.get()

        if order == 'add': # Add register.
            if len(_task_value) > 0 and len(_day_value) > 0 and len(_month_value) > 0 and len(_year_value) > 0 and len(_hour_value) > 0 and len(_minute_value) > 0:
                list_of_rows = tree.get_children()
                for _register in list_of_rows:
                    tree.delete(_register)

                columns = DAO.insert_into_table(self, _task_value,
                f'{_day_value}/{_month_value}/{_year_value}',
                f'{_hour_value}:{_minute_value}')

                for row in columns:
                    tree.insert('', position, text=row[0], values=(row[1], row[2], row[3]))    
            else:
                messagebox.showerror('Error','Entrys cannot be empty.')
        
        elif order == 'edit': # Edit register.
            
                _selection = tree.focus()
                _register = tree.item(_selection, 'text')
                print(_selection.get_children())
                if _register == '':
                    messagebox.showinfo('Error','You must to select the register that you want to edit.')
                else:
                    if len(_task_value) > 0 and len(_day_value) > 0 and len(_month_value) > 0 and len(_year_value) > 0 and len(_hour_value) > 0 and len(_minute_value) > 0:
                        columns = DAO.edit_for_table(self, _register, _task_value, f'{_year_value}-{_month_value}-{_day_value}', f'{_hour_value}:{_minute_value}')
                        list_of_rows = tree.get_children()

                        for _register in list_of_rows:
                            tree.delete(_register)

                        for row in columns:
                            tree.insert('', position, text=row[0], values=(row[1], row[2], row[3]))  
                    else:
                        messagebox.showerror('Error','Entrys cannot be empty.')

        elif order == 'delete': # Delete register.
            _selection = tree.focus()
            _register = tree.item(_selection, 'text')
            if _register == '':
                messagebox.showinfo('Error','You must to select the register that you want to delete.')
            else:
                columns = DAO.delete_from_table(self, _register)

                list_of_rows = tree.get_children()
                for _register in list_of_rows:
                    tree.delete(_register)

                for row in columns:
                    tree.insert('', position, text=row[0], values=(row[1], row[2], row[3])) 

        elif order == 'delete_all': # Delete all registers.
            _register = DAO.view_table(self)
            _advertise_box = messagebox.askyesno('Alert','¿Are you sure you want to delete all registers?')
            if _advertise_box:
                if len(_register) > 0:
                    columns = DAO.delete_all(self)
                    list_of_rows = tree.get_children()
                    for _register in list_of_rows:
                        tree.delete(_register)
                else:
                    messagebox.showerror('Error','There is no registers.')
            else:
                pass
                

          
        
    
