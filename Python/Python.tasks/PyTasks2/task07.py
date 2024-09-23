# 7. Write a program that reads a number, N, from standard input and computes the sum of the first N natural numbers (N included).
# Sample input: 3
# Sample output: 6

n = int(input("Enter your number: "))
res = 0

for i in range(1, n+1):
    res += i
print(res)
