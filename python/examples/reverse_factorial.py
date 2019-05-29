


def rev_factorial(no):
	fact = 1
	while True:
		q, r = divmod(no, fact)
		if r != 0:
			return None
		if q == 1:
			return fact
			break	
		if r == 0:
			no = no // fact
			fact += 1
print(rev_factorial(1*2*3*4*5))


'''
OUTPUT

5
'''
