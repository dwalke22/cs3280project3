#!/usr/bin/env python3
"""
Port scanner that attempts to make a
TCP connection
"""
import multiprocessing
import sys

__author__ = "David Walker"
__version__ = "Fall 2020"

def main():
    """The Main entry point for the application"""
    ip_address = sys.argv[1]
    start_port = sys.argv[2]
    print(ip_address)
    print(start_port)
    if len(sys.argv) == 4:
        end_port = sys.argv[3]
        print(end_port)


if __name__ == "__main__":
    main()
