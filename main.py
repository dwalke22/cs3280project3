#!/usr/bin/env python3
"""
Port scanner that attempts to make a
TCP connection
"""
import multiprocessing
import sys
import os
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

def execute_task(arguments):
    """The task to execute"""
    print('Trying something...')
    print('with process no. ' + str(os.getppid()))
    print('...using ' + arguments)

if __name__ == "__main__":
    IP_ADDRESS = sys.argv[1]
    START_PORT = sys.argv[2]
    if len(sys.argv) == 4:
        END_PORT = sys.argv[3]
    if utils.verify_ipv4(IP_ADDRESS):
        VAL = " ".join(sys.argv)
        PROC = multiprocessing.Process(target=execute_task, args=(VAL,))
        PROC.start()
        PROC.join()
    else:
        print(" ".join(sys.argv))
        print("Not Valid Data")
