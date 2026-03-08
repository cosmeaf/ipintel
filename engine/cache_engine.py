# ipintel/engine/cache_engine.py

import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "/opt/ipintel/cache/ip_cache.json"


def load_cache():

    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE) as f:
        return json.load(f)


def save_cache(cache):

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def get_cached(ip):

    cache = load_cache()

    if ip not in cache:
        return None

    entry = cache[ip]

    ts = datetime.fromisoformat(entry["timestamp"])

    if datetime.utcnow() - ts > timedelta(hours=24):
        return None

    return entry["data"]


def set_cache(ip, data):

    cache = load_cache()

    cache[ip] = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": data,
    }

    save_cache(cache)