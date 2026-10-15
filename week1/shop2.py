prices = {"Rice": 200, "Sugar": 180, "Milk": 70}
quantities = {"Rice": 2, "Sugar": 3, "Milk": 4}


def calculate_discount(grand_total):
    if grand_total >= 5000:
        return grand_total * 0.10
    elif grand_total >= 3000:
        return grand_total * 0.05
    else:
        return 0


def calculate_tax(grand_total):
    return grand_total * 0.16


grand_total = 0
total_items = 0

for product in prices:
    total = prices[product] * quantities[product]
    grand_total = grand_total + total
    total_items = total_items + quantities[product]

    print(f"{product}: KSh {total:.2f}")

discount = calculate_discount(grand_total)
tax = calculate_tax(grand_total)

final_price = grand_total - discount + tax

print(f"Total items: {total_items}")
print("--------------------")
print(f"Grand total: KSh {grand_total:.2f}")
print(f"Discount: KSh {discount:.2f}")
print(f"Tax: KSh {tax:.2f}")
print(f"Final price: KSh {final_price:.2f}")
