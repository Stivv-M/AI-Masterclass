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


print()
print("SALES RECEIPT\n")
for product in prices:
    quantity = int(input(f"{product}: "))
    quantities[product] = quantity

    total = prices[product] * quantity
    totals[product] = total

    grand_total = grand_total + total
    total_items = total_items + quantity

    discount = calculate_discount(grand_total)
    tax = calculate_tax(grand_total)
print()
print(f"{'PRODUCT':<10} {'QTY':<5} {'PRICE':<16} {'TOTAL'}")
for product in prices:
    print(f"{product:<10} {quantities[product]:<5} KES {prices[product]:<12.2f}"
          f" KES {totals[product]:.2f}")
print("\n----------------------------")
print(f"Total items: {total_items}")
print(f"Grand Total: KES {grand_total:.2f}")
print(f"Discount: KES {discount:.2f}")
print(f"Tax: KES {tax:.2f}")
print(f"Final Price: KES {grand_total - discount + tax:.2f}")
print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.end of receipt')
print()
