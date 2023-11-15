


char = input("Enter any character so i cloud count it in my text file: ")
counts = 0

file = open('task1_data.txt', 'r')
text = file.readlines()
file.close()

for l in text:
    counts += l.count(char)

print("The number is " + str(counts))


