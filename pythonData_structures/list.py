
# list

fruits = ["apple", "banana", "grapes"]
print(fruits)

fruits[1] = "blueberry"
print(fruits)

fruits = ["orange", "peaches", "grape"]

# adding kiwi to the fruits
fruits.append("kiwi")
print(fruits)

# apple added before peaches
fruits.insert(1, "apple")
print(fruits)

fruits.remove("kiwi")
print(fruits)

# sorts fruits in an ascending order
fruits.sort()
print(fruits)

# descending order set
fruits.sort(reverse=True)
print(fruits)



