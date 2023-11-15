
lst = [25, 1, 77.15, 0, "py", "2.50", "ten", False, "", True, 145, "10"]
sum = 0.0

for el in lst:
    try:
        print(el)
        el = float(el)
    except TypeError:
        print("This is not a number")
        continue
    except ValueError:
        print("This is not a number")
        continue

    if el != 0:
        div = 100/el
        if div>=4:
            sum += div
        else:
            print("The result from division is lower then 4")
    else:
        print("The number is 0 so we can't divide")

print("\n\nThe sum is: " + str(int(sum)))

