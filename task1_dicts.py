#!/usr/bin/python3.9
from pprint import pprint

mydict ={
    "city": "Moscow",
    "temperature": "20"
}

print(mydict["city"])
mydict["temperature"] = int(mydict["temperature"]) - 5
print(mydict)

print(mydict.get("country"))
print(mydict.get("country","Russia"))

mydict["country"] = "Russia"
mydict["date"] = "27.05.2019"
print(len(mydict))
