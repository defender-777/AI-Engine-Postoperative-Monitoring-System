def compute_risk_score(wound_label, wound_conf, vitals_alerts):
    score = 0

    if wound_label == "healthy": score += 0
    elif wound_label == "mild_infection": score += 40
    elif wound_label == "severe_infection": score += 80

    score += wound_conf * 20

    for a in vitals_alerts:
        if "Fever" in a: score += 15
        if "Heart Rate" in a: score += 10
        if "Oxygen" in a: score += 25
        if "AI" in a: score += 10

    return min(score, 100)

def risk_level(score):
    return "HIGH" if score >= 70 else "MODERATE" if score >= 40 else "LOW"

def compute_full_risk(wound_pred, vitals_alerts):
    wound_label = wound_pred["label"]
    wound_conf  = wound_pred["confidence"]

    score = compute_risk_score(wound_label, wound_conf, vitals_alerts)
    level = risk_level(score)

    reasons = [
        f"Wound classified as {wound_label} (confidence {round(wound_conf, 2)})"
    ] + vitals_alerts

    return {
        "risk_score": float(score),
        "risk_level": level,
        "reasons": reasons,
        "explanation": " | ".join(reasons)
    }
