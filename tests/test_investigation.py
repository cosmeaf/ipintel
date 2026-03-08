#!/usr/bin/env python3

import sys
import os
import socket
import subprocess
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from engine.investigation_engine import investigate_ip


def get_local_ip():
    try:
        ip = subprocess.check_output(["hostname", "-I"]).decode().split()[0]
        return ip
    except Exception:
        return None


def run_test(ip):

    print("")
    print("================================")
    print("INVESTIGATION TEST")
    print("IP:", ip)
    print("================================")

    data = investigate_ip(ip)

    if not data:
        print("FAIL: investigation returned nothing")
        return False

    print(json.dumps(data, indent=4))

    print("")
    print("STATUS: OK")

    return True


def test_domain(domain):

    print("")
    print("================================")
    print("DOMAIN INVESTIGATION TEST")
    print("DOMAIN:", domain)
    print("================================")

    try:
        ip = socket.gethostbyname(domain)
        print("Resolved IP:", ip)
        return run_test(ip)

    except Exception as e:
        print("DNS ERROR:", e)
        return False


if __name__ == "__main__":

    print("")
    print("=========== IPINTEL FULL INVESTIGATION TEST ===========")

    # IP conhecido
    run_test("8.8.8.8")

    # IP local
    local_ip = get_local_ip()
    if local_ip:
        run_test(local_ip)

    # domínio
    test_domain("google.com")

    print("")