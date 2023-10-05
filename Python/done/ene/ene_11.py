# 11. Write a program that reads a number and displays a corresponding triangle, as shown in the sample input/output.
# Sample Input:
# 5
# Sample Output:
# *
# **
# ***
# ****
# *****
import random

z = random.randint(1,100)
y = ""

for i in range(z):
    y = y + "*"
    print(y)

print(z)