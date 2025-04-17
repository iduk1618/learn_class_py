

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age= age
        Student.num_students += 1

student1 = Student("Milan", 30)
student2 = Student("Neven", 35)
student3 = Student("Marko", 55)
student4 = Student("Ana", 27)

print(student1.name)
print(student1.age)
print(Student.class_year)       #Bolje je pozivati class variable preko imena klase, a ne preko imena instance.

print(student2.name)
print(student2.age)
print(Student.class_year)       #Znamo da je class_year class variable jer pristupamo preko imena klase a ne preko imena instance.

print(f"My graduating class of {Student.class_year} and has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)