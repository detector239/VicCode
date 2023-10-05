from itertools import combinations_with_replacement as comb

subjects = int(input("How many subjects do you have?:\n> "))
qualification = float(input("What qualification do you expect?:\n> "))

x = comb((5, 6, 7, 8, 9, 10), subjects)

for i in x:
  avg = round(sum(i)/len(i), 2)
  if avg >= qualification:
    print(avg, ":", i)
