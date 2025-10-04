# ingredients = ["water", "milk", "black tea"]
# ingredients.append("sugar")
# print(f"Ingredients are : {ingredients}")
# ingredients.remove("water")
# print(f"Ingredients are : {ingredients}")

# spice_options = ["ginger", "cardamom"]
# chai_ingredients = ["water", "milk"]

# chai_ingredients.extend(spice_options)
# print(f"Chai : {chai_ingredients}")

# chai_ingredients.insert(2, "black tea")
# print(f"Chai : {chai_ingredients}")

# last_updated = chai_ingredients.pop()
# print(f"Last Updated : {chai_ingredients}")

# chai_ingredients.reverse()
# print(f"Reverse : {chai_ingredients}")

# chai_ingredients.sort()
# print(f"Sort : {chai_ingredients}")


sugar_levels = [1,2,3,4,5,6]
print(f"Max level : {max(sugar_levels)}")
print(f"Min level : {min(sugar_levels)}")


base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix : {full_liquid_mix}")

strong_brew  = ["black tea", "water"] * 3
print(f"String brew : {strong_brew}")