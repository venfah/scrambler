



no = 29

for each in range (2, no + 1):
	divisible = 0
	for no in range (2, each + 1):
		if (each % no == 0):
			divisible += 1
	if divisible <= 1:
		print (each),
