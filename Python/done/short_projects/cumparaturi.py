
produse = [ ]


try:
    n = input("Ai cumparat azi ceva ('da' sau 'nu'):")
except ValueError:
    print("Puneti va rog 'da' sau 'nu'. ")
    n = input("Ai cumparat azi ceva ('da' sau 'nu'):")



if n == "nu":
    print("Atunci bine. La revedere!")
    quit()
x = 0

while n == "da":
    m = input("Ce ai cumparat: ")
    produse.append(m)

    try:
        z = input("Cat a costat, ce ai cumparat:")
        z = int(z)
    except ValueError:
        print("Puneti va rog un numar natural. ")

    if z.isnumeric:
        z = int(z)
        x = x + z

    q = input("Ai cumparat azi ceva ('da' sau 'nu'):")
    if q == "da":

    elif



x = str(x)

print("Iata ce ai cumparat:")
print(produse)
print("iata cat ai cheltuit:")
print(x)