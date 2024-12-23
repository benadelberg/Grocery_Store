import sqlite3

conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

queries = [
    "SELECT * FROM Customers;"
]