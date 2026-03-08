#!/usr/bin/env python3

import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from engine.risk_engine import calculate_risk


def run_test(name, data):

    print("")
    print("================================")
    print("RISK TEST:", name)
    print("================================")

    score, reasons = calculate_risk(data)

    print("INPUT:", data)
    print("SCORE:", score)
    print("REASONS:", reasons)

    print("")
    print("STATUS: OK")


if __name__ == "__main__":

    print("")
    print("=========== IPINTEL RISK TEST ===========")

    # caso 1 normal
    run_test("normal_ip", {
        "tor": False,
        "proxy": False,
        "datacenter": False,
        "country": "US"
    })

    # caso 2 datacenter
    run_test("datacenter_ip", {
        "tor": False,
        "proxy": False,
        "datacenter": True,
        "country": "US"
    })

    # caso 3 proxy
    run_test("proxy_ip", {
        "tor": False,
        "proxy": True,
        "datacenter": False,
        "country": "US"
    })

    # caso 4 tor
    run_test("tor_ip", {
        "tor": True,
        "proxy": False,
        "datacenter": False,
        "country": "US"
    })

    # caso 5 tudo suspeito
    run_test("high_risk", {
        "tor": True,
        "proxy": True,
        "datacenter": True,
        "country": None
    })

    print("")