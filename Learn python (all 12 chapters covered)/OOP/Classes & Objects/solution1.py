class Student:
    def set_details(self, name, marks):
        self.name = name
        self.marks = marks
        
Student1 = Student()
Student1.set_details('Sujay', 75)
print(Student1.name, Student1.marks)