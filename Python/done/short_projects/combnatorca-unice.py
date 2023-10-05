

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


num_list = ["Tata", "Mama", "Daniela", "Victor", "Bunelul", "Bunica"]
num = verify(f"Write a number less then {len(num_list)}:\n> ")+1

if num <= len(num_list):
    for i1 in range(0, num):
        for i2 in range(i1+1, num):
            for i3 in range(i2+1, num):
                x = num_list[i1], num_list[i2], num_list[i3]
                if len(set(x)) == 3:
                    print(", ".join(set(x)))
                # print(i1, i2, i3)
else:
    print("Number is too high!")

