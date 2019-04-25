1. read a file and count each words and first 3 occurances.
2. str1 = 'abc'
now find out missing strings from alphabet.

for 1

https://github.com/venfah/scrambler/blob/master/python/examples/find_max_three.py 
'''
# One more better way just to read the file  and get the word list
words = open(filename, 'b').read().split()
for word in words:
	if word in count_dict:
		count_dict[word] += 1
	else:
		count_dict[word]  = 1
'''

2. 

  1 
  2 
  3 import string
  4 input_str = 'ABC'
  5 
  6 input_set = set(input_str)
  7 all_set = set (string.ascii_uppercase)
  8 print("".join(sorted(list(all_set.difference(input_set)))))
  9 
