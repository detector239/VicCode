
import random


def computer_guess(l, x):
    low = l
    high = x
    guess = low
    feedback = ''
    while feedback != 'c':
        if low < high:
            guess = random.randint(low, high)
        else:
            guess = low
            break
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly!!')

ll = 1
xx = 10
print(f"Chose a number between {ll} and {xx}")
input("Press <Enter> to continue")
computer_guess(ll, xx)

