products = [
{"name": "apple", "price": 3.5, "stock": 12,"category":"fruits"},
{"name": "bread", "price": 4.2, "stock": 4,"category":"bakery"},
{"name": "coffee", "price": 29.99, "stock": 2,"category":"drinks"},
{"name": "milk", "price": 6.5, "stock": 9,"category":"dairy"},
{"name": "Coca-Cola", "price": 14.5, "stock": 19,"category":"drinks"},
{"name": "pear", "price": 4.5, "stock": 29,"category":"fruits"},
]
print(f"Total value: {sum(product['price'] * product['stock'] for product in products)}")
products.sort(key=lambda product:product["price"])
print("By value:")
for product in products:
    print(f"-{product['name']} {product['price']}")
print("Low stock:",end=" ")
for product in products:
    if product["stock"]<5:
        print(f"{product['name']} ({product['stock']})",end=", ")

print(end="\n")
print(f"Average price: {sum(product['price'] for product in products)/len(products)}")

products.sort(key=lambda product:product["price"],reverse=True)
print(f"Most expensive: {products[0]['name']}")

categoryValue={}

for product in products:
    category=product["category"]
    value=product["price"]*product["stock"]

    if category not in categoryValue:
        categoryValue[category]=0
    categoryValue[category]+=value

print("By category:")
for category,value in categoryValue.items():
    print(f"-{category}: {value}")