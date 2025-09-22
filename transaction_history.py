from datetime import datetime

HISTORY_FILE = "transactions.txt"  # store all history here

def add_transaction(kind, amount, balance):
    #Save a transaction record with datetime into a file
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{time_now} | {kind.upper()}: RM{amount:.2f}, Balance: RM{balance:.2f}"
    with open(HISTORY_FILE, "a") as f:   # append mode
        f.write(record + "\n")

def show_history():
    #Display all past transactions
    print("\nTransaction History:")
    try:
        with open(HISTORY_FILE, "r") as f:   # read mode
            history = f.readlines()
            if history:
                for line in history:
                    print(line.strip())
            else:
                print("No transactions yet.")
    except FileNotFoundError:
        print("No transaction history file found.")

