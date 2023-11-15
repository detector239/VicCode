s = "php = Rasmus Lerdorf; perl = Larry Wall; python = Guido van Rossum"

dict1 = {}
dict2 = {}


lst = s.split(";")

for i in range(len(lst)):
    el = lst[i]
    indx = int(el.find("="))
    name = el[0 : indx-1].replace(' ', '')
    creator = el[indx+2 : -1]
    dict1[f'tool{i+1}'] = {'name' : name, 'creator' : creator}
    dict2[name] = creator

print(dict1)
print(dict2)

