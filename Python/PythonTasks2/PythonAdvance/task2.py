import os

# while True:
#     try:
    #     break
    # except IOError:
    #     print('Somthing went wrong.\nWe coldn\'t open the first file.')
    #     quit()



# while True:
# filetext2 = None
    # try:
    #     break
    # except IOError:
    #     print('Somthing went wrong. We coldn\'t open the second file.')
    #     quit()
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
