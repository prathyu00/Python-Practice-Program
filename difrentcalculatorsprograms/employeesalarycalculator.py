employee_name = input("enter employee name: ")
basic_salary = float(input("enter basic salary: "))
experience = int(input("enter years of experience: "))

hra = basic_salary*0.20
da = basic_salary*0.10

if experience >= 5:
    bonus = basic_salary*0.15
elif experience >=3:
    bonus = basic_salary*0.10
else:
    bonus=basic_salary*0.05
    
gross_salary = basic_salary+hra+da+bonus

if gross_salary >= 50000:
    tax = gross_salary*0.10
else:
    tax =gross_salary*0.05
    
net_salary=gross_salary-tax

print("\n------EMPLOYEE SALARY-------")
print("Employee: ",employee_name)
print("basic salary",basic_salary)
print("HRA",hra)
print("DA",da)
print("bonus:",bonus)
print("gross salary:",gross_salary)
print("tax:",tax)
print("NET SALARY",net_salary)    
    