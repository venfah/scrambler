'''
print reverse ladder.
run python reverse_ladder.py 5
output:
    *
   **
  ***
 ****
*****
'''
from __future__ import print_function
import sys

if len(sys.argv) <> 2:
    print ("help: python {0} 5". format(sys.argv[0]))
    sys.exit(1)

no = int(sys.argv[1])
for each in range(0, no):
    print (' ' * (no - each - 1), '*' * (each + 1))
