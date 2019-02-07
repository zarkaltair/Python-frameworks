import pandas as pd
import datetime
import re
import matplotlib.pyplot as plt

from pprint import pprint
from collections import Counter


# display options for output pandas
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.options.display.expand_frame_repr = False


# Task 1 and 2 read the file and parse it in DataFrame with separate to space and named columns
df = pd.read_table('log', sep=' ', 
						  names=['Date and Time','Time code','URL', 'Code', 'Size'], 
						  engine='python', 
						  error_bad_lines=False
	) # access_log_jul95
# reset index
df = df.reset_index()
# delete unnecessary columns
df = df.drop(['level_1'], axis='columns')
df = df.drop(['level_2'], axis='columns')
# concatenate Date column with Time column
# df['Date and Time'] = df['IP'] + '' + df['Date']
# delete IP column and Date column
df = df.drop(['Time code'], axis='columns')
# df = df.drop(['Date'], axis='columns')
# rename column
df = df.rename(columns={'level_0': 'IP'})


# Task 3 with method Counter count quantity repeat to URL
count_repeat_to_url = Counter([i for i in df['URL']])


# Task 4 to 15 most visited url
most_visited_url = count_repeat_to_url.most_common(15)
# print(most_visited_url)


# Task 5 
array_time_string_by_log = [i for i in df['Date and Time']]
array_time = []
for time_string in array_time_string_by_log:
	# define pattern for regular expression
	pattern = r'[^\d]'
	# find the regular expression pattern in the string and remove all unnecessary
	# split that string into spaces using the method .sub
	d = re.sub(pattern, ' ', time_string).split(' ')
	# define date and time in the string
	time_request = [int(i) for i in d if i.isdigit() and int(i) < 100]
	# append our time_request to array_time
	array_time.append(time_request)

# define time to start and finish requests
time_start = array_time[0][0] * 60 * 60 * 24 + array_time[0][-1]
time_finish = array_time[-1][0] * 60 * 60 * 24 + array_time[-1][1] * 60 * 60 + array_time[-1][2] * 60 + array_time[-1][-1]

# define quantity request per second
quantity_request_per_second = (time_finish - time_start) / len(array_time_string_by_log)
# print(quantity_request_per_second)



# Task 6 
# df_plot = df.loc['0': '100', ['Date and Time']]
# df_plot = df.plot.scatter(x=array_time, y='IP')
# plt.show()


# Task 7 




# pprint(count_repeat_to_url)
# pprint(most_visited_url)
# pprint(quantity_request_per_second)


t1 = '[01/Jul/1995:00:00:01'
t2 = '[03/Jul/1995:04:02:51'
time1 = pd.to_datetime(t1[1:], format='%d/%b/%Y:%H:%M:%S')
time2 = pd.to_datetime(t2[1:], format='%d/%b/%Y:%H:%M:%S')
print(time2 - time1)



# print(df)