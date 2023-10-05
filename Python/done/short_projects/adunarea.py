
print("Sum the numbers!")
try:
    n = int(input("    From: "))
    m = int(input("    To: "))
except ValueError:
    print("You did not input a number.")
    quit()

fromA = n
toB = m + 1

if n > m:
    fromA = m
    toB = n + 1

z = 0
for i in range(fromA, toB, 1):
    z = z + i

print("The answer is: " + str(z))
