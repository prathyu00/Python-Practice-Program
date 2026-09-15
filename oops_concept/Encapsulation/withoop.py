class Employee:
    def __init__(self,salary,overtime,rate):
        self.salary = salary
        self.overtime = overtime
        self.rate = rate
        
    #the logic is encapsulated with the object
    def get_wage(self):
        return self.salary + (self.overtime * self.rate)
    
    #usage
    emp = Employee(50000,10,20)
    print(emp.get_wage())#you simply call method [1]
        