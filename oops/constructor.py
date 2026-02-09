class Student:
    college_name = "Apna College" #class
    PI = 3.14

    def __init__(self, name, gpa):
        self.name = name #instance
        self.gpa = gpa
        self.PI = 3.14


st1 = Student("Rahul", 9.2)

print(st1.name)
print(st1.PI) # can call by both method #1
print(Student.PI) #2
