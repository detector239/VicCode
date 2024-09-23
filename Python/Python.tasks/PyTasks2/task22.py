# 22. Write a program that computes the total weight of all items in a shopping bag.
# The program will read N (the number of items) and then it will read two lines for each item.
# The first line represents the item name and the second represents its weight.
# The program will output a dictionary containing the total weight for each item.
# Sample Input:
# 4
# coffee
# 500
# sugar
# 1000
# coffee
# 500
# milk
# 1500
# Sample Output:
# {'coffee': 1000, 'sugar': 1000, 'milk': 1500}


num = int(input("Enter your number of items: "))

print("Enter your items: ")

input_ = []
for _ in range(num*2):
    line = input()
    input_.append(line)


items = dict()

for i in range(len(input_)):
    try:
        int(input_[i])
    except ValueError:
        items[input_[i]] = 0


for i in range(num*2):
    try:
        int(input_[i])
    except ValueError:
        items[input_[i]] += int(input_[i+1])

print(items)


