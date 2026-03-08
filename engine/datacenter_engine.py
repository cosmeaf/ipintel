# /opt/ipintel/engine/datacenter_engine.py

ASN_FILE = "/opt/ipintel/datacenter/datacenter_asn.txt"


def is_datacenter(asn):

    try:

        with open(ASN_FILE) as f:

            for line in f:

                if line.strip() == str(asn):
                    return True

    except Exception:
        pass

    return False