from time import sleep, time

def find_time(func):
	def inner(*args, **kwargs):
		start = time()
		return_value = func(*args, **kwargs)
		end = time()
		print ("{} took {} seconds".format(func.__name__, end-start))
		return return_value
	return inner


@find_time	
def run_a_test(num):
	for _ in range(0, num):
		for __ in range(0, _):
			for ___ in range (0, __):
				if (___ != 99):
					pass
	return 1

print(run_a_test(1000))
