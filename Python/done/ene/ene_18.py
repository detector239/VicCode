# 18. Write a program that reads an integer number and outputs a list containing its divisors
# (except 1 and the number itself) in ascending order.
#  If the number is in prime, an empty list will be printed.

def verify(text):
    while True:
        try:
            user_input = input(text)
            user_input = int(user_input)
        except ValueError:
            print("Invalid input! Try again.")
            continue
        if user_input <= 0:
            print("Invalid input. Try again.")
            continue
        else:
            break
    return user_input

num = verify("Write a number:\n> ")
div_list = []

for i in range(2, num-1):
    div = num / i
    if str(div).endswith(".0"):
        div_list.append(int(i))


print(div_list)

