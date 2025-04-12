

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

    #Prima klasu kao prvi argument a ne instancu (self), po konvenciji ime je (cls)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    #Metod koji iz promenljive koja je string, razdvaja string u vise komponenti
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)
        return cls(first, last, pay)

emp_1 = Employee('Ivan','Djuka',120000)
emp_2 = Employee('Nikola','Nikolic',60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)