names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [70, 40, 20, 80]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")