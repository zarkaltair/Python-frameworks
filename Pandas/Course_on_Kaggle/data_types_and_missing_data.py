import pandas as pd


reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)

# What is the data type of the `points` column in the dataset?
dtype = reviews.points.dtype

# Create a `Series` from entries in the `points` column, but convert the entries to strings. Hint: strings are `str` in native Python.
point_strings = reviews.points.astype(str)

# Sometimes the price column is null. How many reviews in the dataset are missing a price?
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# Create a `Series` counting the number of times each value occurs in the `region_1` field. This field is often missing data, so replace missing values with `Unknown`. Sort in descending order.
replace_missing_values = reviews.region_1.fillna("Unknown")
reviews_per_region = replace_missing_values.value_counts().sort_values(ascending=False)