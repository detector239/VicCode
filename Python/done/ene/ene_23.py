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

a = "It's tea time"
b = {}
z = []

for i in (a):
    z.append(i)

b.update(z)

for x in b:
    c = a.count(x)
    print(x, ':', c)


