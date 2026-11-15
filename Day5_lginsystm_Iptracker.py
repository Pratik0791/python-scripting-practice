"""Day 5: analyze login events by source IP address.

This script analyzes the sample events below. It does not discover a user's
real public IP address or monitor live network traffic.
"""

from collections import Counter
from ipaddress import ip_address
from typing import Any

LOGIN_LOGS: list[dict[str, Any]] = [
    {"username": "admin", "ip": "192.168.1.1"},
    {"username": "admin", "ip": "10.0.0.2"},
    {"username": "root", "ip": "192.168.1.1"},
    {"username": "guest", "ip": "10.0.0.2"},
    {"username": "admin", "ip": "10.0.0.2"},
]

SUSPICIOUS_ATTEMPT_THRESHOLD = 2


def analyze_login_logs(
    logs: list[dict[str, Any]], threshold: int = SUSPICIOUS_ATTEMPT_THRESHOLD
) -> tuple[Counter[str], list[str], list[int]]:
    """Count valid source IPs and return suspicious IPs and invalid row indexes."""
    if threshold < 1:
        raise ValueError("threshold must be at least 1")

    ip_counts: Counter[str] = Counter()
    invalid_rows: list[int] = []

    for row_number, log in enumerate(logs, start=1):
        raw_ip = log.get("ip")
        if not isinstance(raw_ip, str):
            invalid_rows.append(row_number)
            continue

        try:
            normalized_ip = str(ip_address(raw_ip.strip()))
        except ValueError:
            invalid_rows.append(row_number)
            continue

        ip_counts[normalized_ip] += 1

    suspicious_ips = sorted(
        ip for ip, count in ip_counts.items() if count > threshold
    )
    return ip_counts, suspicious_ips, invalid_rows


def main() -> None:
    ip_counts, suspicious_ips, invalid_rows = analyze_login_logs(LOGIN_LOGS)

    print("Unique valid IP addresses:")
    for ip in sorted(ip_counts):
        print(f"- {ip}")

    print("\\nLogin attempts per IP:")
    for ip, count in sorted(ip_counts.items()):
        print(f"{ip}: {count}")

    print(
        f"\\nSuspicious IPs (more than {SUSPICIOUS_ATTEMPT_THRESHOLD} attempts):"
    )
    if suspicious_ips:
        for ip in suspicious_ips:
            print(f"- {ip}")
    else:
        print("None")

    if invalid_rows:
        print("\\nRows with missing or invalid IP addresses:")
        for row_number in invalid_rows:
            print(f"- Row {row_number}")


if __name__ == "__main__":
    main()
