
# 2.Write a program that request user to input 5 numbers, divide the numbers in two lists one for odd numbers and one for even numbers.

from numpy import average


num1 = input("Write number 1:\n> ")
num2 = input("Write number 2:\n> ")
num3 = input("Write number 3:\n> ")
num4 = input("Write number 4:\n> ")
num5 = input("Write number 5:\n> ")
numl = [num1, num2, num3, num4, num5]
numlo = []
numle = []

for i in numl:
    if int(i) % 2 == 0:
        numle.append(i)
    else:
        numlo.append(i)

print(numle)
print(numlo)

#  2.1 Check if there are numbers which are repeating and exclude them from the list.

numle = list(set(numle))
numlo = list(set(numlo))

print(numle)
print(numlo)

#  2.2 Reverse lists without using reverse function.

numo = []
nume = []

for num in numlo:
    numo.insert(-1, num)

for num in numle:
    nume.insert(-1, num)

print(nume)
print(numo)

#  2.3 Find out the average of set of integers from each list.

num = ""
for i in nume:
    if num == "":
        num = i
    else:
        num = average(num,i)
anume = num

num = ""
for i in numo:
    if num == "":
        num = int(i)
    else:
        num = average(num,int(i))
anumo = num


print(anume)
print(anumo)

print('### 2.4 Calculate the sum of the two numbers.')

print(anume + anumo)

# *Print the result of each step.



