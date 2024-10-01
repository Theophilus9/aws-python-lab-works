fruits = ["apple", "mango", "banana", "pear", "pineapple"]

counter = 10
while (counter > 0):
    print(fruits[counter%5])
    counter -= 1

for fruit in fruits:
    print("{} is a type of fruit".format(fruit))
    