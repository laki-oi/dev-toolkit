#!/usr/bin/env python3
"""System information utility script."""
import os
import platform
import sys

def get_system_summary():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "python_version": sys.version.split()[0],
        "cpu_count": os.cpu_count()
    }

if __name__ == "__main__":
    for k, v in get_system_summary().items():
        print(f"{k.capitalize()}: {v}")
