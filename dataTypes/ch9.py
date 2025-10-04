chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base : {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")

print(f"Is Sugar in the order? {'sugar' in chai_order}")

print(f"Order details (keys): {chai_order.keys()}") 
print(f"Order details (values): {chai_order.values()}") 
print(f"Order details (items): {chai_order.items()}") 