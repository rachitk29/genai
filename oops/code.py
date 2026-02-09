# class Student: 
#     subject = "Python"
#     college = "Apna"
#     year = "4th year"

# stu1 = Student()

# l = [1, 2]
# s = set()
# print((stu1.subject))

class Student():
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa 

    def get_cgpa(self):
            return self.cgpa
    
stu1 = Student("Rahul",9.0)
stu2 = Student("Riya",.70)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa = {stu2.get_cgpa()}")