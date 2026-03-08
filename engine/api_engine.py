# /opt/ipintel/engine/api_engine.py

import requests


def api_lookup(ip):

    try:

        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)

        return r.json()

    except Exception:

        return {}