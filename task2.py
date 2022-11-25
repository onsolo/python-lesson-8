# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint

matrix_size = 5
matrix = [0] * matrix_size

for i in range(len(matrix)):
    matrix[i] = list(randint(1, 10) for x in range(5))


matrix_main_diagonal_sum = 0
for i in range(matrix_size):
    for k in range(matrix_size):
        if i == k:
            matrix_main_diagonal_sum += matrix[i][k]

indexes = []
for i in matrix:
    if sum(i) > matrix_main_diagonal_sum:
        indexes.append(matrix.index(i))

print(f'Строки, сумма которых превосходит сумму главной диагонали: {indexes}')