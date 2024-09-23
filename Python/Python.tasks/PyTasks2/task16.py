# 16. Write a program that reads an integer number and outputs its reverse.
from typing import List, Any

num = list(input("Enter your number: "))
man = 0

for i in range(int(int(len(num))/2)):
    man = num[i]
    num[i] = num[-(i+1)]
    num[-(i+1)] = man
print(str(num))


