chai_type  = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} Please..! ")

chai_description = "Aromatic and Bold"
print(f"Description : {chai_description [0:5:3]}")
print(f"Last Word : {chai_description[:: -1]}")

label_text = "chai special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded Label : {label_text}")
print(f"Encoded label : {encoded_label}")

decode_label = encoded_label.("utf-8")
print(f"Decoded label : {decode_label}")
