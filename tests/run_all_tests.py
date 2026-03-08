#!/usr/bin/env python3

import subprocess
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_DIR = os.path.join(BASE_DIR, "tests")

tests = [
    "test_geoip.py",
    "test_asn.py",
    "test_datacenter.py",
    "test_tor.py",
    "test_proxy.py",
    "test_dns.py",
    "test_whois.py",
    "test_risk.py",
    "test_investigation.py",
]

print("")
print("===========================================")
print("IPINTEL TEST SUITE")
print("===========================================")

all_ok = True

for test in tests:

    path = os.path.join(TEST_DIR, test)

    print("")
    print("-------------------------------------------")
    print(f"RUNNING: {test}")
    print("-------------------------------------------")

    result = subprocess.run(
        ["python3", path],
        cwd=BASE_DIR
    )

    if result.returncode == 0:
        print(f"[OK] {test}")
    else:
        print(f"[FAIL] {test}")
        all_ok = False

print("")
print("===========================================")

if all_ok:
    print("ALL TESTS PASSED")
    sys.exit(0)
else:
    print("SOME TESTS FAILED")
    sys.exit(1)