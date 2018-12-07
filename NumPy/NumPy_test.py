import numpy as np


a = np.array([1, 4, 5, 8], float)

print(a)
print(type(a))

a = np.array([[1, 2, 3], [4, 5, 6]], float)

print(a)
print(a[1,:])
print('Метод shape возвращает количество строк и столбцов в матрице:', a.shape)
print('Числовой тип данных в NumPy -', a.dtype)
print('Метод len возвращает длину первого измерения (оси):', len(a))
print('Метод in используется для проверки на наличие элемента в массиве:', 2 in a)

a = np.array(range(10), float)

print(a)
a = a.reshape((5, 2)) # метод reshape создает новый массив, а не модифицирует оригинальный.
print(a)

a = np.array([1, 2, 3], float)
a = a.tolist()

print(a)

a = np.array([1, 2, 3], float)
s = a.tostring() # конвертация массива в бинарную строку

print(s)
a = np.fromstring(s)
print(a)

a = np.array([1, 2, 3], float)
a.fill(0)

print(a)

a = np.array(range(6), float).reshape((2, 3))

print(a)
print(a.transpose()) # Транспонирование массивов

a = np.array([[1, 2, 3], [4, 5, 6]], float)

print(a)
print(a.flatten()) # Конвертация из многомерного массива в одномерный

a = np.array([1, 2], float)
b = np.array([3, 4, 5, 6], float)
c = np.array([7, 8, 9], float)

print(a)
print(b)
print(c)
print(np.concatenate((a, b, c)))

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float)

print(a)
print(b)
print()

print(np.concatenate((a,b), axis=0)) # конкатенация по разным осям
print(np.concatenate((a,b), axis=1)) # конкатенация по разным осям

print()
a = np.array([1, 2, 3], float)

print(a[:, np.newaxis]) # размерность массива может быть увеличена при использовании константы newaxis в квадратных скобках:
print(a[:, np.newaxis].shape)
print(a[np.newaxis, :])
print(a[np.newaxis, :].shape)

a = np.arange(5, dtype=float)
b = np.arange(1, 6, 2, dtype=int)

print()
print(a)
print(b)
print()

a = np.ones((2, 3), dtype=float)
b = np.zeros(7, dtype=int)

print()
print(a)
print(b)
print()

a = np.array([[1, 2, 3], [4, 5, 6]], float)
a = np.zeros_like(a)

print(a)
print()

a = np.ones_like(a)

print(a)

a = np.identity(4, dtype=float) # матрица с главной диагональю, которая заполненная единицами

print()
print(a)
print()

a = np.eye(4, k=1, dtype=float) # Функция eye возвращает матрицу с единичками на к-атой диагонали:

print(a)
print()

a = np.array([1, 2, 3], float)
b = np.array([5, 2, 6], float)

print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(a % b)
print(b ** a)
print()

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[2, 0], [1, 3]], float)

print(a * b)
print()

a = np.array([[1, 2], [3, 4], [5, 6]], float)
b = np.array([-1, 3], float)

print(a + b)
print()

a = np.zeros((2, 2), float)
b = np.array([-1, 3], float)

print(a + b)
print(a + b[:, np.newaxis])
print()

# к стандартным операторам, в numpy включена библиотека стандартных математических функций, которые могут быть применены поэлементно к массивам. Собственно функции: abs, sign, sqrt, log, log10, exp, sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, и arctanh.

a = np.array([1.1, 1.5, 1.9], float)

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
print()

print(np.pi)
print(np.e)
print()

a = np.array([1, 4, 5], int)

for i in a:
	print(i)
print()

a = np.array([[1, 2], [3, 4], [5, 6]], int)

for i in a:
	print(i)
print()

a = np.array([[1, 2], [3, 4], [5, 6]], float)

for (x, y) in a:
	print(x * y)
print()

a = np.array([2, 4, 3], float)

print(np.sum(a))
print(np.prod(a))
print()

a = np.array([2, 1, 9], float)

print(a.mean())
print(a.var())
print(a.std())
print(a.min())
print(a.max())
print()
print(a.argmin()) # Функции argmin и argmax возвращают индекс минимального или максимального элемента
print(a.argmax())
print()

a = np.array([[0, 2], [3, -1], [3, 5]], float)

print(a.mean(axis=0))
print(a.mean(axis=1))
print(a.min(axis=1))
print(a.max(axis=0))
print()

a = np.array([6, 2, 5, -1, 0], float)

print(sorted(a))
a.sort()
print(a)
print()

a = np.array([1, 1, 4, 5, 5, 5, 7], float)

print(np.unique(a))
print()

a = np.array([[1, 2], [3, 4]], float)

print(a.diagonal())
print()

a = np.array([1, 3, 0], float)
b = np.array([0, 3, 2], float)
c = 2

print(a > b)
print(a == b)
print(a <= b)
print(a > 2)
print()

a = np.array([True, False, False], bool)

print(any(a))
print(all(a))
print()

a = np.array([1, 3, 0], float)
b = np.array([True, False, True], bool)
c = np.array([False, True, False], bool)

print(np.logical_and(a > 0, a < 3))
print(np.logical_not(b))
print(np.logical_or(b, c))
print()

a = np.array([1, 3, 0], float)

print(np.where(a != 0, 1 / a, a))
print(np.where(a > 0, 3, 2))
print()

a = np.array([[0, 1], [3, 0]], float)

print(a.nonzero())
print()

a = np.array([1, np.NaN, np.Inf], float)

print(np.isnan(a))
print(np.isfinite(a))
print()

a = np.array([[6, 4], [5, 9]], float)

print(a >= 6)
print(a[a >= 6])
print(a[np.logical_and(a > 5, a < 9)])
print()

a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)

print(a[b])
print()

a = np.array([2, 4, 6, 8], float)

print(a[[0, 0, 1, 3, 2, 1]])
print()

a = np.array([[1, 4], [9, 16]], float)
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)

print(a[b,c])
print()

a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
# Специальная функция take доступна для выполнения выборки с целочисленными массивами. Это работает также как и использования оператора взятия по индексу:
print(a.take(b))
print()

a = np.array([[0, 1], [2, 3]], float)
b = np.array([0, 0, 1], int)

print(a.take(b, axis=0))
print(a.take(b, axis=1))
print()

a = np.array([0, 1, 2, 3, 4, 5], float)
b = np.array([9, 8, 7], float)
# В противоположность к функции take есть функция put, которая будет брать значения из исходного массива и записывать их на специфические индексы в другом put-массиве.
a.put([0, 3], b)
print(a)
print()

a = np.array([1, 2, 3], float)
b = np.array([0, 1, 1], float)
# Функция dot возвращает скалярное произведение векторов:
print(np.dot(a, b))
print()

a = np.array([[0, 1], [2, 3]], float)
b = np.array([2, 3], float)
c = np.array([[1, 1], [4, 0]], float)
# Функция dot также может умножать матрицы:
print(np.dot(b, a))
print(np.dot(a, b))
print(np.dot(a, c))
print(np.dot(c, a))
print()

a = np.array([1, 4, 0], float)
b = np.array([2, 2, 1], float)
# 
print(np.outer(a, b))
print(np.inner(a, b))
print(np.cross(a, b))
print()

a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
# linalg можно оперировать с вырожденными и невырожденными матрицами. Определитель матрицы ищется таким образом:
print(np.linalg.det(a))
print()

vals, vecs = np.linalg.eig(a)
# Также можно найти собственный вектор и собственное значение матрицы:
print(vals)
print(vecs)
print()

b = np.linalg.inv(a)
# Невырожденная матрица может быть найдена так:
print(b)
print(np.dot(a, b))
print()

a = np.array([[1, 3,4], [5, 2, 3]], float)
U, s, Vh = np.linalg.svd(a)
# Одиночное разложение (аналог диагонализации не квадратной матрицы) может быть достигнут так:
print(U)
print(s)
print(Vh)
print()

a = np.random.seed(293)
# Seed это целое число. Каждая программа которая запускается с одинаковым seed`ом будет генерировать одинаковую последовательность чисел каждый раз
print(a)
print()

a = np.random.rand(5)
# Массив случайных чисел из полуинтервала [0.0, 1.0) может быть сгенерирован так:
print(a)
print()

a = np.random.rand(2,3)
b = np.random.rand(6).reshape((2,3))
# Функция rand может быть использована для генерации двумерных массивов, или можно использовать функцию reshape:
print(a)
print(b)
print()

a = np.random.random()
# Для генерации единичного случайного числа на интервале [0.0, 1.0):
print(a)
print()

a = np.random.randint(5, 10)
# Для генерации случайного целочисленного числа в диапазоне [min, max) используем функцию randint(min, max):
print(a)
print()

a = np.random.normal()
# Для получении числа из нормального распределения (μ = 0, σ = 1), без указания аргументов:
print(a)
print()

a = np.random.normal(size=5)
# Для генерации нескольких значений используем аргумент size:
print(a)
print()

# l = range(10)
# np.random.shuffle(l)
# # Модуль для генерации случайных чисел также может быть использован для случайного распределения значений в списке.
# print(l)
# print()


# print(dir(np))