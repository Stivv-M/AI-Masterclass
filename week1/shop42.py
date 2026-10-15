prices = {"Rice": 200, "Sugar": 180, "Milk": 70, }
quantities = {}
totals = {}
grand_total = 0
total_items = 0


def calculate_discount(total):
    if total > 5000:
        return total * 0.1
    elif total > 3000:
        return total * 0.05
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


for product in prices:
    quantity = int(input(f"{product}: "))
    quantities[product] = quantity

    total = prices[product] * quantity
    totals[product] = total

    grand_total = grand_total + total
    total_items = total_items + quantity
    discount = calculate_discount(grand_total)
    tax = calculate_tax(grand_total)
    final_price = grand_total - discount + tax

print()
print("====== SALES RECEIPT ======")
print()
print(f"{'Product':<10} {'Qty':<5} {'Price':<12} {'Total'}")

for product in prices:
    print(
        f"{product:<10} {quantities[product]:<5} KSh {prices[product]:<8.2f} KSh {totals[product]:.2f}")

print("----------------------------")
print(f"Total items: {total_items}")
print(f"Grand Total: KSh {grand_total:.2f}")
print(f"Discount: KSh {discount:.2f}")
print(f"Tax: KSh {tax:.2f}")
print(f"Final Price: KSh {final_price:.2f}")
print("============================")
