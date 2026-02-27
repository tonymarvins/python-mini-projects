from operations import add, subtract, multiply, divide
from utils import get_number
from config import APP_NAME

def menu():
    print(f"\n{APP_NAME}")
    print("1 add")
    print("2 subtract")
    print("3 multiply")
    print("4 divide")
    print("5 exit")
def run():
    while True:
        menu()
        choice = input("select option: ")

        if choice =="5";
          break
        a = get_number("first number: ")
        b = get_number("second number: ")

        try:
            if choice == "1":
                print(add(a, b))
            elif choice == "2":
                print(subtract(a, b))
            elif choice == "3":
                print(multiply(a, b))
            elif choice == "4":
                print(divide(a,b))
        except Execution as e:
            print(e)


if __name__ == "__main__":
    run()
