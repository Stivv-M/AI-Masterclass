def calculate_discount(total):
    if total >= 3000:
        return total * 0.1
    elif total >= 1500:
        return total * 0.05
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


prices = {"Rice": 200, "Sugar": 180, "Milk": 70, "Bread": 150, "Eggs": 10}
quantities = {}
totals = {}
grand_total = 0
item_count = 0

print("SALES RECEIPT\n")
for product in prices:
    while True:
        try:
            quantity = int(input(f"{product}: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a whole number ")
    quantities[product] = quantity
    total = prices[product] * quantity
    totals[product] = total

    grand_total = grand_total + total
    item_count = item_count + quantity

    discount = calculate_discount(grand_total)
    tax = calculate_tax(grand_total - discount)
    final_total = grand_total - discount + tax

cashier = input("Enter cashier name: ")
print("\n----------------------------")
print(f"{'PRODUCT':<10} {'QTY':<5} {'PRICE':<16} {'TOTAL'}")
for product in prices:
    print(f"{product:<10} {quantities[product]:<5} KES {prices[product]:<12.2f}"
          f" KES {totals[product]:.2f}")


print("\n----------------------------")
print(f"{'Item Count':<10} {item_count:<5} {'Grand Total:':<16} KES {grand_total:.2f}")
print(f"{'DISCOUNT':<10} {'':<5} {'':<16} KES {discount:.2f}")
print(f"{'TAX':<10} {'':<5} {'':<16} KES {tax:.2f}")
print(f"{'FINAL TOTAL':<10} {'':<5} {'':<15} KES {final_total:.2f}")
print(f"{'You were served by:'} {cashier.upper()}")
print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.')
