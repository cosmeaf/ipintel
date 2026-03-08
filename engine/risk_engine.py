# ipintel/engine/risk_engine.py


def calculate_risk(data):

    score = 0
    reasons = []

    if data.get("tor"):
        score += 70
        reasons.append("tor")

    if data.get("proxy"):
        score += 40
        reasons.append("proxy")

    if data.get("datacenter"):
        score += 30
        reasons.append("datacenter")

    if not data.get("country"):
        score += 10
        reasons.append("unknown_geo")

    return score, reasons