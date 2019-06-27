

'''
1. find prime no from 1 to 100

'''


def find_prime(no):
    if no == 1 or no == 2:
        return True
    for i in range(2, no):
        if divmod(no, i)[1] == 0:
            return False
    return True

for i in range (1, 101):
    if find_prime(i) == True:
        print (i),
'''
OUTPUT
Guest ran 18 lines of Python 2 (finished in 1.56s):

1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
>>> 
'''


'''
2. 
'''

'''
OUTPUT

'''

'''
3 find the equilibrium of the list
ie find an element such that right and left side of the element's sum is same (excluding the element)

'''


l1 = [4,1,2,3,5,6,4]

start = 0
end = len(l1)

found = False

for ind in range(1, len(l1)-1):
    if (sum(l1[start:ind]) == sum(l1[ind+1:end])):
        print (l1[start:ind], l1[ind+1:end], sum(l1[start:ind]), sum(l1[ind+1:end]))
        Found = True
        break    
else:
    if Found == False:
        print ("equilibrium of list: not found")
        
        
'''
OUTPUT


([4, 1, 2, 3], [6, 4], 10, 10)

''''

'''
Questions on linux and storage:

1. how to get the lun details, fdisk -l, multipath -ll, pvdisplay, lddisply, lvdisplay
2. how to create lv - pvcreate, ldcreate, lvcreate
3. how to list pcie devices, lspci
4. how to get pwwn no of hba
systool -c fc_host -v | grep -i wwn
5. how to test a raw lun with io
   differetn randdom ness of the IO, read write perc, zone set, zone create, different bs, combination of bs, DIRECT and SYNC flags
   trim, writesame zero and different patterns, read modified writes
   
6. how to get the iostat in linux, iostat.
7. what is inflight IO
8. What is loop back device

interview by vinayak shinde and abey
'''
