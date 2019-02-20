'''
print the word list from the input
if CTRL+C is pressed, handle it
'''

from __future__ import print_function
import signal

def sig_handler(signal, frame):
    print ("Caught CTRL+C: no words listed", end="\n")

signal.signal(signal.SIGINT, sig_handler)

print(raw_input("Enter an input string: ").strip().split())
