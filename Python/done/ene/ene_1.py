# Write a program that reads two numbers, a,b, and outputs the one which is greater.
# If the numbers are equal, then the program should print the message "the numbers are equal".

def verify(a):
    try:
        nr1 = int(input(a))
    except ValueError:
        print("ERROR! You didn't input number. Quiting.")
        quit()
    return nr1


a = verify("Input number a: ")
b = verify("Input number b: ")

if a > b:
    print("The number a is greater.")

elif b > a:
    print("The number b is greater. ")

elif a == b:
    print("The numbers are equal.")

