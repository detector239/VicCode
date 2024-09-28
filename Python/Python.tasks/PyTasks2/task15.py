# 15.Given a list of numbers, ln1, constructed before your code, print a new list which counts how many
# times each digit appears throughout all of the numbers from list ln1.
# Sample Input: 123 45 67 89 102
# Sample Output: [1, 2, 2, 1, 1, 1, 1, 1, 1, 1]


txt = input("Enter your numbers(divided by spaces):")
ln1 = txt.split(" ")
ln2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for el in ln1:
    for ch in el:
        ln2[int(ch)] += 1

print(ln2)
