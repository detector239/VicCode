# 8. Write a program that reads a number, N, from standard input and prints all its divisors (except for 1 and N).
# Sample input: 12
# Sample output: 2 3 4 6
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





