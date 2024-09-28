# Write a program that accepts a string as input. This line is the path to the file.
#     If the file exists:
#     1) Check whether it is possible to write to it
#     2) Delete that file and finish the job
#     If there is no file:
#     1) Create it
#     2) Write a string with Latin letters and any symbols that are not in ASCII table (diacritical, cyrillic etc.) in UTF-8 encoding
#     3) Read and display the contents in WINDOWS-1251 and UTF-8 encoding
#     4) Delete that file and finish the job
#     Use at least 2 functions to configure actions when file exists and when not.

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

