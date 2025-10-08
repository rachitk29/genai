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

flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while(flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry", {flavour} is not available)
print(f"You choose {flavour} chai")