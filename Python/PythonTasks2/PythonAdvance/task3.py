import os

def file_found(path):
    if os.access(path, os.W_OK):
        print('The file can be written')
    else:
        print('The file cann\'t be written')
    os.remove(path)
    quit()

def file_not_found(path):
    with open(path, 'w') as file:
        text = "The Hamangia culture is a Late Neolithic archaeological culture of Dobruja (Romania and Bulgaria) between the Danube and the Black Sea and untenia in the south. It is named after the site of Baia-Hamangia, discovered in 1952 along Golovita Lake.[1]"
        file.write(str(text.encode("utf8")))
    print(text.encode("utf8"))
    print(text.encode("windows-1251"))



'''
---------------------------------------------------------------------------------------------------------------------------------------------------
'''

path = input("Enter a file path: ")


if os.access(path, os.F_OK):
    print('File found')
    file_found(path)
else:
    print('File not found')
    file_not_found(path)

