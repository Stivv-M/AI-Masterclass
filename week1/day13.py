def greet(name):
    print('hello', name)


greet('Ruth')
print('\n')


def greet(name):
    print("Hello", name)


greet('Rose')
print('\n')


def add(a, b):
    return a + b


result = add(7, 3)
print(result)
print('\n')


def multiply(a, b, c):
    return a*b*c


total = multiply(2, 3, 4) + 100
print(total)

print('\n')


def divide(c, g):
    return c/g


finaly = divide(8, 2)
print(finaly)
print("\n")


def checkprice(price):
    if price > 100:
        return 'expensive'
    else:
        return 'affordable'


v = checkprice(99)
print(v)
print("\n")


def price(cost):
    if cost >= 290:
        return 'sell'
    else:
        return 'dont sell'


final = price(290)
print(final)
print('\n')


def calculate_price(quantity, price):
    return quantity*price


total = calculate_price(300, 20)
if total >= 1000:
    print("sell 3 at price of 2")
else:
    ('sell 1 at price of 1')
print("\n")


def total_sum(quantity, price):
    return quantity*price


z = total_sum(12, 10) + 10
if z >= 900:
    print('buy two')
else:
    print('buy as many as possible')
print('\n')


def get_discount(price):
    if price > 1000:
        return 'give a biro pen'
    else:
        return 'nothing'


discount = get_discount(1980)
print(discount)
print('\n')


def get_discount(price):
    if price >= 1000:
        return 100
    else:
        return 0


price = 1200
discount = get_discount(price)

final_price = price - discount

print(final_price)


def get_discount(price):
    if price >= 1000:
        return 100
    else:
        return 0


def final_price(price):
    discount = get_discount(price)
    return price - discount


result = final_price(1200)

print(result)


def add_tax(price):
    return price + 20


def final_price(price):
    tax = add_tax(price)
    return tax


result = final_price(100)

print(result)
print('\n')


def calculate_total(price, quantity):
    return price * quantity


print('\n')


def calc_total(price, quantity):
    return price * quantity


def calc_discount(total):
    if total >= 1000:
        return total * 0.10
    elif total >= 500:
        return total * 0.05
    else:
        return 0


total = calc_total(400, 2)
discount = calc_discount(total)
final_price = total - discount
print(final_price)
print('\n')
