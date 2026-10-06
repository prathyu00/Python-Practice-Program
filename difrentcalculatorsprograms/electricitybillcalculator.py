customer=input("enter customer name: ")
unit=int(input("enter electricity units consumed: "))

if unit <= 100:
    bills=unit*2
elif unit <= 200:
    bills = (100*2)+((unit-100)*3)
elif unit <= 300:
    bills = (100*2)+(100*3)+((unit-200)*5)        
else:
    bills = (100*2)+(100*3)+(100*5)+((unit-300)*7)
    
fixxed_charge=100
total_bill=bills+fixxed_charge

print("\n----- ELECTRICITY BILL -----")
print("Customer:", customer)
print("Units Consumed:", unit)
print("Energy Charge:", bills)
print("Fixed Charge:", fixxed_charge)
print("Total Bill:", total_bill)