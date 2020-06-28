import pandas as pd


# DataFrame проще всего сконструировать на примере питоновского словаря:
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})
print(df)
print()
print(df['country'])
print()

# Чтобы убедиться, что столбец в DataFrame это Series, извлекаем любой:
print(type(df['country']))
print()

# Если индекс по строкам явно не задан, то pandas задаёт целочисленный индекс
print(df.columns)
print()
print(df.index)
print()

# Доступ по индексу в DataFrame
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
print(df)
print()
print(df.index)
print()

df.index.name = 'Country Code'
print(df)
print()

# объекты Series из DataFrame будут иметь те же индексы, что и объект DataFrame:
print(df['country'])
print()

# Доступ к строкам по индексу возможен несколькими способами:
# .loc - используется для доступа по строковой метке
# .iloc - используется для доступа по числовому значению (начиная от 0)
print(df.loc['KZ'])
print()
print(df.iloc[0])
print()

# Можно делать выборку по индексу и интересующим колонкам:
print(df.loc[['KZ', 'RU'], 'population'])
print()

# Как можно заметить, .loc в квадратных скобках принимает 2 аргумента: интересующий индекс, в том числе поддерживается слайсинг и колонки.
print(df.loc['KZ': 'BY', :])
print()

# Фильтровать DataFrame с помощью т.н. булевых массивов:
print(df[df.population > 10][['country', 'square']])
print()

# Сбросить индексы можно вот так:
print(df.reset_index())
print()

# Добавим новый столбец, в котором население (в миллионах) поделим на площадь страны, получив тем самым плотность:
df['density'] = df['population'] / df['square'] * 1000000
print(df)
print()

# Не нравится новый столбец? Не проблема, удалим его:
df = df.drop(['density'], axis='columns')
print(df)
print()

# Переименовывать столбцы нужно через метод rename:
df = df.rename(columns={'Country Code': 'country_code'})
print(df)
print()

# Чаще всего приходится работать с csv-файлами. Например, чтобы сохранить наш DataFrame со странами, достаточно написать:
df.to_csv('filename.csv')

# Считать данные из csv-файла и превратить в DataFrame можно функцией read_csv:
df = pd.read_csv('filename.csv', sep=',')
