#!/usr/bin/env python3
"""
Port scanner that attempts to make a
TCP connection
"""
import sys
from socket import AF_INET, SOCK_STREAM, socket
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

if __name__ == "__main__":
    IP_ADDRESS = sys.argv[1]
    if not utils.verify_ipv4(IP_ADDRESS):
        print("Not Valid IP")
    START = int(sys.argv[2])
    if len(sys.argv) == 4:
        END = int(sys.argv[3])
        for i in range(START, END):
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((IP_ADDRESS, i))
            print("Port " + str(i) + " " + str(conn))
            s.close()
    else:
        for i in range(START,):
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((IP_ADDRESS, i))
            print("Port " + str(i) + " " + str(conn))
