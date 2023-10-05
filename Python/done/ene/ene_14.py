# 14. Given two lists of numbers, ln1, ln2, constructed before your code, print all elements from ln1 that also appear in ln2.
# ln1 = 5 6 7 9
# ln2 = 7 2 5 9
# Output:
# 5 7 9

ln1 = [5, 6, 7, 9]
ln2 = [7, 2, 5, 9]
ln3 = []

for i in ln1:
    if i in ln2:
        ln3.append(i)

print(ln3)
# set_1 = set(ln1)
# set_2 = set(ln2)

# print(set_1.intersection(set_2))


