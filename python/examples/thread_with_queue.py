# This is a sandbox to experiment with CoderPad's execution capabilities.
# It's a temporary, throw-away session only visible to you.


import threading

import Queue
import random
import time


def find_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Function {} took {} seconds for the value {}".format(func.__name__, time.time() - start, args[0]))

    return inner

@find_time
def run_a_test(no):
    default = 5
    no = random.randrange(0, no) or default

    for _ in range(0, no):
        for __ in range(0, _):
            for ___ in range (0, __):
                pass
    q.put("{} number of iterations completed: {}".format(no, True))
    return True


thread_factory = []

no_of_threads = 10

q = Queue.Queue()


for i in range(0, no_of_threads):
    thread_factory.append(threading.Thread(target=run_a_test, args=(500,)))

for thread in thread_factory:
    thread.start()

for thread in thread_factory:
    thread.join()
    while q.empty() == False: print(q.get())
    
"""
OUTPUT: ON CoderPad.io platform in python 2.7

Nazir ran 49 lines of Python 2 (finished in 5.72s):

Function run_a_test took 7.10487365723e-05 seconds for the value 500
Function run_a_test took 0.153090953827 seconds for the value 500
Function run_a_test took 0.19163608551 seconds for the value 500
Function run_a_test took 0.405709981918 seconds for the value 500
3 number of iterations completed: True
100 number of iterations completed: True
134 number of iterations completed: True
148 number of iterations completed: True
Function run_a_test took 2.05795311928 seconds for the value 500
Function run_a_test took 2.26459097862 seconds for the value 500
Function run_a_test took 2.66167497635 seconds for the value 500
Function run_a_test took 2.75154900551 seconds for the value 500
Function run_a_test took 3.73260116577 seconds for the value 500
Function run_a_test took 4.04177999496 seconds for the value 500
252 number of iterations completed: True
259 number of iterations completed: True
280 number of iterations completed: True
293 number of iterations completed: True
394 number of iterations completed: True
483 number of iterations completed: True

>>> 
"""
