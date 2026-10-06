number_of_student=int(input("how many student? "))
for student in range(number_of_student):
    print("/nstudent",student + 1)
    name=input("enter student name: ")
    marks=float(input("enter marks: "))
    if marks >=90:
        grade ="A+"
    elif marks >=80:
        grade ="A"
    elif marks >=70:
        grade ="B"
    elif marks >=60:
        grade="C"
    elif marks >=40:
        grade="D"
    else:
        grade="F"


print("Name",name)
print("marks",marks)
print("grade",grade)
