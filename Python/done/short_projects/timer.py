from playsound import playsound
import time

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


seconds = verify("Write how many seconds you want to wait:\n> ")

for i in range(1, seconds+1):
    print(f"{i} seconds")
    time.sleep(1)


playsound('audio.mp3')
input("Press Enter to continue...")
