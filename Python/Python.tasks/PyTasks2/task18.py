# 18. Write a program that reads an integer number and outputs a list containing its divisors (except 1 and the number itself) in ascending order.
# If the number is prime, an empty list will be printed.

from math import sqrt

try:
    N = int(input("Enter your number to find it's divisors: "))
except:
    print("")
    exit(1)

divisors = set()

for i in range(1, int(sqrt(N))+1):
    if N/i == N//i:
        divisors.add(i)
        divisors.add(int(N/i))
divisors.remove(1)
divisors.remove(N)
print(sorted(divisors))