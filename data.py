import csv
import random

# Store Table
stores = [
    [1, "123 Main St"],
    [2, "456 High St"],
    [3, "789 Elm St"],
]

# Employees Table
employees = [
    [1, "Alice Manager", "Manager"],
    [2, "Bob Cashier", "Cashier"],
    [3, "Charlie Stocker", "Stocker"],
    [4, "David Manager", "Manager"],
    [5, "Eve Cashier", "Cashier"],
    [6, "Frank Stocker", "Stocker"],
    [7, "Grace Manager", "Manager"],
    [8, "Heidi Cashier", "Cashier"],
    [9, "Isaac Stocker", "Stocker"],
]

# Timesheet Table (Only Hours)
timesheets = [[i + 1, random.randint(4, 8)] for i in range(len(employees) * 3)]

# Ice Cream Table
ice_cream_flavors = [
    "Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookies and Cream",
    "Rocky Road", "Butter Pecan", "Pistachio", "Neapolitan", "Coffee",
    "Caramel Swirl", "Chocolate Chip", "Birthday Cake", "Mango Sorbet", "Raspberry Ripple",
    "Coconut", "Peanut Butter Cup", "Brownie Batter", "Cherry Garcia", "Blueberry Cheesecake",
    "Salted Caramel", "Cotton Candy", "Black Raspberry", "Lemon Sorbet", "Maple Walnut",
    "Tiramisu", "Green Tea", "Honey Lavender", "Almond Joy", "Dulce de Leche",
    "Mocha Almond Fudge", "Bubble Gum"
]
ice_cream = [[i + 1, flavor, random.choice([True, False]), random.randint(10, 50), random.randint(2, 6)] for i, flavor in enumerate(ice_cream_flavors)]

# Cones Table
cone_types = ["Waffle", "Sugar", "Cake", "Gluten-Free"]
cones = [[i + 1, cone, cone == "Gluten-Free", random.randint(20, 100), random.randint(1, 3)] for i, cone in enumerate(cone_types)]

# Customers Table
customers = [
    [1, "John Doe", random.randint(1, 5)],
    [2, "Jane Smith", random.randint(1, 5)],
    [3, "Mike Johnson", random.randint(1, 5)],
]

# Sales Table
sales = [[i + 1, random.randint(10, 500), customers[i][0]] for i in range(len(customers))]

# Inventory Table
inventory = [[i + 1, random.randint(1, len(ice_cream)), random.randint(1, len(cones))] for i in range(10)]

# Save as CSV Files
def save_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

save_csv("store.csv", stores, ["ID", "Location"])
save_csv("employees.csv", employees, ["ID", "Name", "Position"])
save_csv("timesheet.csv", timesheets, ["ID", "Hours"])
save_csv("ice_cream.csv", ice_cream, ["ID", "Flavor", "Dairy Free", "Quantity", "Price"])
save_csv("cones.csv", cones, ["ID", "Cone Type", "Gluten Free", "Quantity", "Price"])
save_csv("customer.csv", customers, ["ID", "Name", "Purchases"])
save_csv("sales.csv", sales, ["ID", "Profit", "Customer ID"])
save_csv("inventory.csv", inventory, ["ID", "Ice Cream ID", "Cones ID"])
