total =0

while True:
    print("\n--------- Menu ---------")
    print("1. Pizzaa - 250")
    print("2. Burger - 150")
    print("3. pasta - 200")
    print("4. coffee - 80")
    print("5. finish order")
    
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        quantity = int(input("enter quantity: "))
        price = 250
        total = total + (price * quantity)

    elif choice == 2:
        quantity = int(input("enter quantity: "))
        price = 150
        total = total + (price * quantity)
        
    elif choice == 3:
        quantity = int(input("enter quantity: "))
        price = 200
        total = total + (price * quantity) 
        
    elif choice == 4:
        quantity = int(input("enter quantity: "))
        price = 80
        total = total + (price * quantity)       
        
    elif choice == 5:
        break
    
    else:
        print("invalid choice.")
        
gst=total*0.05
final_amount=total+gst

print("\n-----FINAL BILL-------")
print("food total:",total)
print("gst",gst) 
print("final amount",final_amount)       
         
    
     