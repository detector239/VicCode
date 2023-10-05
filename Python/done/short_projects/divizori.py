

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


num = verify("Write a number to find it's divizors:\n> ")
divizors = []

for i in range(1, num+1):
    x = num/i
    if x == int(x):
        divizors.append(i)

print(divizors)
