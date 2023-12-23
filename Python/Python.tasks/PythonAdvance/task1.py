# Prepare yourself a text file. The file should be named 'task1_data.txt’.
#     Write a program that takes one character from the user.
#     Count how many times this character appears in the file.
char = input("Enter any character so i could count it in my text file: ")
counts = 0

file = open('task1_data.txt', 'r')
text = file.readlines()
file.close()

for l in text:
    counts += l.count(char)

print("The number is " + str(counts))


