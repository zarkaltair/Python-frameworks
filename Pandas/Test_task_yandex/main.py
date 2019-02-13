import pandas as pd
import numpy as np
import datetime
import re

from pprint import pprint
from matplotlib import pyplot
from collections import Counter


# display options for output pandas
pd.options.display.max_rows = 100000
pd.options.display.max_columns = 10
pd.options.display.expand_frame_repr = False

# ([\'\\"`�|#*$&<^>/_:;()~=%@+?,0-9A-Z\-a-z\.]*) - - \[([0-9A-Za-z\/\:]*) -[0-9]*\] ([0-9A-Za-z\'\\\]\"`�|#*$t̓&<^>/_:;()~=%@+?,/\.\- ]*\") ([0-9]*) ([0-9\-]*)

# create parser for non-standard format time
parser = lambda date: pd.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S')
# define pattern for regular expression
pattern_for_log = r'(.+) - - \[(.+) -[0-9]*\] (.+) (.+) (.+)'
# Task 1 and 2 read the file and parse it in DataFrame with separate to space and named columns
df = pd.read_table('log', sep=pattern_for_log, 
					names=['None', 'IP/Domain name', 'Date and Time', 'URL', 'Code', 'Size'], 
					index_col=False, 
					engine='python', 
					error_bad_lines=False, 
					parse_dates=[2], 
					date_parser=parser, 
) # access_log_Jul95

# delete unnecessary columns
df = df.drop(['None'], axis='columns')
# replace all NaN elements with 0
df = df.fillna(0)
# replace all '-' elements with 0
df['Size'] = df['Size'].replace({'-': 0})


# Task 3 with method Counter count quantity repeat to each URL
count_repeat_to_url = Counter([i for i in df['URL']])


# Task 4 to 15 most visited url
most_visited_url = count_repeat_to_url.most_common(15)
df_url = pd.DataFrame(most_visited_url, columns=['URL','Quantity'])
print(df_url)


# Task 5 define quantity requests
quantity_requests = int(df['Code'].count())
# create array with all date and time
array_time_string_by_log = [i for i in df['Date and Time']]
# convert first and last time request
time_start = array_time_string_by_log[0]
time_finish = array_time_string_by_log[-1]
# define delta time
delta_time = pd.to_timedelta((time_finish - time_start), unit='S', box=False)
# convert delta time to int64 type
delta_time_int64 = delta_time.astype('timedelta64[s]').astype(int)
# define quantity request per second
quantity_requests_per_second = quantity_requests / delta_time_int64
print('Quantity requests per second: ' + str(round(quantity_requests_per_second, 2)))


# Task 6 graph of requests per second
time = [i for i in df['Date and Time']]
count = [i for i in range(len(df['Date and Time']))]
# properties for plotting
fig, ax = pyplot.subplots()
ax.plot(time, count)
ax.set(xlabel='Time', 
	   ylabel='Quantity requests',
       title='Graph of requests per second')
ax.grid()
pyplot.show()

# Task 7 create histogram of requests size distribution
n, bins, pathes = pyplot.hist(df['Size'], int(df['Size'].count()), facecolor='g', alpha=0.85)
# properties for plotting
pyplot.xlabel('Request size')
pyplot.ylabel('Quantity requests')
pyplot.title('Histogram of requests size distribution')
pyplot.axis([0, df['Size'].max(), 0, Counter([i for i in df['Size']]).most_common(1)[0][1]])
pyplot.grid(True)
pyplot.show()

'''
# print(df)
'''