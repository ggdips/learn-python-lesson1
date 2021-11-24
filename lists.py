#!/usr/bin/python3.9

phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
print(phones)

count = len(phones)
print(count)

phones.append("iPhone 12")
print(phones)

print(phones.count("iPhone 12"))

print(phones[-1])

print(phones[0:-1])

print(phones[:3])

print(phones[3:])

print(phones.index("iPhone 12"))

phones.sort()
print(phones.index("iPhone 12"))
print(phones)

print("Samsung Galaxy S21" in phones)

del phones[1]
print(phones)


phones.remove("iPhone 12")
print(phones)
