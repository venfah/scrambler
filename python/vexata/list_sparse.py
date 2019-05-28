

list_item = '''
name available recieved comment
service1 1 2 comment
service2 4 5 comment again
'''

result_dict = dict()
header = []

for enu, line in enumerate(list_item.splitlines()):
    print ("{} : {}".format(enu, line))
    temp = []
    if enu == 0:
        continue
    if enu == 1:
        header.extend(line.split())
    else:
        temp.extend(line.split(' ', 3))
        result_dict[temp[0]] = dict()
        print (header)
        print (temp)
        for i in range(0, len(temp)):
            result_dict[temp[0]][header[i]] = temp[i]


print (result_dict)
