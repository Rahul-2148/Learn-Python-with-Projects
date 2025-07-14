class Student:
    def set_details(name, marks):
        name = name
        marks = marks
        
Student1 = Student()
Student1.set_details('Sujay', 75)
print(Student1.name, Student1.marks)

# bina self ke attribute error aayega kyuki python ko pata hi nhi chalega ki 75 marks kiska h bhot sare students me so self se findout kr leta h name ke basis pr