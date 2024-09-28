# 3. Write the program that outputs the maximum out of 3 numbers read from standard input.
# Sample input: 2 4 1
# Sample output: 4



txt = input("Input 3 numbers: ")
lst = txt.split(" ")
max = lst[0]

for el in lst:
    if int(el) > max:
        max = int(el)

print(max)




