import random

def play():
    user = ''
    while user != 'e':
        user = input("What's your choise? 'r' for rock, 'p' for paper, 's' for scissors or 'e' to exit from game\n> ").lower()
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print('It\'s a tie.')
        elif is_win(user, computer):
            print('You won!')
        elif is_win(computer, user):
            print('You lose.')
        elif user == 'e':
            continue
        else:
            print('Invalid input. Try again.')


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True


# print(play())
play()