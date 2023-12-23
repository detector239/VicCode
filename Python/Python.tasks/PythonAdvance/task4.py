# Write a program that uses the list:
#     lst = [25, 1, 77.15, 0, "py", "2.50", "ten", False, "", True, 145, "10"]

#     The program should divide number 100 into every element of the list.
#     The program should count the sum of all division results greater or equal (>=) 4.

#     sum = 0, 100/10=10 -> 10>=4 -> sum=0+10=10
#     sum = 10, 100/100=1 -> 1<4 -> sum = 10
#     sum = 10, 100/5=20 -> 20>=4 -> sum =10+20=30

#     Catch the error of converting the string to the integer and the division by 0 error.
#     Each error must be caught in one except block and the corresponding message should be displayed which is transmitted in the error object.


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

