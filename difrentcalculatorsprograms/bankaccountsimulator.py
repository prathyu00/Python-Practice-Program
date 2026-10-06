balance=5000
transaction=[]

while True:
    print("\n ==== BANK MENU ====")
    print("1. check balance")
    print("2. deposite")
    print("3. withdraw")
    print("4. transactions")
    print("5. exit")
    
    choice =int(input("enter your choice: "))
    if choice == 1:
        print("current balance:",balance)
        
    elif choice == 2:
        amount=float(input("enter deposite amount: "))
        
        if amount > 0:
            balance=balance+amount
            transaction.append("deposite money"+str(amount))
            print("deposite succesfully")
        else:
            print("invalid amount")
            
    elif choice == 3:
        amount = float(input("enter withdrawal amount "))
        if amount >0 and amount<=balance:
            balance=balance-amount
            transaction.append("withdrawal money" + str(amount))
            print("withdrawal succesful.")
            
        else:
            print("invalid amount")
            
    elif choice == 4:
        print("\n ----- transactions-----")
        if len(transaction) ==0:
            print("no transaction yet")
        else:
            for transactions in transaction:
                print(transactions)
                
    elif choice == 5:
        print("thank you for banking with us.")
        break
    
    else:
        print("invalid choice. ")
        