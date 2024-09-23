# 4. Write a program that computes your grade for the Programming course:
# lab_grade = (test_1 + test_2)/2
# final_grade = 70% lab_grade + 30% exam_grade
#
# The input consists of three grades, for the first test, for the second test, and for the exam.
# If any of the lab grade or the exam grade are less than 5 the program will print: "failed". Otherwise, the program will print the final grade.
#
# Sample input: 4 10 8
# Sample output: 7.3

txt = input("Input your grades(this orde: test_1 test_2 exam_grade): ")

lst = txt.split(" ")

lab_grade = (int(lst[0]) + int(lst[1]))/2

final_grade = 70/100*lab_grade + 30/100*int(lst[2])

print(final_grade)
