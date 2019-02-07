import pandas as pd
import matplotlib.pyplot as plt


# display options for pandas
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.options.display.expand_frame_repr = False

# Группировка данных один из самых часто используемых методов при анализе данных. В pandas за группировку отвечает метод .groupby.
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.head())
print()

# Необходимо подсчитать, сколько женщин и мужчин выжило, а сколько нет. В этом нам поможет метод .groupby.
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
print()

# А теперь проанализируем в разрезе класса кабины:
print(titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())
print()

# Сводные таблицы в pandas
pvt = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
print(pvt.loc['female', ['1st', '2nd', '3rd']])
print()

# Анализ временных рядов на примере акций Apple
df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()
print(df.info())
print()

# Давайте теперь узнаем среднюю цену акции (mean) на закрытии (Close):
print(df.loc['2012-Feb', 'Close'].mean())
print()

# А если взять промежуток с февраля 2012 по февраль 2015 и посчитать среднее:
print(df.loc['2012-Feb':'2015-Feb', 'Close'].mean())
print()

# А что если нам нужно узнать среднюю цену закрытия по неделям?!
print(df.resample('W')['Close'].mean())
print()

# Визуализация данных в pandas
new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()