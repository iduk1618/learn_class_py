 

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
    
    @staticmethod
    def is_workday(day):
        if day .weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Ivan','Djuka',120000)
emp_2 = Employee('Nikola','Nikolic',60000)

import datetime
my_date = datetime.date(2025, 4, 14)
print(Employee.is_workday(my_date))