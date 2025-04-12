

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return (f"{self.first}{" "}{self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, emplyees=None):
        super().__init__(first, last, pay)
        if emplyees is None:
            self.emplyees = []
        else:
            self.emplyees = emplyees
    def add_emp(self, emp):
        if emp not in self.emplyees:
            self.emplyees.append(emp)

    def rem_emp(self, emp):
        if emp in self.emplyees:
            self.emplyees.remove(emp)

    def print_emps(self):
        for emp in self.emplyees:
            print('-->', emp.fullname())

emp_1 = Developer('Ivan','Djuka',120000)
emp_2 = Developer('Nikola','Nikolic',60000)

 