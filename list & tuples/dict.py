# key : value pairs 
# dictionaries are mutuable

info = {
    "name" : "rachit",
    "cgpa" : 8.5,
    "subjects": ["maths", "science"],
    3.14 : "PI"
}

print(type(info))
print(info["name"])

print(info.keys())
print(info.items())

print(info.get("cgpa2"))  # wrong key 
print("End of code")