#!/usr/bin/python
import argparse
import threading
from subprocess import check_output, CalledProcessError
from re import compile, search
from time import time, mktime, strptime, ctime, sleep

'''
HOW TO RUN

# python run_stress.py --namespace t001-u000003  --pods st-centos-01,st-centos-02,st-centos-03,st-centos-04,st-centos-05,st-centos-06,st-centos-07,st-centos-08,st-centos-09,st-centos-10,st-centos-11,st-centos-12,st-centos-13,st-centos-14,st-centos-15,st-centos-16,st-centos-17,st-centos-18,st-centos-19,st-centos-20

python run_stress.py --namespace t001-u000003  --pods $(kubectl get pods --all-namespaces | grep -i t001-u | awk -vORS=, '{print $2}' | sed 's/,$/\n/')


HOW TO GET CSV OF ALL PODS for some NAMESPACES

[root@eqx04-backend12 srcbuild]# kubectl get pods --all-namespaces | grep -i t001-u | awk -vORS=, '{print $2}' | sed 's/,$/\n/'
cs-1-server-01,cs-1-server-02,cs-1-server-03,cs-1-server-04,cs-1-server-05,cs-1-server-06,cs-1-server-07,cs-1-server-08,cs-1-server-09,cs-1-server-10,cs-1-server-11,cs-1-server-12,cs-1-server-13,cs-1-server-14,cs-1-server-15,cs-1-server-16,cs-1-server-17,cs-1-server-18,cs-1-server-19,cs-1-server-20
[root@eqx04-backend12 srcbuild]#

USE THE BELOW COMMAND TO STESS CPU

python run_stress.py --namespace t001-u000003  --pods $(kubectl get pods --all-namespaces | grep -i t001-u | awk -vORS=, '{print $2}' | sed 's/,$/\n/')

'''

def run(cmd):
    print("{}: {}".format(ctime(), cmd))
    try:
        out = check_output(cmd, shell=True)
    except CalledProcessError as e:
        out = ""
    return out

def thread_target(*cpargs):
    get_cpu = "kubectl describe pod {} -n {} | grep -i robin.runtime.cpuset | cut -d, -f2".format(cpargs[1], cpargs[0])
    output = run(get_cpu)
    print (output)
    #cmd = "kubectl exec -it -n {} {} -- stress -c {}".format(cpargs[0], cpargs[1], output)
    cmd = "kubectl exec -it -n {} {} -- stress --cpu 57 --io 4 --vm 2 --vm-bytes 128M --timeout 4h".format(cpargs[0], cpargs[1])
    print (cmd)
    output = run(cmd)
    print (output)
    pass

if __name__ == "__main__":
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='run stress on CPUs')
    parser.add_argument('--pods', type=str, help='csv of pod names')
    parser.add_argument('--namespace', type=str, help='Name space of all the pods')
    args = parser.parse_args()

    i = 0
    Threads = {}

    for each_pod in args.pods.split(","):
        test_thread = threading.Thread(target=thread_target, name="wr_ver_thr" + str(i), args=(args.namespace, each_pod))
        test_thread.start()
        Threads[test_thread] = test_thread
        i += 1

    sleep(60)
    #while True:
    #    print ("Going to sleeper thread")
    #    sleep(60)
    #    pass
    for each_thread in Threads.keys():
        print each_thread.join()
