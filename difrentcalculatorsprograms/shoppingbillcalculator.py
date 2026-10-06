customer=input("enter customer name: ")

milk_price=float(input("enter milk price: "))
milk_quantity=int(input("enter milk quantity: "))

rice_price=float(input("enter rice price: "))
rice_quantity=int(input("enter rice quantity: "))

bread_price=float(input("enter bread price: "))
bread_quantity=int(input("enter bread quantity: "))

fruit_price=float(input("enter fruit price: "))
fruit_quantity=int(input("enter fruit quantity: "))

rice_total=rice_price*rice_quantity
milk_total=milk_price*milk_quantity
bread_total=bread_price*bread_quantity
fruit_total=fruit_price*fruit_quantity

sub_total=milk_total+bread_total+fruit_total+rice_total

if sub_total>=2000:
    discount=sub_total*0.20
elif sub_total>=1000:
    discount=sub_total*0.10
else:
    discount=0
    
taxable_amount=sub_total-discount
    
gst=taxable_amount*0.05

final_bill=taxable_amount*gst

print("....total bill.....")
print("customer name: ",customer)
print("subtotal: ",sub_total)
print("discount: ",discount) 
print("gst",gst) 
print("final bill",final_bill)  
    





