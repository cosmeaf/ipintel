# /opt/ipintel/engine/proxy_engine.py

PROXY_FILE = "/opt/ipintel/proxy/proxy_list.txt"


def is_proxy(ip):

    try:

        with open(PROXY_FILE) as f:

            for line in f:

                if line.strip().startswith(ip):
                    return True

    except Exception:
        pass

    return False