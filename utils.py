#!/usr/bin/env python3
"""
Provides utility methods for scanning TCP connections
"""
import re

def verify_ipv4(ip_address):
    """Verifies that the ip is a valid IPv4 address"""
    ip_regex = re.compile(r"""^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$""", re.X)
    return ip_regex.match(ip_address)

def scan(ip_address, port):
    """Scans the port to see if the port is open"""
