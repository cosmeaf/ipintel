# /opt/ipintel/engine/tor_engine.py

TOR_FILE = "/opt/ipintel/tor/exit_nodes.txt"


def is_tor(ip):

    try:

        with open(TOR_FILE) as f:

            for line in f:

                if line.strip() == ip:
                    return True

    except Exception:
        pass

    return False