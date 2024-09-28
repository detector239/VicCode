# 12.Write a program that reads an integer number, N, and outputs True if N is a prime number, and False otherwise.
# A number is prime if its only divisors are 1 and N itself. You can use the break instruction to stop the loop
# early if the number is not prime.

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







