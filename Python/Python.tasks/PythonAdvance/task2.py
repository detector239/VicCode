# Prepare two files: task2_data_1.txt task2_data_2.txt
#     Append the contents of the second file to the first, previously making 3 line feeds (\n).
#     Rename the first file to task2_data_all.txt
#     Delete the second file.


import os
filetext1 = open('task2_data1.txt', "a")
filetext2 = open('task2_data2.txt', "r")

text = filetext2.readlines()

filetext1.write('\n\n\n')
for line in text:
    filetext1.write(line)


filetext1.close()
os.rename(filetext1.name, 'task2_data_all.txt')

filetext2.close()
os.remove(filetext2.name)
