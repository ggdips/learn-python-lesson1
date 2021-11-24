#!/usr/bin/python3.9
from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
phones = ["iPhone 12 Pro", "Samsung Galaxy S21", "Xiaomi Mi11"]
stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]


print(product)
print(len(product))

product["memory"] = 64
print(product)

product["memory"] = 256
print(product)

print(product["price"])
print(product.get("discount","0"))

del product["stock"]
print(product)

product["recomended"] = phones
pprint(product)
pprint(product["recomended"])

pprint(stock[0]["recomended"][0])
