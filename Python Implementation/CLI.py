import sqlite3

from start.py import * 

def check_existing_table(table_name,db_name):
    with sqlite3.connect(db_name):
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()

def recreate_table(table_name,db_name):
    if len(result) == 1:
        
