import re

text = input("Enter the time: ")

# regex = re.fullmatch(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', text) 
# regex = re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text) 
regex = re.fullmatch(r'\d{4}-[0-1]\d-[0-3]\d [0-2]\d:[0-5]\d:[0-5]\d', text) 

if regex:
    print("Well done!")
else:
    print("You did something wrong")
