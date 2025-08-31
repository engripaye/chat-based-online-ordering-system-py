import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",       # change to your MySQL username
        password="1234567", # change to your MySQL password
        database="chat_ordering"
    )
