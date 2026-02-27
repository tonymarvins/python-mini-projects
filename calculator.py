# Luis's Calculator 🧮
# First amateur draft

def menu():
     print("\n Welcome to my calculator! 🧮")
    print("Choose an option:")
    print("1. Add ➕")
    print("2. Subtract ➖")
    print("3. Multiply ✖️")
    print("4. Divide ➗")
    print("5. Exit")

menu()
def add(a, b):
    return a + b
    # Testing addition
    print("2 + 3 =", add(2, 3))

def subtract(a, b):
    return a - b
    # Testing subtraction
    print("5 - 2 =", subtract(5, 2))

def multiply(a, b):
    return a * b
    # Testing multiplication
    print("4 * 3 =", multiply(4, 3))

def divide(a, b):
    return a / b
    # Testing division
    print("10 / 2 =", divide(10, 2))

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

