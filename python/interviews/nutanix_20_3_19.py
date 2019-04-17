'''

Nutanix questions: 20th March - 2019

 

1. You have developed a http application and deploed on office intranet. next morning

it is not up. how do you troubleshoot and fidn the RCA.

 

2.           

                r = lambda q: q*2

                s = lambda q: q*3

                x = 2

                x = r(x)

                x = s(x)

                x = r(x)

                print r(x), r(s(x))

 

3. given a string "I love You Nutanix"

do word reversal. if first letter of the word is capitalized, when you reverse the first letter should be capitalized.

output string: I evol UoY XinatuN

 

4. can we have an output string on which no repitable string is adjacent. for this question

assume there is only one string which is oging to be repeated.

 

given a string "aab" , it can be written as "aba" so it is POSSIBLE to re-write like above. so output "POSSIBLE" if possible

if string is "aa", it can not be changed to have non repeatable words in adjacent. so here "NOT POSSIBLE"

 

'''

 

r = lambda q: q*2

s = lambda q: q*3

x = 2

x = r(x)

x = s(x)

x = r(x)

print r(x), r(s(x))

 

# 48, 144

import string

input_string = "I love You Nutanix"

output_string = []

for word in input_string.strip().split():

                reversed = [char for char in word]

                reversed.reverse()

                reversed_word = "".join(reversed)

                if word.istitle() == True:

                                output_string.append(reversed_word.capitalize())

                else:

                                output_string.append(reversed_word)

print (" ".join(output_string))

                               

given_string = "aab"

dict1 = {}

for char in given_string:

                if char in dict1:

                                dict1[char] += 1

                else:

                                dict1[char]  = 1

 

if len(dict1.keys()) >= 2:

                print ("\"POSSIBLE\"")

else:

                print ("\"NOT POSSIBLE\"")
