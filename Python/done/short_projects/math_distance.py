import sys

num = int(input("Write the distance number:\n> "))

while -sys.maxsize <= num and num <= sys.maxsize:
    num = int(num)*10
    print(num)

# int() has

