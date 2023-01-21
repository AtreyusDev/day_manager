# NOTE: This database is hosted in a local server. For that, nobody except the creator of this app can
#       work whit the database.
#       If you are interested in use this code with another database, go on! I hope it works :D ...

# This class contains all the querys for the app database with PostgreSQL.

import psycopg2 # Library that contains the functions for work with PostgreSQL
import datetime # Library that contains the functions for work with dates and times.

class DAO(): #DATA ACCES OBJECT
    def __init__(self):
        # Here we initialize the class.
        # The connection is covered by a try-catch block for check the connection status.
        try: 
            self.connect = psycopg2.connect( # This variable allows the connection with the database...
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
            print('Connection succes!')
            self.cursor = self.connect.cursor() # This variable open the cursor to perform database operations...
            self.create_table() # Here, the class calls this function to create a table in the database.

        except Exception as e: # In case of error, print the reason.
            print(f'Oops! We had a problem with the DataBase. This is the reason: {e}')

    def create_table(self): # This function CREATE the table. 
        try: # The creation is covered by a try-catch block to check the creation status.
            print('Creating table...')
            self.cursor.execute('CREATE TABLE if NOT EXISTS to_do_list (id SERIAL PRIMARY KEY, task VARCHAR(200), date DATE, hour TIME);')
            # This table contains three columns: Id, Task and Date.
            print('Table created succesfull!')
            
        except Exception as e: # In case of error, print the reason.
            print(f'Oops! We had a problem creating the table. This is the reason: {e}')

    def view_table(self): # This function does a SELECT query from the table.
        self.connect = psycopg2.connect( 
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
        self.cursor = self.connect.cursor()
        self.cursor.execute('SELECT * FROM to_do_list ORDER BY id')
        return self.cursor.fetchall() # This variable contains all the regist of the table.
        # FETCHALL() return a list with all the registers.

    def insert_into_table(self, task, date, time): # This function does a INSERT query in to the table.
        self.connect = psycopg2.connect(
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
        self.cursor = self.connect.cursor()
        self.cursor.execute('INSERT INTO to_do_list (task, date, hour) VALUES (%s, %s, %s)', (task, date, time))
        self.connect.commit()
        self.cursor.execute('SELECT * FROM to_do_list ORDER BY id')
        return self.cursor.fetchall()

    def edit_for_table(self, selection, task, date, time): # This function does a UPDATE query in to the table.
        self.connect = psycopg2.connect(
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
        self.cursor = self.connect.cursor()
        query = "UPDATE to_do_list SET task = %s, date = %s, hour = %s WHERE id = %s"
        self.cursor.execute(query, (task, date, time, selection))
        self.connect.commit()
        self.cursor.execute('SELECT * FROM to_do_list ORDER BY id')
        regist_list_updated = self.cursor.fetchall()
        return regist_list_updated

    def delete_from_table(self, id_regist):
        self.connect = psycopg2.connect( # This var allows the connection with the database...
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'DELETE FROM to_do_list WHERE id = {id_regist}')
        self.connect.commit()
        self.cursor.execute('SELECT * FROM to_do_list ORDER BY id')
        columns = self.cursor.fetchall()
        if len(columns) == 0:
            self.cursor.execute('ALTER SEQUENCE to_do_list_id_seq RESTART WITH 1') # This query reset all Id.
            self.connect.commit()
            self.cursor.execute('SELECT * FROM to_do_list ORDER BY id')
            return self.cursor.fetchall()
        else: 
            return columns

    def delete_all(self):
        self.connect = psycopg2.connect( # This var allows the connection with the database...
                dbname='TaskList',
                user='postgres',
                password='Asia_27.',
                host='localhost',
            )
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'DELETE FROM to_do_list')
        self.connect.commit()
        self.cursor.execute('ALTER SEQUENCE to_do_list_id_seq RESTART WITH 1')
        self.connect.commit()
    
    