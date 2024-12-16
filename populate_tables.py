import sqlite3

conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

suppliers = [
    ("Fresh Farms", "123-456-7890"),
    ("Dairy World", "234-567-8901"),
    ("Grain Supplies", "345-678-9012"),
    ("Bakery Supplies", "456-789-0123")
]
cursor.executemany("""
INSERT INTO Suppliers (SupplierName, ContactInfo) VALUES (?, ?)
""", suppliers)

products = [
    ("Apple", "Fruits", 0.5, 100, 1),
    ("Banana", "Fruits", 0.2, 150, 1),
    ("Milk", "Dairy", 1.5, 50, 2),
    ("Bread", "Bakery", 2.0, 30, 4),
    ("Egg", "Dairy", 3.0, 20, 2)
]
cursor.executemany("""
INSERT INTO Products (ProductName, Category, Price, StockQuantity, SupplierID) VALUES (?, ?, ?, ?, ?)
""", products)

customers = [
    ("John", "Doe", "johndoe@example.com", 50),
    ("Jane", "Smith", "janesmith@example.com", 100),
    ("Alice", "Johnson", "alicej@example.com", 200)
]
cursor.executemany("""
INSERT INTO Customers (FirstName, LastName, Email, LoyaltyPoints) VALUES (?, ?, ?, ?)
""", customers)

orders = [
    (1, "2024-11-18", 5.0),
    (2, "2024-11-18", 7.0),
    (3, "2024-11-19", 6.0)
]
cursor.executemany("""
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)
""", orders)

order_details = [
    (1, 1, 5, 0.5),
    (1, 2, 10, 0.2),
    (2, 3, 2, 1.5),
    (2, 4, 1, 2.0),
    (3, 5, 1, 3.0)
]
cursor.executemany("""
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES (?, ?, ?, ?)
""", order_details)

conn.commit()
conn.close()

print("Sample data populated successfully")