'''
# Time complexity for reversing alternate columns in rows*columns 2D matrix
# m rows and n col
# m + m/2*reverse(log(n))
interviewed by kiran from rubrik
'''

output = [ [1, 2, 3], [6, 5, 4], [7, 8, 9], [2,3,4]]


def test_matrix(matrix):
    result = []
    for e, el in enumerate(matrix):
        if e%2 == 0:
            result.append(el)
        else:
            result.append(list(reversed(el)))
    print (result)

            
matrix = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]]

# Different tests
test_matrix([[]])
test_matrix([[1,2,3]])
test_matrix(matrix)
matrix.append([1,2,3])
test_matrix(matrix)
 
'''
Nazir Ahamed ran 29 lines of Python 2 (finished in 1.49s):

[[]]
[[1, 2, 3]]
[[1, 2, 3], [6, 5, 4], [7, 8, 9]]
[[1, 2, 3], [6, 5, 4], [7, 8, 9], [3, 2, 1]]

>>> 
'''
