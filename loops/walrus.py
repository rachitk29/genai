# value = 14
# reminder = value % 5

# if reminder:
#     print(f"Not divisible, reminder is {reminder}")

value = 13

if(reminder := value % 5): 
    print(f"Not divisible, reminder is {reminder}")


available_sizes = ["small", "medium", "large"]
if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")