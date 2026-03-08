# /opt/ipintel/engine/investigation_engine.py

from .geoip_engine import lookup_geo
from .asn_engine import lookup_asn
from .tor_engine import is_tor
from .proxy_engine import is_proxy
from .datacenter_engine import is_datacenter
from .dns_engine import reverse_dns
from .whois_engine import lookup_whois
from .api_engine import api_lookup
from .risk_engine import calculate_risk


def investigate_ip(ip):

    data = {
        "ip": ip,
        "country": None,
        "city": None,
        "region": None,
        "latitude": None,
        "longitude": None,
        "asn": None,
        "asn_org": None,
        "tor": False,
        "proxy": False,
        "datacenter": False,
        "rdns": None,
        "whois": None,
        "risk_score": 0,
        "risk_reasons": []
    }

    # ---------------------------------------------------------
    # GEOIP LOCAL
    # ---------------------------------------------------------

    geo = lookup_geo(ip) or {}

    if geo:
        data.update(geo)

    # ---------------------------------------------------------
    # ASN LOCAL
    # ---------------------------------------------------------

    asn = lookup_asn(ip) or {}

    if asn:
        data.update(asn)

    # ---------------------------------------------------------
    # TOR / PROXY
    # ---------------------------------------------------------

    try:
        data["tor"] = is_tor(ip)
    except Exception:
        data["tor"] = False

    try:
        data["proxy"] = is_proxy(ip)
    except Exception:
        data["proxy"] = False

    # ---------------------------------------------------------
    # DATACENTER DETECTION
    # ---------------------------------------------------------

    if data.get("asn"):
        try:
            data["datacenter"] = is_datacenter(data["asn"])
        except Exception:
            data["datacenter"] = False

    # ---------------------------------------------------------
    # REVERSE DNS
    # ---------------------------------------------------------

    try:
        data["rdns"] = reverse_dns(ip)
    except Exception:
        data["rdns"] = None

    # ---------------------------------------------------------
    # FALLBACK API (SE GEOIP FALHAR)
    # ---------------------------------------------------------

    if not data.get("country"):

        try:
            api = api_lookup(ip)

            if api:

                data["country"] = api.get("country_name") or data["country"]
                data["city"] = api.get("city") or data["city"]
                data["region"] = api.get("region") or data["region"]
                data["latitude"] = api.get("latitude") or data["latitude"]
                data["longitude"] = api.get("longitude") or data["longitude"]

        except Exception:
            pass

    # ---------------------------------------------------------
    # WHOIS
    # ---------------------------------------------------------

    try:
        data["whois"] = lookup_whois(ip)
    except Exception:
        data["whois"] = None

    # ---------------------------------------------------------
    # RISK SCORE
    # ---------------------------------------------------------

    score, reasons = calculate_risk(data)

    data["risk_score"] = score
    data["risk_reasons"] = reasons

    return data