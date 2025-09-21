from datetime import datetime

transactions = [] #store all history here

def log_transaction(kind, amount, balance): #save a transaction record with datetime
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{time_now} | {kind.upper()}: RM{amount:.2f}, Balance: RM{balance:.2f}"
    transactions.append(record)

def show_history(): #display all past transactions
    if not transactions:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for t in transactions:
            print("-", t)