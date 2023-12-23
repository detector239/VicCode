# There is a string:
# s = 'this =- is , bad ! text #$%^123%^#&'
# Write a program that replaces all non-letters with spaces.

s = 'this =- is , bad ! text #$%^123%^#&'

for l in s:
    if not l.isalpha():
        s = s.replace(l, " ")

print(s)
