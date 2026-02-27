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

def run():
    while True:
        menu()
        choice = input("Select option: ")

        if choice == "5":
            print("Goodbye 👋")
            break

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
            else:
                print("Invalid option")

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    run()
