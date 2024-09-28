# 4.Write a program that creates a statistic about the number of vowels appearing in a sentence. The program reads a sentence from the standard input and outputs the corresponding dictionary. Count uppercase and lowercase vowels together.
# Sample Input:
# Mary learns programming.
# Sample Output:
# {'a': 3, 'e': 1, 'o': 1, 'i': 1}


txt = input("Enter your text: ").lower()
vowels = ["a", "e", "i", "o", "u"]
txt_vow = dict()

for ch in txt:
    if ch in vowels:
        if ch in txt_vow:
            txt_vow[ch] += 1
        else:
            txt_vow[ch] = 1
print(txt_vow)
