

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return (f"{self.first}{" "}{self.last}")
        


emp_1 = Employee('Ivan','Djuka',120000)
emp_2 = Employee('Nikola','Nikolic',60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

print((emp_1.fullname()))         #Nema potrebe pozivate self, automatski
print(Employee.fullname(emp_1))     #Mora da se pozove instanca koji zelimo