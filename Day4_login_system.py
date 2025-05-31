# Login System with Attempts Limit
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "correct_username" and password == "correct_password":
        print("✅ Access Granted. Welcome!")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong credentials. Attempts left: {attempts}")

        if attempts == 0:
            print("🔒 Access denied. Account locked.")