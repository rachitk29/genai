def calculate_bill(cups, pricer_per_cup):
    return cups * pricer_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2", calculate_bill(2,200))