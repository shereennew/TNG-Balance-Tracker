from check_balance import read_balance
from top_up import save_balance   

def deduct_balance():
    balance = read_balance()  
    try:
        amount = float(input("Enter payment amount: RM "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return
        
        if amount > balance:
            print("Insufficient balance. Please top up first.")
            return
        
        balance -= amount
        save_balance(balance)
        print(f" Payment successful! New balance: RM {balance:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
