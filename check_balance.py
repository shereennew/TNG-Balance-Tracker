BALANCE_FILE = "balance.txt"

# gets the balance value from balance.txt
def read_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 0.0
    except ValueError:
        return 0.0

# displays the balance value
def check_balance():
    return read_balance()

#low balance warning
def check_low_balance():
    balance = read_balance()
    if balance < 10:
        print("⚠️ Warning: Your balance is below RM10. Please top up soon!")

