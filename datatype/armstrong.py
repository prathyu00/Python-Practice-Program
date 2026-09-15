number=2000
original=number
total=0

while number > 0:
   digit=number%10
   total=total+digit**3
   number=number//10
   
if total == original:
    print(total,"armstrong number")
else:
    print(total,"not an armstrong number")       
   