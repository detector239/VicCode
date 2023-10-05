from os import linesep


readbook = []
book = open("carte.txt", "r")

readbook = book.readlines()
print(readbook)

for line in readbook:
    print(line)

book.close()