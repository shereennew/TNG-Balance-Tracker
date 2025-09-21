def check_bal ():
    pass
def top_up ():
    pass
def make_payment ():
    pass
def trans_history ():
    pass

balance = 0.00
transaction = []

def menu () :
    
    while True :
        
        print ("Welcome to TNG Balance Tracker! \n")    
        print ("1. Check Balance\n2. Top-up\n3. Make Payment\n4. Transaction History\n5. Exit\n")

        user_input = input("Enter Choice: ")
        if user_input == "1" :
            check_bal()
        elif user_input == "2" :
            top_up() 
        elif user_input == "3" :
            make_payment() 
        elif user_input == "4" :
            trans_history()
        elif user_input == "5" :
            print ("Thank you for using TNG Balance Tracker!")
            break 
        else :
            print ("Invalid Choice. Please Try Again.")
            continue

        while True :
            cont = input("Do you want to continue? (y/n) : ")
            if cont.lower() == "y":
                break
            elif cont.lower() == "n":
                print ("Thank you for using TNG Balance Tracker!")
                return
            else :
                print ("Invalid Input. Please Try Again.")
                continue

if __name__ == "__main__":
    menu()
