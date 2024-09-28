    # Write a program that accepts a string separated by spaces. For example: one 2 3 zero. Print the first and the last element and the total number of unique elements.

    # -> one 2 3 zero
    # one zero 4
    # -> ten 5 ten 100
    # ten 100 3
    # -> ten ten ten ten
    # ten ten 1

s = input("input characters divided by spaces: ")

lst = s.split(" ")

first = lst[0]
last = lst[-1]

print(first, last, len(set(lst)))
