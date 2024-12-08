import sqlite3

def init_db():
    connection = sqlite3.connect('data.db')
    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks (
            ID INTEGER PRYMARY KEY,
            User_ID INTEGER NOT NULL,
            Task_Text TEXT NOT NULL,
            Status BOOLEAN DEFAULT 0
            )
        '''
    )
    connection.commit()
    connection.close()

def get_connection():
    return sqlite3.connect('data.db')