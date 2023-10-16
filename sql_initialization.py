import sqlite3

connection = sqlite3.connect("database_azienda.db")

with open("database_management.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()