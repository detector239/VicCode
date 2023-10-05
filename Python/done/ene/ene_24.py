# 24.Write a program that creates a statistic about the number of vowels appearing in a sentence.
# The program reads a sentence from the standard input and outputs the corresponding dictionary.
# Count uppercase and lowercase vowels together.
# Sample Input:
# Mary learns programming.
# Sample Output:
# {'a': 3, 'e': 1, 'o': 1, 'i': 1}

text = input("Write some text to count the vowels:\n> ")
vo_list = ["a", "e", "i", "o", "u"]
vo_dic = {}

for i in text:
    if i.lower() in vo_list:
        if i.lower() in vo_dic:
            vo_dic[i.lower()] = vo_dic[i.lower()] + 1
        else:
            vo_dic[i.lower()] = 1

print(vo_dic)