

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



num = verify("Write a number:\n> ")+1


for i1 in range(num):
    for i2 in range(num):
        for i3 in range(num):
            print(i1, i2, i3)
            # print(i1, i2, i3)

