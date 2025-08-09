def analyze_risk(answer):
    missing_info_flag = "MISSING" in answer.upper()
    confidence = 95 if not missing_info_flag else 75

    return f"Confidence: {confidence}%\nMissing Information: {missing_info_flag}"
