

text = input("Enter any text: ")
original_text = text

characters = len(text)
spaces = text.count(' ')
letter_number = characters - spaces
capitalize = text.capitalize()
title = text.title()
skyperemoved = text.removesuffix('skype')
index = text.index()
expendedtabs = text.expandtabs()


if original_text.endswith("x"):
    print("The text ends with 'x'. ")

if original_text.istitle():
    print("Text is title. ")

if original_text.isspace():
    print("The text have only spaces. ")

if original_text.isnumeric():
    print("The text is numeric.")

if "asd" in text.lower():
    print("Found 'asd' in given text.")

print(capitalize)
print(title)
print(index)
print(expendedtabs)
print(str(letter_number) + " characters.")
print(str(spaces) + " spaces.")
print("The upper text is:", text.upper())
print("The lower text is:", text.lower())

if original_text.islower:
    print("The text is lower.")
elif original_text.isupper:
    print("The text is upper.")
else:
    print('This text has lower and upper letters.')
