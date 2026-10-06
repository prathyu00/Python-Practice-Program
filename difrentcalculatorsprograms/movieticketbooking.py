total_ticket=0
total_amount=0

number_of_people = int(input("enter numer of people: "))

for person in range(number_of_people):
    print("\nperson" ,person + 1 )
    
    age=int(input("enter age: "))
    
    if age<5:
        ticket_price=0
        category="free"
        
    elif age <=12:
        ticket_price=120
        category="child"
        
    elif age<=59:
        ticket_price=200
        category="adult"
        
    else:
        ticket_price=100
        category="senior citizen"
        
        
total_ticket=total_ticket+1
total_amount=total_amount+ticket_price

print("category: ",category)
print("ticket price:",ticket_price)

print("\n------BOOKING SUMMARY-------")
print("total tickets",total_ticket)
print("total amount",total_amount)
        
        