"""Day 5: safely redact sensitive values from configuration data.

This is a demonstration utility. It does not remove secrets from Git history.
If real credentials were committed, rotate them and clean repository history.
"""

from collections.abc import Mapping
from typing import Any

SENSITIVE_KEY_FRAGMENTS = (
    "password",
    "secret",
    "token",
    "api_key",
    "apikey",
    "credential",
    "private_key",
)


def is_sensitive_key(key: object) -> bool:
    """Check key names case-insensitively for common secret indicators."""
    normalized_key = str(key).strip().lower().replace("-", "_")
    return any(fragment in normalized_key for fragment in SENSITIVE_KEY_FRAGMENTS)


def sanitize_value(value: Any) -> Any:
    """Recursively sanitize mappings and sequences without modifying input data."""
    if isinstance(value, Mapping):
        return {
            key: "[REDACTED]" if is_sensitive_key(key) else sanitize_value(item)
            for key, item in value.items()
        }

    if isinstance(value, list):
        return [sanitize_value(item) for item in value]

    if isinstance(value, tuple):
        return tuple(sanitize_value(item) for item in value)

    return value


def sanitize_config(config: Mapping[str, Any]) -> dict[str, Any]:
    """Return a sanitized copy of a configuration mapping."""
    if not isinstance(config, Mapping):
        raise TypeError("config must be a mapping")

    return sanitize_value(config)


def main() -> None:
    # Use placeholders only. Never put real credentials in source code.
    config = {
        "firewall": "enabled",
        "ssh": "open",
        "dns": "8.8.8.8",
        "password": "example-only",
        "secret_key": "example-only",
        "service": {
            "api_token": "example-only",
            "region": "ap-south-1",
        },
    }

    sanitized_config = sanitize_config(config)
    print("Sanitized configuration:")
    print(sanitized_config)


if __name__ == "__main__":
    main()
