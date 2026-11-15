"""A small access-control exercise using a salted password hash.

Demo account:
    username: admin
    password: letmein

This is still a teaching example: production systems should load users and
password hashes from a protected database and use an established auth library.
"""

import getpass
import hashlib
import hmac

USERNAME = "admin"
PASSWORD_SALT = bytes.fromhex("1ed0e87600fd548b1546aa9f2645d318")
PASSWORD_HASH = bytes.fromhex(
    "256b27c43b18316268df486e2835c447416553426c2e76f461e129b00f220a93"
)
PBKDF2_ITERATIONS = 600_000


def verify_password(password: str) -> bool:
    """Verify a password against the stored PBKDF2-HMAC-SHA256 hash."""
    candidate_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        PASSWORD_SALT,
        PBKDF2_ITERATIONS,
    )
    return hmac.compare_digest(candidate_hash, PASSWORD_HASH)


def main() -> None:
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")

    if username != USERNAME:
        print("Invalid username or password.")
        return

    if verify_password(password):
        print("Access granted.")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
