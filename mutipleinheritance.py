class Person:
    def __init__(self):
        print("Person constructor")

    def show(self):
        print("I am a person")


class Student(Person):
    def __init__(self):
        print("Student constructor")
        super().__init__()

    def study(self):
        print("Studying")


class Employee(Person):
    def __init__(self):
        print("Employee constructor")
        super().__init__()

    def work(self):
        print("Working")


class Intern(Student, Employee):
    def __init__(self):
        print("Intern constructor")
        super().__init__()

    def intern_role(self):
        print("I am an intern")


i = Intern()

i.show()
i.study()
i.work()
i.intern_role()
