# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random
from statistics import mean

groups_count = 5
marks = [0] * groups_count

for i in range(len(marks)):
    marks[i] = list(random.randint(1, 5) for k in range(4))

avg_marks = []
for i in marks:
    avg_marks.append(mean(i))

print(f'Наилучший средний балл у группы №{avg_marks.index(max(avg_marks)) + 1}')

