# Luis's Calculator final tweaks 
# First amateur draft

def menu():
     print("\nWelcome to my calculator! 🧮")
     print("Choose an option:")
     print("1. Add ➕")
     print("2. Subtract ➖")
     print("3. Multiply ✖️")
     print("4. Divide ➗")
     print("5. Exit")
menu()
  #test the  functions with real numbers
def add(a, b):
    return a + b
   
def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
     
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

