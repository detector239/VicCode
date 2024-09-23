# 10. Write a program that reads an integer, N, and outputs all even numbers less than N,
# including N if its even.

N = int(input("Enter your number: "))

for i in range(N+1):
    if i % 2 == 0:
        print(i)
