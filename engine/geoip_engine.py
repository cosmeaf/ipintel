# /opt/ipintel/engine/geoip_engine.py

import geoip2.database

DB_CITY = "/opt/ipintel/geoip/GeoLite2-City.mmdb"
DB_ASN = "/opt/ipintel/geoip/GeoLite2-ASN.mmdb"


def lookup_geo(ip):

    try:

        with geoip2.database.Reader(DB_CITY) as reader:

            res = reader.city(ip)

            return {
                "country": res.country.name,
                "city": res.city.name or "",
                "latitude": res.location.latitude,
                "longitude": res.location.longitude,
            }

    except Exception:
        return {}