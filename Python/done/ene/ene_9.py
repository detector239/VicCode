# 9. Write a program that reads a string from standard input and prints each character
#    in the string, except spaces, using the for instruction.

print("From your text we will show you all the characters without spaces.")
print("Write the text here:")
text = input("> ")

text = text.replace(" ", "")

print("The characters are:\n" + ", ".join(list(text))+".")