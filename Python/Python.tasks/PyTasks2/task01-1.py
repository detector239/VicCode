# Task v1.
# Ask user to input 5 words.

text = input("Input 5 words: ")

# Add words to a list.

lst = text.split(" ")

# Output the list.

print(lst)

# Convert words to uppercase.

for i in range(len(lst)):
    lst[i] = lst[i].upper()

# Output the result list.

print(lst)






