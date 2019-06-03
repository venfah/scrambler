#How do you reverse a given string in place?
str1 = 'stonecold'
str_list = list(str1)

for i in range(0, int(len(str_list)/2)):
    str_list[i], str_list[len(str_list) -1 - i] =  str_list[len(str_list) -1 - i], str_list[i]
print ("Original String {}".format(str1))
print ("Reversed String {}".format("".join(str_list)))


# How do you print duplicate characters from a string?

from collections import Counter
import string

print("Duplicate Chars {} ".format("".join([key for key, val in Counter(str1).items() if val > 1])))

print(sorted(str1))

#How do you count a number of vowels and consonants in a given string?

result_dict = {'vowels':0, 'consonents':0}
for char in str1.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        result_dict['vowels'] += 1
    if char in set(string.lowercase).difference(set(['a', 'e', 'i', 'o', 'u'])):
        result_dict['consonents'] += 1
print (result_dict)

atoi = 0
for char in str1:
    atoi += ord(char)
print ("atoi value of {} is {}".format(str1, atoi))
    
    
    
'''
OUTPUT
Nazir ran 34 lines of Python 2 (finished in 1.53s):

Original String stonecold
Reversed String dlocenots
Duplicate Chars o 
['c', 'd', 'e', 'l', 'n', 'o', 'o', 's', 't']
{'consonents': 6, 'vowels': 3}
Traceback (most recent call last):
  File "/home/coderpad/solution.py", line 33, in <module>
    print ("atoi value of {} is {}".format(st1, atoi))
NameError: name 'st1' is not defined


>>> 

Nazir ran 34 lines of Python 2 (finished in 1.36s):

Original String stonecold
Reversed String dlocenots
Duplicate Chars o 
['c', 'd', 'e', 'l', 'n', 'o', 'o', 's', 't']
{'consonents': 6, 'vowels': 3}
atoi value of stonecold is 971

>>> 
'''
