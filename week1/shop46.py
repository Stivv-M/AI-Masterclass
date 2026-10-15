products = {"1001": {"name": "Rice", "price": 200},"1002": {"name": "Sugar", "price": 180},"1003": {"name": "Milk", "price": 70}}

quantities = {}

while True:
    barcode = input("Scan barcode (or type done): ")

    if barcode == "done":
        break

    if barcode in products:
        product_name = products[barcode]["name"]

        if product_name in quantities:
            quantities[product_name] = quantities[product_name] + 1
        else:
            quantities[product_name] = 1

        print(product_name, "Quantity:", quantities[product_name])

    else:
        print("Product not found!")
grand_total = 0

for product_name in quantities:
    quantity = quantities[product_name]

    for barcode in products:
        if products[barcode]["name"] == product_name:
            price = products[barcode]["price"]
            break

    total = quantity * price
    grand_total = grand_total + total

    print(product_name, quantity, "KES", total)

print("Grand Total: KES", grand_total)
print("Final quantities:", quantities)