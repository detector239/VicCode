import os
from time import sleep

time = int(input("After how many seconds you want to shut down the computer? \n> "))
time = time-1

print(time)
for i in range(time):
    sleep(0.9)
    time = time-1
    print(time)

os.system("shutdown /s /t 1")


