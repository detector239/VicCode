# 21. Write a program that reads a number and creates a set containing all of its digits.
user_input = ''

while user_input != 'e':
    try:
        user_input = input("Input a number to print its digits (Input 'e' to exit): ")
        if user_input == 'e':
            break
        else:
            user_input = int(user_input)
    except ValueError:
        print("Invalid input. Try again.")
        continue
        #print(board)
    set_num = set(str(user_input))
    print(set_num)


