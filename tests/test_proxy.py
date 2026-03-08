#!/usr/bin/env python3

import sys
import os
import socket
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from engine.proxy_engine import is_proxy


def get_local_ip():
    try:
        ip = subprocess.check_output(["hostname", "-I"]).decode().split()[0]
        return ip
    except Exception:
        return None


def test_ip(ip):

    print("")
    print("================================")
    print("PROXY TEST")
    print("IP:", ip)
    print("================================")

    proxy = is_proxy(ip)

    print("PROXY DETECTED:", proxy)

    print("")
    print("STATUS: OK")

    return True


def test_domain(domain):

    print("")
    print("================================")
    print("DOMAIN PROXY TEST")
    print("DOMAIN:", domain)
    print("================================")

    try:
        ip = socket.gethostbyname(domain)
        print("Resolved IP:", ip)
        return test_ip(ip)

    except Exception as e:
        print("DNS ERROR:", e)
        return False


if __name__ == "__main__":

    print("")
    print("=========== IPINTEL PROXY TEST ===========")

    # IP conhecido
    test_ip("8.8.8.8")

    # IP local
    local_ip = get_local_ip()
    if local_ip:
        test_ip(local_ip)

    # domínio
    test_domain("google.com")

    print("")