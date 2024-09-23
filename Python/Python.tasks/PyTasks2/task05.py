# 5.  Write a program that finds the roots of a second degree equation. Considering the equation of the form ax^2+bx+c,
# the program will read a, b, and c from standard input. The program will output the two solutions for when the equation equals 0.
# Sample input: 1  6  5
# Sample output: -5.0   -1.0
from math import sqrt


txt = input("Input your a, b, c: ")
lst = txt.split(" ")
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
delta = b**2-4*a*c
if delta < 0:
    x1 = (sqrt(delta)-b)/2*a
    x2 = -(sqrt(delta)+b)/2*a
    print(x1, x2)
else:
    print("The ecuation has no solution.")

