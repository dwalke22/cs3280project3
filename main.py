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

def scan(arguments):
    """
    The task to execute

    arguments - specified arguments
    """
    print("Port: " + arguments + " " + str(utils.scan(IP_ADDRESS, arguments)))

if __name__ == "__main__":
    IP_ADDRESS = sys.argv[1]
    START_PORT = int(sys.argv[2])
    if len(sys.argv) == 4:
        END_PORT = int(sys.argv[3])
        if START_PORT > END_PORT:
            raise ValueError("End Port value must come after Start Port")
    if utils.verify_ipv4(IP_ADDRESS):
        ports = range(START_PORT, END_PORT + 1)
        list_of_ports = []

        for idx, val in enumerate(ports):
            proc = multiprocessing.Process(target=scan, args=(str(val),))
            list_of_ports.append(proc)
            proc.start()

        for proc in list_of_ports:
            proc.join()
        
    else:
        print(" ".join(sys.argv))
        print("Not Valid Data")
