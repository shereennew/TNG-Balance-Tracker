

BALANCE_FILE = "balance.txt"  

def read_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 0.0
    except ValueError:
        return 0.0
    
def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def top_up():
    balance = read_balance()  # get current balance from file
    try:
        amount = float(input("Enter top-up amount: RM "))
        if amount > 0:
            balance += amount
            save_balance(balance)
            print(f"Top-up successful! New balance: RM {balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
