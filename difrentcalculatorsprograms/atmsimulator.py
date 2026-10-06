balance=10000
pin=1234

enterred_pin=int(input("enter the pin: "))
if enterred_pin == pin:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
     
        choice= int(input("enter your choice"))     
        if choice==1:
            print("balance is: ",balance)
        elif choice==2:
            deposit=float(input("enter deposite amount: "))
            balance=balance+deposit
            print("deposit successfull")
            print("new balance",balance)
        elif choice==3:
            withdrawal=float(input("enter your withdrawal amount: "))
            if withdrawal<=balance:
                balance=balance-withdrawal
                print("please collect your cash")
                print("remaining balance: ",balance)
                print("insufficient balance")
            elif choice == 4:
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice.")

        else:
            print("Incorrect PIN.")
    
    
    
        
    
    