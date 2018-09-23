# https://docs.google.com/document/d/1BrDhg6EadRNwBKASQ7I96rhPHmJBaqzVNCtCszqADSk/edit?usp=sharing

# Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))

# Вывод матриц
# print(matrix)
# print(matrix_t)

for line in matrix:
    print(line)

# print(sum(line))
print('*' * 25)
for line in matrix_t:
    print(list(line))

