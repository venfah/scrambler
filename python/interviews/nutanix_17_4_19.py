# 1
'''
# input1 = [-3, 0, 2, 0, 1, 4]
# output1 = [-3, 2, 1, 4, 0, 0]
#print([no for nof
for i in range(0, len(input1)):
	if input1[i] == 0:
  	input1.remove(0)
    input1.append(0)
'''

input1 = [-3, 0, 2, 0, 1, 4]
for each in input1:
	if each == 0:
		input1.remove(0)
		input1.append(0)
print(input1)

#2
'''
# input1 = "hhdddbbbbaaabbh"
# output  = "3h3d6b3a"
'''
input1 = "hhdddbbbbaaabbh"

result_dict1 = dict()
for each in input1:
	if each in result_dict1:
		result_dict1[each] += 1
	else:
		result_dict1[each]  = 1
ordered_list = []
for each in input1:
	if each not in ordered_list:
		ordered_list.append(each)
output_str = ''

for each in ordered_list:
	output_str += str(result_dict1[each]) + each
print(output_str)
