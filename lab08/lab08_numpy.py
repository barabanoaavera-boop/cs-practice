import numpy as np

# ===== ЗАДАНИЕ 1: Создание векторов и матриц =====
print("--- Задание 1 ---")
hours = np.arange(0, 22, 3) 
print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)

line = np.linspace(0, 1, 5) 
zeros = np.zeros(6, dtype=int) 
unknown_table = np.full((2, 3), -1) 
identity = np.eye(3) 

# ===== ЗАДАНИЕ 2: Индексы и срезы в векторе =====
print("\n--- Задание 2 ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с 2 по 5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("В обратном порядке:", hours[::-1])

# ===== ЗАДАНИЕ 3: Строки и столбцы таблицы =====
print("\n--- Задание 3 ---")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])
print("Форма:", temperatures.shape, "Размерность:", temperatures.ndim, "Элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
central = temperatures[0:2, 1:3]
print("Центральный фрагмент 2x2:\n", central)

# ===== ЗАДАНИЕ 4: Прямоугольные срезы =====
print("\n--- Задание 4 ---")
matrix = np.arange(1, 26).reshape(5, 5)
print("Первые три строки:\n", matrix[:3])
print("Последние две строки:\n", matrix[-2:])
print("Первые два столбца:\n", matrix[:, :2])
print("Строки 1-3, столбцы 2-4:\n", matrix[1:4, 2:5])
print("Правый нижний угол 2x2:\n", matrix[-2:, -2:])

# ===== ЗАДАНИЕ 5: Изменение массива с помощью срезов =====
print("\n--- Задание 5 ---")
changed_hours = hours.copy() 
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)

# ===== ЗАДАНИЕ 6: Изменение формы =====
print("\n--- Задание 6 ---")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers:", numbers, "shape:", numbers.shape)
print("table:\n", table, "shape:", table.shape)
print("transposed:\n", transposed, "shape:", transposed.shape)
