# 6. Write a program that reads an integer number from standard input and computes the sum of its digits.

num = input("Enter your number: ")
result = 0


for ch in num:
    result += int(ch)
print(result)

