lgin_credential = {
    "username": "admin",
    "password": "toor",
    "login_attempts": 3
}

attempts = lgin_credential["login_attempts"]

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == lgin_credential["username"] and password == lgin_credential["password"]:
        print("Login successful!")
        lgin_credential["status"] = "active"
        break
    else:
        attempts -= 1
        lgin_credential["login_attempts"] = attempts
        print(f"Login failed. {attempts} attempts remaining.")

if attempts == 0:
    lgin_credential["status"] = "locked"
    print("Account locked due to too many failed attempts.")

print("Final User Info:", lgin_credential)
