#!/usr/bin/env python3
"""
Port scanner that attempts to make a
TCP connection
"""
import argparse
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
    END = int(sys.argv[3])
    if START > END:
        raise ValueError("Start Port cannot come after End Port")
