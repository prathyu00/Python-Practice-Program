name=input("enter student name: ")
maths=int(input("enter maths mark: "))
science=int(input("enter science mark: "))
english=int(input("enter english mark: "))
python=int(input("enter python mark: "))
computer=int(input("enter computer mark: "))

total=maths+science+english+python+computer
average=total/5
percentage=(total/500)*100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"
    
if percentage>=40:
    result="pass"
else:
    result="fail"
    
    
    
print("........student marks.........")
print("student name is: ",name) 
print("total mark: ",total)   
print("average is: ",average)
print("percentage is: ",percentage,"%")
print("grade is: ",grade)
print("result",result)   
    
