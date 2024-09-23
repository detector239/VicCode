# 20. The decimal number, 585 = 1001001001 (binary), is palindromic in both bases. Write a program
# that reads a number and checks if its palindromic in both bases.

num = input("Enter your number: ")
lsti = rlsti = list(num)
lstb = rlstb = list(bin(int(num)))

del lstb[0:2]
rlstb.reverse()
rlsti.reverse()

if lsti == rlsti and lstb == rlstb:
    print(f"The number {num} is palindromic in base 10 and in base 2.")
else:
    print(f"The number {num} is not palindromic in base 10 and in base 2.")



