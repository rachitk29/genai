essential_spices = {"cardamom", "ginger", "cinamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices : {all_spices}")

all_spices = essential_spices & optional_spices
print(f"Common Spices : {all_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only essential Spices : {only_in_essential}")

print(f"Is 'cloves' in essential spices ? {'ginger' in essential_spices}")

