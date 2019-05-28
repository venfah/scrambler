

list_item = '''
name available recieved comment
service1 1 2 comment
service2 4 5 comment again
'''

result_dict = dict()
header = []

for enu, line in enumerate(list_item.splitlines()):
    temp = []
    if enu == 0:
        continue
    if enu == 1:
        header.extend(line.split())
    else:
        temp.extend(line.split(' ', 3))
        result_dict[temp[0]] = dict()
        for i in range(0, len(temp)):
            result_dict[temp[0]][header[i]] = temp[i]


print (result_dict)


'''
RESULT OUTPUT for result_dict:

[root@colonicobar ~]# python list_sparse.py 
{'service2': {'available': '4', 'recieved': '5', 'name': 'service2', 'comment': 'comment again'}, 'service1': {'available': '1', 'recieved': '2', 'name': 'service1', 'comment': 'comment'}}
[root@colonicobar ~]# 
'''
