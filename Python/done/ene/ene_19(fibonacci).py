
print("Going to calculate the Fibonacci numbers.")
print("How many numbers would you like to calculate?")
try:
    m = int(input("Input a number: "))
except ValueError:
    print("ERROR! You did not input a number. Quiting.")
    quit()

# Setting initial numbers
n1 = 0
print(n1)
n2 = 1
print(n2)

# Calculating the rest of numbers
for i in range(m-2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

# NOTA = 10
