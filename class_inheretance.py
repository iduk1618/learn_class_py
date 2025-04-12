

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

dev_1 = Developer('Ivan','Djuka',120000,'Python')
dev_2 = Developer('Nikola','Nikolic',60000,'Java')

mgr_1 = Manager('Sue','Smith',160000, [dev_1])

print(isinstance(mgr_1,Developer))
print(issubclass(Manager,Developer))




# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.rem_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)