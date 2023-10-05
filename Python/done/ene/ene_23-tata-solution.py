#23.Write a program that reads a sentence from standard input and counts how many times each letter appears in the sentence.
#The program should respect the output style presented in the sample.
#Sample Input:
#It's tea time
#Sample Output:
#I :  1
#t :  3
#' :  1
#s :  1
#  :  2
#e :  2
#a :  1
#i :  1
#m :  1


#=== Solution 1 - Is simple, but the output is not as required

a = "It's tea time"    # Sample input
# a = input("Input a string to count used letters in it: ")
for c in set(a):
    print(f"{c} :  {a.count(c)}")

#=== Solution 2 - The output is as required

a = "It's tea time"    # Sample input
s = set(a)    # Create a set of unique letters. It is required to avoid letters duplication.
for c in a:
    if c in s:
        print(f"{c} :  {a.count(c)}")
        s.remove(c)

