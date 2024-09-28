# 11. Write a program that reads a  and displays a corresponding triangle, as shown in the sample input/output.
# Sample Input: 5
# Sample Output:
# *
# **
# ***
# ****
# *****

try:
    num = int(input("Enter your number: "))
except:
    print("")
    exit(1)


for i in range(1, num+1):
    print("*" * i)