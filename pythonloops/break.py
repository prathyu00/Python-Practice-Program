a=int(input("enter a number: "))
for i in range(2,a+1):
 if a%i == 0:
    break
if a==i:
    print(a,"the number is prime")
else:
    print(a,"the number is not prime")
    