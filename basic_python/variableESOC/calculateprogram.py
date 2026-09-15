a=int(input("enter first number: "))
c=input("enter operaters like (+,-,*,%) : ")
b=int(input("enter second number: "))

if c == "+":
    result=(a+b)
elif c == "_":
   result=(a-b)
elif c == "*":
    result=(a*b)
elif c== "%":
    result=(a%b)   
else:
    print("invalid operator")
    
print("the final result",result)
   
    
    
   

