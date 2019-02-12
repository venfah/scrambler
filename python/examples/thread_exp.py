
'''
Thread example with python and queue

'''

import threading
import time
import Queue
import random

def thread_target(a=0, b=0, **kwargs):
    time.sleep(10)
    queue_val.put(str(kwargs) + " Addition of X and Y: " + str(a + b))

if __name__ == "__main__":
    queue_val = Queue.Queue()

    no_of_th = 5
    i = 0
    Threads = {}

    while (i < no_of_th):
        rand_arr = [random.randint(0, no_of_th)*random.randint(0, int(no_of_th*5*7/3)), random.randint(1, no_of_th - 1)*random.randint(0, int(no_of_th*17*7/9))]
        i += 1
        test_thread = threading.Thread(target=thread_target, name="test_thread" + str(i), args=rand_arr, kwargs={'x': rand_arr[0],'y': rand_arr[1]})
        test_thread.start()
        Threads[test_thread] = test_thread
    print Threads

    time.sleep(15)
    for each_thread in Threads.keys():
        print each_thread.join()

    while not queue_val.empty():
        print queue_val.get()
        queue_val.task_done()
