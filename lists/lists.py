# create empty lists
empty_1 = []
empty_2 = list()

# Create a list with some items
fruits = ["apple", "banana", "orange",]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# reassign value at index
fruits = ["apple", "banana", "orange",]
fruits[1] = "plum"
print(fruits)

#get the number of items
num_of_fruits = len(fruits)
print(num_of_fruits)

#remove last element
removed_fruit = fruits.pop()
print(f'I removed {removed_fruit}')

# add a new fruit to list
fruits.append("pineapple")
print(fruits)






