# 13. Write a program that reads a number, N, and then reads N lines representing words.
# The program will add each word to a list which will be printed after reading all words.
# Sample Input:
# 5
# the
# quick
# turtle
# steals
# lettuce
# Sample Output:
# ['the', 'quick', 'turtle', 'steals', 'lettuce']

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

num = verify("Write a number\n> ")
words = []

for i in range(num):
    word = input(f"Write the word {i + 1}: ")
    words.append(word)

print(words)
