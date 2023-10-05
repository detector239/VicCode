import random

def verify(a):
    nr1 = ''
    while not nr1.isdigit():
        # try:
        nr1 = input(a)
        # except ValueError:
        if not nr1.isdigit():
            print("Please input a valid natural number.")

    return int(nr1)



def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = verify(f"Guess a number between 1 and {x}: ")
        if guess < random_number:
            print(f'Sorry. The number {guess} is too Low.')
        elif guess > random_number:
            print(f'Sorry. The number {guess} is too High.')
    print(f'Congrats!! You have guessed the number {random_number} correctly!!!')

guess(1000)
