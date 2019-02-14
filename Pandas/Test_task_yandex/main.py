import pandas as pd

from matplotlib import pyplot
from collections import Counter


# display options for output pandas
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.options.display.expand_frame_repr = False

# ([0-9A-Z\a-z]*) - - \[(.+) -[0-9]*\] (.+) (\d+) (\d+)|(\w+.\w)

# create parser for non-standard format time
parser = lambda date: pd.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S')
# define pattern for regular expression
pattern_for_log = r'(.+) - - \[(.+) -[0-9]*\] (.+) (.+) (.+)|(\w+.\w)'
# Task 1 and 2 read the file and parse it in DataFrame with separate to space and named columns
df = pd.read_table('access_log_Jul95', 
					sep=pattern_for_log, 
					names=['None', 'IP/Domain name', 'Date and Time', 'URL', 'Code', 'Size'], 
					index_col=False, 
					engine='python', 
					error_bad_lines=False, 
					parse_dates=[2], 
					date_parser=parser, 
)
# delete unnecessary columns
df = df.drop(['None'], axis='columns')
# replace all NaN elements with 0
df = df.fillna(0)
# replace all '-' elements with 0 in Size column
df['Size'] = df['Size'].replace({'-': 0})


# Task 3 with method Counter count quantity repeat to each URL
count_repeat_to_url = Counter([i for i in df['URL']])


# Task 4 to 15 most visited url
most_visited_url = count_repeat_to_url.most_common(15)
df_url = pd.DataFrame(most_visited_url, columns=['URL','Quantity'])
print(df_url)


# Task 5 define quantity requests
quantity_requests = int(df['Code'].count())
# find first and last time request
time_start = df['Date and Time'].iloc[0]
time_finish = df['Date and Time'].iloc[-1]
# define delta time
delta_time = pd.to_timedelta((time_finish - time_start), unit='S', box=False)
# convert delta time to int64 type
delta_time_int64 = delta_time.astype('timedelta64[s]').astype(int)
# define quantity request per second
quantity_requests_per_second = quantity_requests / delta_time_int64
print('Quantity requests per second: ' + str(round(quantity_requests_per_second, 2)))


# Task 6 graph of requests per second
time = df['Date and Time']
count = [i for i in range(len(df['Date and Time']))]
# properties for plotting
fig, ax = pyplot.subplots(figsize=(18, 9))
ax.plot(time, count)
ax.set(xlabel='Time, seconds', 
	   ylabel='Quantity requests, pieces', 
       title='Graph of requests per second', 
)
ax.grid()
pyplot.show()


# Task 7 create histogram of requests size distribution
df = df.set_index('Date and Time')
# convert all Size elements to integer
df['Size'] = df['Size'].apply(int)
# resize column to 1 day
days_df = df.resample('1d')['Size'].mean()
# properties for plotting
fig, ax = pyplot.subplots(figsize=(18, 9))
ax.barh(days_df.index, days_df, align='center', height=0.5)
labels = ax.get_xticklabels()
# prooerties for figure
ax.set(xlabel='Request size, bytes', 
	   ylabel='Quantity times, days', 
       title='Histogram of requests size distribution', 
)
ax.grid()
pyplot.show()