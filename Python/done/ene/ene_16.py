# 16. Write a program that reads an integer number and outputs its reverse.
user_input = ''

while user_input != 'e':
    while True:
        try:
            user_input = input("Input a number to find his revers (Input 'e' to exit): ")
            if user_input == 'e':
                break
            else:
                user_input = int(user_input)
        except ValueError:
            print("Invalid input. Try again.")
            continue
            #print(board)
        break
    if user_input == 'e':
        break
    else:
        revers_num = []
        for i in str(user_input):
            revers_num.insert(0, i)
        print(f"The revers number is '" + "".join(revers_num) + "'")


