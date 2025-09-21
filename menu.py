from check_balance import check_balance as check_bal
from top_up import top_up
from deduct_balance import deduct_balance as make_payment
from transaction_history import show_history as trans_history
from pin import set_pin, verify_pin, change_pin

def menu () :
    print("🌟 Welcome to TNG Balance Tracker! 🌟")
    if not verify_pin():
        choice = input("No PIN or incorrect. Do you want to set one? (y/n): ")
        if choice.lower() == "y":
            set_pin()
        else:
            print("Exiting program.")
            return

    while True :
        
        print ("🌟 Welcome to TNG Balance Tracker! 🌟\n")    
        print ("1. 💰 Check Balance\n2. ➕ Top-up\n3. 💸 Make Payment\n4. 📜 Transaction History\n5. 🔑 Change PIN\n6. 👋 Exit\n")

        user_input = input("Enter Choice: ")
        if user_input == "1" :
            print("Your balance is: ", check_bal())
        elif user_input == "2" :
            top_up() 
        elif user_input == "3" :
            make_payment() 
        elif user_input == "4" :
            trans_history()
        elif user_input == "5" :
            change_pin()
        elif user_input == "6" :
            print ("Thank you for using TNG Balance Tracker!👋")
            break 
        else :
            print ("Invalid Choice. Please Try Again.❌")
            continue

        while True :
            cont = input("Do you want to continue? (y/n) : ")
            if cont.lower() == "y":
                break
            elif cont.lower() == "n":
                print ("Thank you for using TNG Balance Tracker!👋")
                return
            else :
                print ("Invalid Input. Please Try Again.❌")
                continue

if __name__ == "__main__":
    menu()
