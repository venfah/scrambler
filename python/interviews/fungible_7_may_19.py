'''
you are given a list l
prepare an another list which has elements where
the index is added to list for number of times of the value in the index

'''

l = [5, 2, 3]

l1 = []

for e, v in enumerate(l):
  l1.extend([e for _ in range(v)])

print (l1)

'''
OUTPUT:
>>> 

Nazir ran 13 lines of Python 2 (finished in 1.38s):

[0, 0, 0, 0, 0, 1, 1, 2, 2, 2]

>>> 


'''
