#     Write a program that accepts a string in the format:
#     “php = Rasmus Lerdorf; perl = Larry Wall; python = Guido van Rossum”
#     Build a dictionary where the keys are the values to the left of "=" and the values are to the right of "=". Delimiter is ";".
#     Invert the dictionary so that values become keys and keys become values. 
#     Print the resulting dictionaries in sorted by key form, separated by fifty symbols “#”. It is guaranteed that all values and keys are unique.

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

