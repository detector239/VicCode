import random

print("We have a bascket with grains.")
print("We need to separate the rice from others grains.")

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


types_num = verify("How many types of grains want to be mixed in the bascket?\n> ")
rice_inum = verify("What is the indentification number for buckwheat?\n> ")
grains_num = verify("How many thousends grains you want to be in the bascket\n> ")
grains_num = grains_num * 1000
bascket = []
rice_bascket = []


for i in range(grains_num+1):
    x = random.randint(1, types_num)
    bascket.append(x)

for i in range(len(bascket)):
    if bascket[i] == rice_inum:
        rice_bascket.append(i)


user_answer = "2"

while user_answer != "no":
    user_answer = input("Do you want to see all rice grains?('yes' or 'no')\n> ")
    if user_answer.lower() == "yes":
        # print(", ".join(rice_bascket)+".")
        print(rice_bascket)
        break
    elif user_answer.lower() == "no":
        print("Ok. Bye!")
        continue
    else:
        print("Invalid input! Try again!")

