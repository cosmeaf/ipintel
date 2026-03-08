#!/usr/bin/env python3

import sys
import os
import socket
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from engine.whois_engine import lookup_whois


def get_local_ip():
    try:
        ip = subprocess.check_output(["hostname", "-I"]).decode().split()[0]
        return ip
    except Exception:
        return None


def test_ip(ip):

    print("")
    print("================================")
    print("WHOIS TEST")
    print("IP:", ip)
    print("================================")

    data = lookup_whois(ip)

    if not data:
        print("FAIL: WHOIS lookup failed")
        return False

    # mostrar apenas primeiras linhas
    lines = data.splitlines()

    for line in lines:
        if any(k in line.lower() for k in ["org", "netname", "country", "descr"]):
            print(line)

    print("")
    print("STATUS: OK")

    return True


def test_domain(domain):

    print("")
    print("================================")
    print("DOMAIN WHOIS TEST")
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
    print("=========== IPINTEL WHOIS TEST ===========")

    test_ip("8.8.8.8")

    local_ip = get_local_ip()
    if local_ip:
        test_ip(local_ip)

    test_domain("google.com")

    print("")