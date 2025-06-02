# Registered users (like a simple database)
users_db = {
    "admin": "admin@123",
    "alice": "wonderland",
    "bob": "builder99"
}

# Login attempt tracker
login_attempts = {}

# Function to mask passwords in logs
def mask_sensitive_data(**kwargs):
    masked = {}
    for key, value in kwargs.items():
        if key == "password":
            masked[key] = "*" * len(value)
        else:
            masked[key] = value
    return masked

# Login function using *args and **kwargs
def login_system(*usernames, **credentials):
    for username in usernames:
        attempts = login_attempts.get(username, 0)
        if attempts >= 3:
            print(f"❌ Account '{username}' is locked due to too many failed attempts.\n")
            continue

        password_input = credentials.get("password")
        real_password = users_db.get(username)

        if real_password is None:
            print(f"⚠️  User '{username}' not found.\n")
            continue

        if password_input == real_password:
            print(f"✅ Welcome, {username}!")
            login_attempts[username] = 0  # Reset attempts
        else:
            attempts += 1
            login_attempts[username] = attempts
            print(f"❌ Incorrect password for {username}. Attempt {attempts}/3")
            if attempts == 3:
                print(f"🚫 Account '{username}' locked!\n")

        # Log login attempt (with masked data)
        log_entry = mask_sensitive_data(username=username, password=password_input)
        print(f"🔒 Login Log: {log_entry}\n")

# -------- Test Run --------
# Call the function with *args and **kwargs
login_system("alice", password="wrongpass")
login_system("alice", password="wonderland")
login_system("admin", password="admin@123")
login_system("bob", password="wrong1")
login_system("bob", password="wrong2")
login_system("bob", password="wrong3")
login_system("bob", password="builder99")
