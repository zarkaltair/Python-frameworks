import pandas as pd


my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
print()
print(my_series.index)
print()
print(my_series.values)
print()

# Индексы можно задавать явно:
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])
print()

# Делать выборку по нескольким индексам и осуществлять групповое присваивание:
print(my_series2[['a', 'b', 'f']])
print()

my_series2[['a', 'b', 'f']] = 0
print(my_series2)
print()

# Фильтровать Series как душе заблагорассудится, а также применять математические операции и многое другое:
print(my_series2[my_series2 > 0])
print()

print(my_series2[my_series2 > 0] * 2)
print()

# Если Series напоминает нам словарь, где ключом является индекс, а значением сам элемент, то можно сделать так:
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)
print()

# У объекта Series и его индекса есть атрибут name, задающий имя объекту и индексу соответственно.
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)
print()

# Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series
my_series3.index = ['A', 'B', 'C', 'D']
print(my_series3)
print()