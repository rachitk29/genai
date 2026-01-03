marks = [90,23,50,69,87]

print(marks)
print(len(marks))
print(marks[3])  #index value
# print(marks[7]) list index out of range
 
# list are mutuabl can be changed see how 
marks[2] = 99
print(marks)

# indexing in list 
print(marks[:3])
print(marks[3:])
print(marks[3:len(marks)])
