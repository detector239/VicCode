# 9. Write a program that reads a string from standard input and prints each character in the string, except spaces, using the for instruction.


txt = input("Enter your string: ")

for ch in txt:
    if ch != " ":
        print(ch)



