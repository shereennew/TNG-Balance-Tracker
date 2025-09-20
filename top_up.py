from check_balance import read_balance  

BALANCE_FILE = "balance.txt"  

def save_balance(balance):
    """Write the updated balance to the file."""
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def top_up():
    """Ask for top-up amount, add to balance, save it."""
    balance = read_balance()  # get current balance
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