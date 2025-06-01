login_logs = [
    {"username": "admin", "ip": "192.168.1.1"},
    {"username": "admin", "ip": "10.0.0.2"},
    {"username": "root", "ip": "192.168.1.1"},
    {"username": "guest", "ip": "10.0.0.2"},
    {"username": "admin", "ip": "10.0.0.2"}
]

# Print all unique IPs used
unique_ips = set(log['ip'] for log in login_logs)
print("Unique IPs used:")
for ip in unique_ips:
    print(ip)

# Print number of login attempts from each IP
ip_attempts = {}
for log in login_logs:
    ip = log['ip']
    ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

print("\nNumber of login attempts from each IP:")
for ip, count in ip_attempts.items():
    print(f"{ip}: {count}")

# Print list of suspicious IPs (those with >2 attempts)
suspicious_ips = [ip for ip, count in ip_attempts.items() if count > 2]
print("\nSuspicious IPs (more than 2 attempts):")
for ip in suspicious_ips:
    print(ip)
