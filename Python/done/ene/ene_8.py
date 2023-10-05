# 8. Write a program that reads a number, N, from standard input and prints all its divisors (except for 1 and N).
# Sample input: 12
# Sample output: 2 3 4 6


print("Input a number to find its divisors: ")
try:
    num = int(input("> "))
except ValueError:
    print("ERROR! You did not input a number. Quiting.")
    quit()

div = []

for i in range(2, num):
    num_div = num / i
    if num_div.is_integer():
        num_div = int(num_div)
        div.append(num_div)

num = str(num)
div = str(div)
print("...")
print(f"{num}'s divisors are: ", " ".join(div))
