from collections import defaultdict


def group_findings(findings):

    groups = defaultdict(list)

    for finding in findings:
        groups[finding["rule_id"]].append(finding)

    return groups