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

>>> str1 = 'abc'
>>> set(str1)
set(['a', 'c', 'b'])
>>> str1 = 'abca'
>>> set(str1)
set(['a', 'c', 'b'])
>>> import string
>>> string.lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> set(string.lowercase)
set(['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z'])
>>> set(string.lowercase).difference(set(str1))
set(['e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z'])
>>> len(set(string.lowercase).difference(set(str1)))
23
>>> 
