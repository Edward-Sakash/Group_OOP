class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, s_id, gpa):
        super().__init__(name, age)
        self.s_id = s_id
        self.gpa = gpa

    def print_details(self):
        super().print_details()
        print(f"Student ID: {self.s_id}")
        print(f"GPA: {self.gpa}")


class Teacher(Person):
    def __init__(self, name, age, t_id, specialization):
        super().__init__(name, age)
        self.t_id = t_id
        self.specialization = specialization

    def print_details(self):
        super().print_details()
        print(f"Teacher ID: {self.t_id}")
        print(f"Specialization: {self.specialization}")
