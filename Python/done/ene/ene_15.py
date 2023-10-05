# 15. Given a list of numbers, ln1, constructedigits[0] before your codigits[0]e, print a new list which counts how many times each digits[0]igit appears throughout all of the numbers from list ln1.
# Sample Input:
# 123 45 67 89 102
# Sample Output:
# [1, 2, 2, 1, 1, 1, 1, 1, 1, 1]

ln1 = "123 45 67 89 102"
digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in (ln1):
    # print(i)
    if i.isnumeric():
        digits[int(i)] = digits[int(i)] + 1

print(digits)

