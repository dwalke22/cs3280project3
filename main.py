#!/usr/bin/env python3
"""
Port scanner that attempts to make a
TCP connection
"""
import sys
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

if __name__ == "__main__":
    IP_ADDRESS = sys.argv[1]
    if not utils.verify_ipv4(IP_ADDRESS):
        print("Not Valid IP")
    START = int(sys.argv[2])
    if len(sys.argv) == 4:
        if "[" in sys.argv[3]:
            END_PORT = sys.argv[3].replace("[", "")
            END_PORT = sys.argv[3].replace("]", "")
            END = int(END_PORT)
        else:
            END = int(sys.argv[3])
    else:
        END = START + 1
    if START > END:
        raise ValueError("Start Port cannot come after End Port")
    PORTS = utils.scan(IP_ADDRESS, START, END)
