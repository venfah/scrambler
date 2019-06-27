
'''
find the equilibrium of the list
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
        print ("equi not found")
        
        
'''
OUTPUT


([4, 1, 2, 3], [6, 4], 10, 10)

''''
