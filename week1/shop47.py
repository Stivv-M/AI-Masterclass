products = {"1001": {"name": "Rice", "price": 200},"1002": {"name": "Sugar", "price": 180},"1003": {"name": "Milk", "price": 70}}

quantities = {}
grand_total = 0
while True:
    barcode = input("Scan barcode (or type done): ")

    if barcode == "done":
        break

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