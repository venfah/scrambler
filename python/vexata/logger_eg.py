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
