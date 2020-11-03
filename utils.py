#!/usr/bin/env python3
"""
Provides utility methods for scanning TCP connections
"""
import re
from socket import AF_INET, SOCK_STREAM, socket
import multiprocessing

def verify_ipv4(ip_address):
    """Verifies that the ip is a valid IPv4 address"""
    ip_regex = re.compile(r"""^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$""", re.X)
    return ip_regex.match(ip_address)

def scan(ip_address, start_port, end_port):
    """Scans all ports"""
    ports = {}
    scanner = socket(AF_INET, SOCK_STREAM)
    for port in range(start_port, end_port + 1):
        val = (ip_address, port,)
        is_open = multiprocessing.Process(target=scanner.connect_ex, args=(val,))
        ports[str(port)] = is_open
    scanner.close()
    return ports
