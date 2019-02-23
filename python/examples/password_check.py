
'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

import re
import sys
import signal

def signal_handler(signal, frame):
	print ("CTRL + C pressed")
	print ("exiting")
	sys.exit(1)
	
signal.signal(signal.SIGINT, signal_handler)

in_string = raw_input().strip()

def check_regex(input_string):
	if len(input_string) <= 6 or len(input_string) > 12:
		return False
	if re.search(r'[0-9]', input_string) and re.search(r'[a-z]', input_string) and re.search(r'[A-Z]', input_string) and re.search(r'[$#@]', input_string):
		return True
	else:
		return False
	
print ("Is password Valid : " + str(check_regex(in_string)))
