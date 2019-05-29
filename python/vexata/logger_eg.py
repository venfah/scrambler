#!/usr/bin/python
# coding: utf-8

import subprocess
from subprocess import CalledProcessError
import logging
import sys


def run_cmd(cmd, **kwargs):
    print (cmd)
    print (kwargs)
    
    logger = logging.getLogger(__name__)

    if kwargs['log_console'] == True: # if you want the console logging initialize the handler
        sf = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        sh = logging.StreamHandler()
        if kwargs['loglevel']:
            sh.setLevel(kwargs['loglevel'])
        else:
            sh.setLevel(logging.INFO)
        sh.setFormatter(sf)
        logger.addHandler(sh)

    if kwargs['log_file'] == True: # if you want the logging to happen to fine, initialize this handler
        ff = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if 'loglocation' in kwargs:
            print ("inside log location true")
            fh = logging.FileHandler(kwargs['loglocation']) #log file has to be present
        else:
            fh = logging.FileHandler('my_app.log')  #  default log file location. This has to be present
        if kwargs['loglevel']:
            fh.setLevel(kwargs['loglevel'])
        else:
            fh.setLevel(logging.INFO)
        fh.setFormatter(ff)
        logger.addHandler(fh)

    output = ''
    return_code = ''
    try: 
            output = subprocess.check_output(cmd)
            return_code = 0
    except CalledProcessError as e:
            return_code = e.returncode
            output = e.output

    logger.error(" ".join(cmd)) 
    logger.error(output) 
    logger.error("Exit status: {}".format(return_code))

def test_1():
    cmd = [ "ls", "-lrt"]
    run_cmd(cmd, log_console=True, log_file=True, loglocation="log.txt", loglevel=logging.DEBUG)

test_1()


'''
SAMPLE OUTPUT: PYTHON 2.7
(python_virtualenv)[root@bazooka2 ha_vxt]# python logger_eg.py 
['ls', '-lrt']
{'loglocation': 'log.txt', 'loglevel': 10, 'log_file': True, 'log_console': True}
inside log location true
__main__ - ERROR - ls -lrt
__main__ - ERROR - total 1064
-rw-r--r--.  1 root    root    846410 Nov 30  2017 est16all.txt
drwxrwxr-x. 10 jenkins jenkins   4096 Aug  4  2018 atf
-rw-r--r--.  1 root    root    158978 Feb  1 15:30 robin-precheck-k8s_5.0.2-93.sh
-rw-r--r--.  1 root    root       524 Feb 14 22:57 pytest_run
-rw-r--r--.  1 root    root       877 Mar  7 03:44 port_parse.py
-rw-r--r--.  1 root    root       560 Mar 19 03:48 ssh.pyc
-rw-r--r--.  1 root    root      1551 Mar 19 04:33 portlist
-rw-r--r--.  1 root    root       807 Mar 19 05:01 ssh.py
-rw-r--r--.  1 root    root       368 Mar 20 11:18 samp.json
-rw-r--r--.  1 root    root       540 Mar 25 00:32 mem_profiling.py
drwxr-xr-x.  2 root    root        16 Mar 27 23:34 fabricshow
drwxr-xr-x. 17 root    root      4096 Apr  4 01:28 PR_LOGS
drwxrwxr-x. 17 jenkins jenkins   4096 Apr  4 02:02 tests
-rw-r--r--.  1 root    root       256 Apr 25 01:20 subpro.py
-rw-r--r--.  1 root    root       353 May  5 13:22 find_missing.py
-rw-r--r--.  1 root    root       157 May  5 23:25 profile.pyc
-rw-r--r--.  1 root    root       122 May 28 04:33 xep.py
-rw-r--r--.  1 root    root       925 May 28 05:54 conftest.py
-rw-r--r--.  1 root    root       669 May 28 05:58 test_1.py
-rw-r--r--.  1 root    root       312 May 28 11:38 url_rest.py
-rw-r--r--.  1 root    root       997 May 28 11:52 pytest_test.py
drwxr-xr-x.  2 root    root      4096 May 28 11:52 __pycache__
-rw-r--r--.  1 root    root      1785 May 29 02:09 logger_eg.py
-rw-r--r--.  1 root    root         0 May 29 02:09 log.txt

__main__ - ERROR - Exit status: 0
(python_virtualenv)[root@bazooka2 ha_vxt]# cat my_app.log ^C                                                                                                      
(python_virtualenv)[root@bazooka2 ha_vxt]# cat log
logger_eg.py  log.txt       
(python_virtualenv)[root@bazooka2 ha_vxt]# cat log.txt 
2019-05-29 02:09:04,462 - __main__ - ERROR - ls -lrt
2019-05-29 02:09:04,462 - __main__ - ERROR - total 1064
-rw-r--r--.  1 root    root    846410 Nov 30  2017 est16all.txt
drwxrwxr-x. 10 jenkins jenkins   4096 Aug  4  2018 atf
-rw-r--r--.  1 root    root    158978 Feb  1 15:30 robin-precheck-k8s_5.0.2-93.sh
-rw-r--r--.  1 root    root       524 Feb 14 22:57 pytest_run
-rw-r--r--.  1 root    root       877 Mar  7 03:44 port_parse.py
-rw-r--r--.  1 root    root       560 Mar 19 03:48 ssh.pyc
-rw-r--r--.  1 root    root      1551 Mar 19 04:33 portlist
-rw-r--r--.  1 root    root       807 Mar 19 05:01 ssh.py
-rw-r--r--.  1 root    root       368 Mar 20 11:18 samp.json
-rw-r--r--.  1 root    root       540 Mar 25 00:32 mem_profiling.py
drwxr-xr-x.  2 root    root        16 Mar 27 23:34 fabricshow
drwxr-xr-x. 17 root    root      4096 Apr  4 01:28 PR_LOGS
drwxrwxr-x. 17 jenkins jenkins   4096 Apr  4 02:02 tests
-rw-r--r--.  1 root    root       256 Apr 25 01:20 subpro.py
-rw-r--r--.  1 root    root       353 May  5 13:22 find_missing.py
-rw-r--r--.  1 root    root       157 May  5 23:25 profile.pyc
-rw-r--r--.  1 root    root       122 May 28 04:33 xep.py
-rw-r--r--.  1 root    root       925 May 28 05:54 conftest.py
-rw-r--r--.  1 root    root       669 May 28 05:58 test_1.py
-rw-r--r--.  1 root    root       312 May 28 11:38 url_rest.py
-rw-r--r--.  1 root    root       997 May 28 11:52 pytest_test.py
drwxr-xr-x.  2 root    root      4096 May 28 11:52 __pycache__
-rw-r--r--.  1 root    root      1785 May 29 02:09 logger_eg.py
-rw-r--r--.  1 root    root         0 May 29 02:09 log.txt

2019-05-29 02:09:04,463 - __main__ - ERROR - Exit status: 0
(python_virtualenv)[root@bazooka2 ha_vxt]# 

'''
