import random

# Генерация случайных размеров матрицы от 4 до 8
height = random.randint(4, 8)
width = random.randint(4, 8)

# Значения для заполнения матрицы
numbers = [-15, -4, -2, -7, 0, 3, 5, 12, 9]

# Создание матрицы
matrix = []
for i in range(height):#цикл for
    row = []
    for j in range(width):#цикл for
        row.append(random.choice(numbers))#дополнение ряда рандомными значениями
    matrix.append(row)

# Вывод матрицы
print("Матрица:")
for row in matrix:#цикл for
    for numb in row:#цикл for
        print( numb , end=" ")
    print()

# Вычисление суммы всех элементов некратных 3
sum = 0
for row in matrix:#цикл for
    for numb in row:#цикл for
        if numb % 3 != 0:#условие что число должно быть некратным трем
            sum += numb

print(f"\nСумма всех элементов некратных 3: {sum}")#вывод суммы
