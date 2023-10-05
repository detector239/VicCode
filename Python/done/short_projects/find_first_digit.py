from operator import mod


print("Input a number to find its first digit: ")
try:
    num = float(input("> "))
except ValueError:
    print("ERROR! You did not input a number. Quiting.")
    quit()


while num <= -10 or 10 <= num:
    num = num / 10

num = int(num)
print("...")
print("The first digit is: " + str(num) + "\n ")
