# 23.Write a program that reads a sentence from standard input and counts how many times each letter appears in the sentence.
# The program should respect the output style presented in the sample.
# Sample Input:
# It's tea time
# Sample Output:
# I :  1
# t :  3
# ' :  1
# s :  1
#   :  2
# e :  2
# a :  1
# i :  1
# m :  1

# VAR I
txt = input("Enter your text: ")
dct = dict()

for ch in txt:
    if ch in dct:
        dct[ch] += 1
    else:
        dct[ch] = 1

for key in dct:
    print(f"{key} : {dct[key]}")



