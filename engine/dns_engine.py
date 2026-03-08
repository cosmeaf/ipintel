# /opt/ipintel/engine/dns_engine.py

import socket


def reverse_dns(ip):

    try:
        host, _, _ = socket.gethostbyaddr(ip)
        return host
    except Exception:
        return None