#!/usr/bin/env python3
"""Simple TCP Port Availability Checker."""
import socket
import sys

def check_port(host, port, timeout=2.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8080
    status = "OPEN" if check_port(host, port) else "CLOSED"
    print(f"Port {port} on {host}: {status}")
