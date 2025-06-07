# [1] Generați primul număr prim mai mare decât numărul natural dat n.
from math import sqrt

cont=True
while cont:
    # try:
    cont=False
    n=int(input("Enter a number: "))
    # except:
    #     print("You didn't enter a number. Try again:")
    #     cont=True

while not cont:
    n+=1
    if n<2:
        cont=False
    else:
        cont=True
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                cont=False
                break

