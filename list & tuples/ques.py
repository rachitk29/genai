info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

courses = set( )

for tup in info:
    courses.add((tup[1])) #courses

print(courses)

for name, course in info:
    if(course == "English"):
        print(name)


dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
        