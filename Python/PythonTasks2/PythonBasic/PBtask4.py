
s = input("input characters divided by spaces: ")

lst = s.split(" ")

first = lst[0]
last = lst[-1]

print(first, last, len(set(lst)))
