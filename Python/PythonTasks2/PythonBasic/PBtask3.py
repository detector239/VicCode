
s = 'this =- is , bad ! text #$%^123%^#&'

for l in s:
    if not l.isalpha():
        s = s.replace(l, " ")

print(s)
