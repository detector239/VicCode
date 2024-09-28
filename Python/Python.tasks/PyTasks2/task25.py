# 25. Write a program that reads a matrix of 3 rows and 3 columns and outputs the elements of the main diagonal.
import re


print("Enter your matrix: ")

row1 = input().split(" | ")
row2 = input().split(" | ")
row3 = input().split(" | ")

lst = []
lst.extend(row1)
lst.extend(row2)
lst.extend(row3)

for i in range(0, 9, 4):
    print(lst[i])