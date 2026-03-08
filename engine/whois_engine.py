# /opt/ipintel/engine/whois_engine.py

import subprocess


def lookup_whois(ip):

    try:

        out = subprocess.check_output(["whois", ip]).decode()

        return out

    except Exception:

        return None