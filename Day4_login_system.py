"""Day 4: a basic login system with password hashing and attempt limits.

Demo account:
    username: admin
    password: toor

The lockout counter is in memory and resets when this script exits.
For real applications, store password hashes and lockout state in a database.
"""

import getpass
import hashlib
import hmac

USERNAME = "admin"
PASSWORD_SALT = bytes.fromhex("a5c4b10f9e7d2a6381f04c6b7d9e2f10")
PASSWORD_HASH = bytes.fromhex(
    "540fda037a800ccb52f3aa309495c2cb8dc5d255b294f8fc555f057539fda2c4"
)
PBKDF2_ITERATIONS = 600_000
MAX_ATTEMPTS = 3


def verify_password(password: str) -> bool:
    """Return True only when password matches the stored PBKDF2 hash."""
    candidate_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        PASSWORD_SALT,
        PBKDF2_ITERATIONS,
    )
    return hmac.compare_digest(candidate_hash, PASSWORD_HASH)


def authenticate(username: str, password: str) -> bool:
    """Check the demo username and password without revealing which failed."""
    username_matches = hmac.compare_digest(
        username.encode("utf-8"), USERNAME.encode("utf-8")
    )
    password_matches = verify_password(password)
    return username_matches and password_matches


def main() -> None:
    attempts_remaining = MAX_ATTEMPTS

    while attempts_remaining > 0:
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ")

        if authenticate(username, password):
            print("Login successful.")
            return

        attempts_remaining -= 1
        print(f"Invalid username or password. Attempts remaining: {attempts_remaining}")

    print("Account locked for this program run after too many failed attempts.")


if __name__ == "__main__":
    main()
