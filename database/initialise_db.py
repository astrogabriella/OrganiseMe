import sqlite3 as sql 

dbCon = sql.connect("database/organise_me.db") 

dbCursor = dbCon.cursor()

with open("database/schema.sql","r") as sql_file:
    sql_commands = sql_file.read()

try:
    dbCursor.executescript(sql_commands)
except sql.Error as e:
    print("Error executing SQL commands:", e)

dbCon.commit()
dbCon.close()

print("Database setup and data insertion completed.")