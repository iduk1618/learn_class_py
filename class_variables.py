

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return (f"{self.first}{" "}{self.last}")
        
    #self daje mogucnost da samo zeljena instanca promieni svoje vriednosti
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#Stampa 0 jer jos nije instancirana ni jedan emp    
print(Employee.num_of_emps)

emp_1 = Employee('Ivan','Djuka',120000)
emp_2 = Employee('Nikola','Nikolic',60000)

#Stampa 2 jer su instancirana 2 emp
print(Employee.num_of_emps)

# print(Employee.__dict__)

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)