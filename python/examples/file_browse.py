

from os import listdir, sep
from os.path import isdir

file_count = dir_count = 0
def file_rec(file_path):
	global file_count
	global dir_count
	list_dir = listdir(file_path)
	for file in list_dir:
		if isdir (file_path + sep + file):
			dir_count += 1
			print ("DIR : {}".format(file_path + sep + file))
			file_rec(file_path + sep + file)
		else:
			file_count += 1
			print ("FILE : {}".format(file_path + sep + file))

file_path = "/home"

file_rec(file_path)
print("file count : {}".format(file_count))
print ("dir count : {}".format(dir_count))
