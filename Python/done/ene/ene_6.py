# 6. Write a program that reads an integer number from standard input and computes the sum of its digits.

try:
    a = int(input("Write a number:"))
except ValueError:
    print("You didn't input a number. Quiting...")
    quit()

sum_digit = 0

for i in str(a):
    sum_digit += int(i)

print("The sum of digits is: ", sum_digit)
