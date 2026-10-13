"""Assignment 1 - Variables, Data Types, Operators, Strings, Input & Type Casting"""


def show(label, value):
    print(label, value)


# ---------------------------------------------------------------
# Variables and Data types
# ---------------------------------------------------------------

# Task 1 - Employee Profile
name, age, salary = "Areeb", 26, 50000
dept, currenlty_employed = "information technology", True

show("Employee name is ", name)
show("Empolyee age is ", age)
show("Empolyee salary is ", float(salary))
show("Empolyee is employed ", currenlty_employed)

for value in (name, age, salary, dept, currenlty_employed):
    print(type(value))

# Task 2 - Product Information
product_name, product_id = "Phone", 12345
product_price, product_quantity = 30000, 3
inventory_value = product_price * product_quantity

show("Product name is ", product_name)
show("Product ID is ", product_id)
show("Product price is ", float(product_price))
show("Product quantity is ", product_quantity)
show("Inventory value is ", inventory_value)

# ---------------------------------------------------------------
# Operators
# ---------------------------------------------------------------

# Task 1 - Number Calculator
a, b = 10, 3

for label, result in [
    ("Addition of two numbers is ", a + b),
    ("Subtraction of two numbers is ", a - b),
    ("Multiplication of two numbers is ", a * b),
    ("Division of two numbers is ", a / b),
    ("Floor division of two numbers is ", a // b),
    ("Modulus of two numbers is ", a % b),
    ("Exponentiation of two numbers is ", a ** b),
]:
    show(label, result)

# Task 2 - Rectangle Area and Perimeter Calculator
length, width = 5, 3

show("Area of rectangle is ", length * width)
show("Perimeter of rectangle is ", 2 * (length + width))
show("Length squared is ", length ** 2)
show("Width squared is ", width ** 2)

# ---------------------------------------------------------------
# String and String Operations
# ---------------------------------------------------------------

# Task 1 - Name Formatter
name = input("Enter your name:")

show("Orignal name is ", name)
show("Uppercase name is ", name.upper())
show("Lowercase name is ", name.lower())
show("Length of name is ", len(name))
show("First character of name is ", name[0])
show("Last character of name is ", name[-1])
show("First three characters of name is ", name[:3])
show("Last three characters of name is ", name[-3:])

# Task 2 - Email Analyzer
email = input("Enter your email address:")
username, _, domain = email.partition("@")

show("Orignal email is ", email)
show("Username is ", username)
show("Domain is ", domain)
show("Length of email is ", len(email))

# ---------------------------------------------------------------
# Input and Type casting
# ---------------------------------------------------------------

# Task 1 - ATM Withdrawal Calculator
name = input("Enter your account holder name:")
current_balance = float(input("Enter your current balance:"))
withdrawal_amount = float(input("Enter the amount you want to withdraw:"))
notes_received = int(input("Enter the number of notes received:"))

show("Account holder name is ", name)
show("Current balance is ", current_balance)
show("Withdrawal amount is ", withdrawal_amount)
show("Reamaining balance is ", current_balance - withdrawal_amount)
show("Amount per note is ", withdrawal_amount / notes_received)

# Task 2 - Movie Ticket Calculator
customer_name = input("Enter Customer name:")
adult_tickets = int(input("Enter number of adult tickets:"))
adult_ticket_price = float(input("Enter price of adult ticket:"))
child_tickets = int(input("Enter number of child tickets:"))
child_ticket_price = float(input("Enter price of child ticket:"))
popcorn_quantity = int(input("Enter quantity of popcorn:"))
popcorn_price = float(input("Enter price of popcorn:"))

adult_total = adult_tickets * adult_ticket_price
child_total = child_tickets * child_ticket_price
popcorn_total = popcorn_quantity * popcorn_price

show("Customer name is ", customer_name)
show("Total amount for adult tickets is ", adult_total)
show("total amount for adult tickets is ", adult_total)
show("Total amount for child tickets is ", child_total)
show("Total amount for child tickets is ", child_total)
show("popcorn quantity is ", popcorn_quantity)
show("Total amount for popcorn is ", popcorn_total)
print("Total Bill is ", adult_total + child_total + popcorn_total)
