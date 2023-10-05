import os



template_file = open("template.txt", "r")
template = template_file.read()



destinatarii_file = open("destinatari.txt", "r")
destinatarii = destinatarii_file.readlines()

for destinatar in (destinatarii):
    invitatie = template.replace("<nume>", destinatar.replace("п»ї", "").replace("\n", "").title()).replace("п»ї", "")
    print(invitatie)
    print("------------------------------------")

#num_name = len(name)----------------------
#num_name = str(num_name)

# with open("felicitare/template.txt", "r") as template:
#     name_place = template.read()


# name.reverse()

# for i in (num_name):
#     name.reverse()
#    person_name = name[i]
#    person_name = person_name.translate({ord(l): None for l in 'пЇ»їП'})
#     name_place = name_place.replace("<nume>,", person_name.title() + ",")
#     print(name_place.translate({ord(l): None for l in 'п»їПЇ'}))
#     name.reverse()
#     name.pop()



