import datetime

while True:
    n = input("Input your birth year (press q to quit): ")
    if n == "q":
        print("You pressed q")
        break
    elif n.isnumeric():
        n = int(n)
        f = datetime.datetime.now()
        f = f.year
        if n > f:
            print("Not valid year.")
        else:
            m = f - n
            m = str(m)
            print("You are " + m + " years old.")
    else:
        print("Not valid year.")


