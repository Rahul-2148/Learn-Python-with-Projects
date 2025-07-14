class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
# creating objects
student1 = Student('Sujay', 24, 'A+')
Student2 = Student('Mudassar', 25, 'B+')

print(student1.name, student1.age, student1.grade)
print(Student2.name, Student2.age, Student2.grade)

"""
1- default constructor (self)
2- parameterized constructor (self, name, age, grade)
3- constructor with default values, (self, name="unknown", age=0, grade="F")
"""