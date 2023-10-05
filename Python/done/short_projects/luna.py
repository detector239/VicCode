
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomber", "Novamber", "December"]
print("Now we print the list of months:")
print(months)
try:
    m = int(input("Input a number of month: "))
except ValueError:
    print("ERROR! You didn't input number. Quiting.")
    quit()

if 0 < m and m < 13:
    print(months[m - 1])
else:
    m = str(m)
    print("ERROR! Month "+ m + " doesn't exist. Quiting.")


months.remove(months[m - 1])
print("Now we print the list of months without the choosen month:")
print(months)
print("Now we sort the list of months:")
months.sort()
print(months)
print("Now we print the month from the sorted list:")
print(months[m - 1])
months.insert(m - 1, "Victor")
print(months)


print(months[2])
