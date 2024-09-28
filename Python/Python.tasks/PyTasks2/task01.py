# 1.  Write a program that reads two numbers, a,b, and outputs the one which is greater. If the
# numbers are equal, then the program should print the message "the numbers are equal".

a = input("Input the first number: ")
b = input("Input the second number: ")


match a, b:
    case a > b:
        print(a)
    case a = b:
        print("the numbers are equal")
    case a < b:
        print(b)

