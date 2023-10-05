# Write a program that reads a number from the input and checks if the number is even.
# If true, then the program prints "EVEN", otherwise it prints "ODD".

def verify(a):
    try:
        nr1 = int(input(a))
    except ValueError:
        print("ERROR! You didn't input number. Quiting.")
        quit()
    return nr1

a = verify("Input a number: ")

if a % 2 == 0:
    print("The number "+ str(a) +" is even. ")
else:
    print("The number " + str(a) + " is odd. ")
