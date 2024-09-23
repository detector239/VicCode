
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2 = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]
matrix3 = [[], [], []]
number_of_columns = len(matrix1)


for num in range(number_of_columns):
    for el in matrix1[num]:
        matrix3[num].append(el*(matrix2[matrix1[num].index(el)][num]))

print(f"{matrix1} x {matrix2} = {matrix3}")




