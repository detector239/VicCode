# 13. Write a program that reads a number, N, and then reads N lines representing words. The program will add each word to a list
# which will be printed after reading all words.
# Sample Input:
# 5
# the
# quick
# turtle
# steals
# lettuce
# Sample Output:
# ['the', 'quick', 'turtle', 'steals', 'lettuce']

try:
    N = int(input("Enter how many wards you want to introduce: "))
except:
    print("You didn't input a number. Quitting...")
    exit(1)