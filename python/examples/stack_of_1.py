'''
stackoverflow problems:
'''
idict =  {'name': 'Mark', 'marks':[{'english':20, 'maths':25},{'english':50, 'maths':55}]}
print (idict)
marks = idict.pop("marks")
result = []
for each in marks:
    result.append({'name': idict['name']})
    for key, val in each.items():
        result[-1][key] = val
print (result)
        




list_i =  [12, 34, 22, 24, 55, 67, 108, 999] 
out_dict = {}

for each in list_i:
    if int(str(each)[0]) in out_dict:
        out_dict[int(str(each)[0])].append(each) 
    else:
        out_dict[int(str(each)[0])] = [each] 

print (out_dict)

        
