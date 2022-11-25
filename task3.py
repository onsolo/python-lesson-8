# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

from random import randint

size = 5
matrix = [0] * size

for i in range(len(matrix)):
    matrix[i] = list(randint(10, 30) for x in range(30))

all_days_temp = []
for row in matrix:
    for i in row:
        all_days_temp.append(i)

periods_temp_sum = []
for i in range(len(all_days_temp) - 7):
    periods_temp_sum.append(sum(all_days_temp[i: i+7]))

index_max_period = periods_temp_sum.index(max(periods_temp_sum))
index_min_period = periods_temp_sum.index(min(periods_temp_sum))


def get_date(index):
    month = index // 30
    print(f'day: {(index + 1) - month * 30}, month: {month + 5}')


print('Самый жаркий период: ')
for i in range(0, 6):
    get_date(index_max_period + i)

print('Самый холодный период: ')
for i in range(0, 6):
    get_date(index_min_period + i)
