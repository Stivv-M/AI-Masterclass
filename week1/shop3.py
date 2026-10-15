def calculate_price(price, quantity):
    return price * quantity


def calculate_discount(total):
    if total >= 10000:
        return total * 0.10
    elif total >= 8000:
        return 0.05
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


price = float(input("Enter Price:-----------"))
quantity = int(input("Enter Quantity:-------"))

total = calculate_price(price, quantity)
discount = calculate_discount(total)
tax = calculate_tax(total)
final_price = total - discount + tax
name = 'Stephen'
print("SALES RECEIPT\n")
print("EASTMATT MATTRESS LTD-GILGIL\n"
      "P.O BOX 54816 - 00200\n"
      "NAIROBI\n"
      "TEL 0722542814\n\n")
print(f"Price per item: KES {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: KES {total:2f}")
print(f"Discount: KES {discount: 2f}")
print(f"Tax: KES {tax:.2f}")
print(f"Final Price: KES {final_price} \n")
print(f"Served by: {name}")
print("\n Thank You For Shopping")
