SEVERITY_SCORE = {
    "CRITICAL": 100,
    "HIGH": 80,
    "MEDIUM": 60,
    "LOW": 30,
    "INFO": 10,
    "UNKNOWN": 0
}


def calculate_risk(results):

    if not results:
        return 0

    score = 0

    for finding in results:

        score += SEVERITY_SCORE.get(
            finding["severity"].upper(),
            0
        )

    return round(score / len(results))