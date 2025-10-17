def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100  

orders = [100, 15, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")