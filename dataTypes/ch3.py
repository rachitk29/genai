is_boiling = True
string_count = 5
total_actions = string_count + is_boiling   # upcasting
print(f"Total Actions : {total_actions}")

milk_present = 1 # no milk
print(f"Is there no milk : {bool(milk_present)}")


water_hot = True
tea_added = True 

can_serve = water_hot and tea_added
print(f"Can serve : {can_serve}")