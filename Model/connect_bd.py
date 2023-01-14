# This class contains all querys for the app database with PostgreSQL.

import psycopg2
import datetime

class DAO(): #DATA ACCES OBJECT
    def __init__(self):
        # Here we initialize the class.
        # The connection is covered by a try-catch block to check the connection status.
        try: 
            self.connect = psycopg2.connect( # This var allows the connection with the database...
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
            print('Connection succes!')
            self.cursor = self.connect.cursor() # This var open the cursor to perform database operations...
            self.create_table() # Here, the class calls this function to create a table in the database.
        except Exception as e: # In case of error, print the reason.
            print(f'Oops! We had a problem with the DataBase. This is the reason: {e}')

    def create_table(self): # This function CREATE the table. 
        try: # The creation is covered by a try-catch block to check the creation status.
            print('Creating table...')
            self.cursor.execute('CREATE TABLE if NOT EXISTS to_do_list (id SERIAL PRIMARY KEY, task VARCHAR, date DATE);')
            # This table contains three columns: Id, Task and Date.
            print('Table created succesfull!')
        except Exception as e: # In case of error, print the reason.
            print(f'Oops! We had a problem creating the table. This is the reason: {e}')

    def view_table(self): # This function does a SELECT query from the table.
        self.cursor.execute('SELECT * FROM to_do_list')
        columns = self.cursor.fetchall() # This var contains all the regist of the table.
        for row in columns:
            print(f"""
            Id: {row[0]}
            Task: {row[1]}
            Date: {row[2]}
            """) # Print the regists of the table.

    def edit_for_table(self): # This function does a UPDATE query in to the table.
        id_task = input('Insert the task id to edit that regist: ')
        task = input('Write the new value for the task: ')
        self.cursor.execute('UPDATE to_do_list SET task = %s WHERE id = %s'  , (task, id_task))
        self.connect.commit()
        print('Regist edit done!')

    def insert_into_table(self): # This function does a INSERT query in to the table.
        task = input('Write the task that you want to insert in the database: ')
        try:
            self.cursor.execute('INSERT INTO to_do_list (task, date) VALUES (%s, %s)', (task, datetime.date.today()))
            self.connect.commit()
            print('Regist insert done!')
        except Exception as e:
            print(f'We cannot insert this regist. Reason: {e}')

    def delete_from_table(self):
        id_task = input('Insert the task id to delete that regist: ')
        try:
            self.cursor.execute('DELETE FROM to_do_list WHERE id = %s', (id_task))
            self.connect.commit()
            print('Regist delete done!')
        except Exception as e:
            print(f'We cannot delete this regist. Reason: {e}')
    
choice = 0

instance = DAO()
instance.create_table()


while choice != 5:

    print("""
    ¿What do you want to do?
    1. View values
    2. Insert values
    3. Delete values
    4. Edit values
    5. Finish
    """)

    choice = int(input('Write the number (1/2/3/4/5) and press Enter: '))

    if choice == 1:
        instance.view_table()
    elif choice == 2:
        instance.insert_into_table()
    elif choice == 3:
        instance.delete_from_table()
    elif choice == 4:
        instance.edit_for_table()
    elif choice == 5:
        print('Good day!')
        exit()
    else:
        print('We don´t found this option, please check your input and try again...')


    