from os import system

n = input("Enter number: ")
n = int(n)
m = 10

for i in range(m + 1):
    print( n, "x", i, "=", i*n)

system("pause")


