

# fungible interview questions by john abraham 11th June 2019
# Q1 write a program to flatten a list
l1 = [1, 3, 5, [6, 6, 8], 6, 7, [1, 2, 3]]
l2 = []
for ele in l1:
	if isinstance(ele, list) == True:
		l2.extend(ele)
	else:
		l2.append(ele)
print (l2)

'''
OUTPUT:
[1, 3, 5, 6, 6, 8, 6, 7, 1, 2, 3]
'''

# Q2 write the same flatten program through recursion
l1 = [1, 3, 5, [6, 6, [1,2,3] ], 6, 7, [1, 2, 3]]
l2 = []
def flat_list(l1):
	global l2
	for ele in l1:
		if isinstance(ele, list):
			flat_list(ele)
		else:
			l2.append(ele)
flat_list(l1)
print (l2)

'''
OUTPUT
[1, 3, 5, 6, 6, 1, 2, 3, 6, 7, 1, 2, 3]
'''

# Q3 sort the keys and print them based on values of the dictionary
d1 = {"a": 5, "b": 1, "c": 7}
#result = ["b", "a", "c"] result should be like this

def on_values(x):
	return x[1]
l1 = sorted(d1.items(), key=on_values)
print([each[0] for each in l1])

'''
OUTPUT

['b', 'a', 'c']

'''

# Q4 example for decorator
def square_func(func):
	def inner(*arg, **kwargs):
		print ("square of no {} is {}".format(arg[0], arg[0]*arg[0]))
		print ("just the no {}".format(func(arg[0])))
	return inner

@square_func
def some_func(a):
	return(a)

a = 20
some_func(a)

'''
OUTPUT
['b', 'a', 'c']
square of no 20 is 400
just the no 20
'''

# Q5: 
s = "abcd-90-def"
from re import search
reg = search(r"^(\w+)-(\w+)-(\w+)", s)
if reg:
	print (reg.groups()[1])
'''
OUTPUT

90

'''