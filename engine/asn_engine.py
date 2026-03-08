# /opt/ipintel/engine/asn_engine.py

import geoip2.database

DB_ASN = "/opt/ipintel/geoip/GeoLite2-ASN.mmdb"


def lookup_asn(ip):

    try:

        with geoip2.database.Reader(DB_ASN) as reader:

            res = reader.asn(ip)

            return {
                "asn": res.autonomous_system_number,
                "asn_org": res.autonomous_system_organization,
            }

    except Exception:
        return {}