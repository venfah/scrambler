
'''
This script is to read a file and find first 3 max word occurences.
'''

filename = 'resources/content.txt'
count_dict = {}

for line in open(filename, 'r'):
	words = line.split()
	for word in words:
		if word in count_dict:
			count_dict[word] += 1
		else:
			count_dict[word]  = 1
		
def on_values(value):
	return value[1]
sorted_list = sorted(count_dict.items(), reverse=True,  key=on_values)

max = dict()

for each in sorted_list:
	max[each[1]] = each[1]
	if len(max) <= 3:
		print (str(each[0]) + " : " +  str(each[1]))

