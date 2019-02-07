from collections import Counter


# define empty string
string_chars = ''
# open file
with open('simbols.txt') as file:
	# concatenate all line in one string
	for line in file:
		string_chars += line

# count all chars
count_chars_dict = Counter([char for char in string_chars])
# take keys in dict
arr_keys = [i for i in count_chars_dict.keys()]
# print 8 most rare chars
print(arr_keys[-1:-9:-1])