# 4. Write a program that computes your grade for the Programming course:
# lab_grade = (test_1 + test_2)/2
# final_grade = 70% lab_grade + 30% exam_grade
# The input consists of three grades, for the first test, for the second test, and for the exam.
# If any of the lab grade or the exam grade are less than 5 the program will print: "failed". Otherwise, the program will print the final grade.
# Sample input: 4 10 8
# Sample output: 7.3




from cgi import test
from curses.ascii import isdigit


def verify(text):
    while True:
        try:
            user_input = input(text)
            user_input1 = user_input.replace(" ", "")
            user_input1 = int(user_input1)
        except ValueError:
            print("Invalid input! Try again.")
            continue
        if user_input1 <= 0:
            print("Invalid input. Try again.")
            continue
        else:
            break
    return str(user_input)

test = verify("Write your grades:\n> ").split()

lab_grade = (int(test[0]) + int(test[1]))/2
lab_grade70 = lab_grade / 100 * 70

exam_grade = int(test[2])
exam_grade30 = exam_grade / 100 * 30

final_grade = lab_grade70 + exam_grade30

print(round(final_grade, 2))