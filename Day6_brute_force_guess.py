# Real user credentials
user = {
    "username": "admin",
    "password": "secure123"
}

# Simulated attacker's password guesses
guessed_passwords = ["123456", "admin", "letmein", "password", "secure123", "qwerty"]

# Initialize counters and log
attempts = 0
failed_attempts = []

# Loop through each guessed password
for guessed_password in guessed_passwords:
    attempts += 1
    print(f"Trying password: {guessed_password}")
    
    if guessed_password == user["password"]:
        print(f"✅ Password found: {guessed_password}")
        break
    else:
        failed_attempts.append(guessed_password)

# Final summary
print(f"\n🔁 Total attempts made: {attempts}")
print(f"❌ Failed attempts: {failed_attempts}")
