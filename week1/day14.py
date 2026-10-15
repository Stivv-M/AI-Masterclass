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


price = 2000
quantity = 3

total = calculate_cost(price, quantity)
discount = calculate_discount(total)
tax = calculate_tax(total)

final_price = total - discount + tax

print(final_price)
print('\n')


def calculate_price(price, quantity):
    return price*quantity


def calculate_discount(total):
    if total >= 3000:
        return total * 0.1
    else:
        return 0


def calculate_tax(total):
    return total * 0.16


total = calculate_cost(600, 6)
discount = calculate_discount(total)
tax = calculate_tax(total)

final_price = total-discount+tax
print(final_price)
print('\n')


def calculate_price(quantity, price):
    return price * quantity


def calculate_discount(total):
    return total * 0.10


quantity = 5
price = 700
total = calculate_price(quantity, price)
discount = calculate_discount(total)
final_price = total - discount
print(final_price)
print('\n')


def add(a, b):
    return a + b


result = add(10)
