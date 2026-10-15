prices = {"Rice": 200, "Sugar": 180, "Milk": 70, "Bread": 110}
quantities = {}
totals = {}
grand_total = 0
item_count = 0


def calculation_discount(total):
    if total >= 5000:
        return total * 0.1
    elif total >= 3000:
        return total * 0.05
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


print("-----------------------------------------")
print('SALES RECEIPT\n')
for product in prices:
    quantity = int(input(f"{product}: "))
    quantities[product] = quantity
    total = prices[product] * quantity
    totals[product] = total
    grand_total = grand_total + total
    item_count = item_count + quantity
    discount = calculation_discount(grand_total)
    tax = calculate_tax(grand_total)
    final_total = grand_total - discount + tax
print('\n-----------------------------------------')
print(f"{'PRODUCT':<10} {'QTY':<5} {'PRICES':<18} {'TOTAL'}\n")
for product in prices:
    print(
        f"{product:<10} {quantities[product]:<5} KES{prices[product]:<15.2f} KES{totals[product]:.2f}")
print()

print(f"{'Item_Count:'} {item_count}{'':<8} {'Grand_total:'} {'':<5} KES{grand_total:.2f}")
print(f"{'Discount'} {'':<30} KES{discount:.2f}")
print(f"{'Tax:'} {'':<35} KES{tax:.2f}")
print(f"{'Final Total:'} {'':<26} KES{final_total:.2f}")
