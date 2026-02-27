def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid number, try again")
import datetime

def log(message: str):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {message}")
