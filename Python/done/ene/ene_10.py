# 10. Write a program that reads an integer, N,
# and outputs all even numbers less than N, including N if its even.

def verify(text):
    while True:
        try:
            user_input = input(text)
            user_input = int(user_input)
            print("\n")
        except ValueError:
            print("Invalid input! Try again.")
            continue
        if user_input <= 0:
            print("Invalid input. Try again.")
            continue
        else:
            break
    return user_input

print("Now you need to write a number to find the even and the lower numbers.")
num = verify("Write the number:\n>")
even_num = []

for i in range(num):
    r = num / 2
    if str(r).endswith(".0"):
        even_num.append(str(int(num)))
    num = num - 1

print("The numbers are:\n" + ", ".join(even_num) + ".")
