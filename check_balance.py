BALANCE_FILE = "balance.txt"

def read_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 0.0
    except ValueError:
        return 0.0

def check_balance():
    return read_balance()

read_balance()