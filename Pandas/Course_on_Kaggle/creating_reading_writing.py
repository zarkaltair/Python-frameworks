import pandas as pd


pd.set_option('max_rows', 5)

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Create a variable `ingredients` with a `pd.Series` that looks like:
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# read file
file_path = '../input/wine-reviews/winemag-data_first150k.csv'
reviews = pd.read_csv(file_path, index_col=0)

# from Data Frame to csv
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv('cows_and_goats.csv')

# read SQL
import sqlite3
conn = sqlite3.connect('../input/pitchfork-data/database.sqlite')

music_reviews = pd.read_sql_query('SELECT * FROM artists', conn)