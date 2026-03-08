#!/usr/bin/env python3

import sys
import os
import socket
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from engine.geoip_engine import lookup_geo


def get_local_ip():
    try:
        ip = subprocess.check_output(["hostname", "-I"]).decode().split()[0]
        return ip
    except Exception:
        return None


def test_ip(ip):

    print("")
    print("================================")
    print("GEOIP TEST")
    print("IP:", ip)
    print("================================")

    data = lookup_geo(ip)

    if not data:
        print("FAIL: no geo data returned")
        return

    print("Country :", data.get("country"))
    print("City    :", data.get("city"))
    print("Lat     :", data.get("lat"))
    print("Lon     :", data.get("lon"))
    print("")


def test_domain(domain):

    print("")
    print("================================")
    print("DOMAIN TEST")
    print("DOMAIN:", domain)
    print("================================")

    try:
        ip = socket.gethostbyname(domain)
        print("Resolved IP:", ip)
        test_ip(ip)
    except Exception as e:
        print("DNS ERROR:", e)


if __name__ == "__main__":

    print("")
    print("=========== IPINTEL GEOIP TEST ===========")

    # 1 IP conhecido
    test_ip("8.8.8.8")

    # 2 IP local
    local_ip = get_local_ip()
    if local_ip:
        test_ip(local_ip)

    # 3 domínio
    test_domain("google.com")

    print("")