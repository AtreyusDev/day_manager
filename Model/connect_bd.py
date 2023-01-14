# This class contains all querys for the app database with PostgreSQL.

import psycopg2
import datetime

class DAO(): #DATA ACCES OBJECT
    def __init__(self):
        # Here we initialize the class.
        # The connection is covered by a try-catch block to check the connection status.
        try: 
            # This var allows the connection with the database...
            self.connect = psycopg2.connect(
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
            print('Connection succes!')
            # This var open the cursor to perform database operations...
            self.cursor = self.connect.cursor() 

        except Exception as e: # In case of error, print the reason.
            print(f'Oops! We had a problem with the DataBase, this is the reason: {e}')

    def createTable(self): # This function CREATE the table.
        self.cursor.execute('CREATE TABLE if NOT EXISTS to_do_list (task VARCHAR, date DATE);')

    def viewTable(self): # This function does a SELECT query from the table.
        self.cursor.execute('SELECT * FROM to_do_list')
        columns = self.cursor.fetchall()
        print(columns)

    def insert_into_table(self): # This function does a INSERT query in to the table.
        task = input('Insert the task as you want to write in the database: ')
        self.cursor.execute('INSERT INTO to_do_list (task, date) VALUES (%s, %s)', (task, datetime.date.today()))
        self.connect.commit()
    
choice = 0

instance = DAO()
instance.createTable()


while choice != 3:

    print("""
    ¿What do you want to do?
    1. View values
    2. Insert values
    3. Finish
    """)

    choice = int(input('Write the number (1/2/3) and press Enter: '))

    if choice == 1:
        instance.viewTable()
    elif choice == 2:
        instance.insert_into_table()
    elif choice == 3:
        print('Good day!')
        exit()
    else:
        print('We don´t found this option, please check your input and try again...')


    