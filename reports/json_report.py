import json
from pathlib import Path


def save_report(report):

    reports = Path("reports")

    reports.mkdir(exist_ok=True)

    path = reports / "report.json"

    with open(path, "w") as f:

        json.dump(report, f, indent=4)

    return str(path)