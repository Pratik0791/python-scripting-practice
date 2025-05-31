# access_control.py

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "letmein":
    print("Access granted.")
elif username == "admin":
    print("Wrong password.")
else:
    print("Unknown user.")
