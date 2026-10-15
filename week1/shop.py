def calculate_cost(price, quantity):
    return price * quantity


def calculate_discount(total):
    if total >= 5000:
        return total * 0.10
    elif total >= 3000:
        return total * 0.05
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = calculate_cost(price, quantity)
discount = calculate_discount(total)
tax = calculate_tax(total)

final_price = total - discount + tax

print("\n======SALES RECEIPT======\n")
print(f"Price per item: KES {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: KES {total:.2f}")
print(f"Discount: KES {discount:.2f}")
print(f"Tax: KES {tax:.2f}")
print(f"Final price: KES {final_price:.2f}")
print("============================")
print("\nThank you for shopping!")
