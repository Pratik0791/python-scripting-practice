# ip count tracker
# This script tracks the occurrence of IP addresses and identifies suspicious ones based on their frequency.
ips = ["192.168.1.2", "10.0.0.5", "192.168.1.2", "172.16.0.1", "10.0.0.5", "8.8.8.8"]
print("IP Addresses:")
for ip in (ips):
    print(ip,sep=" ][ ", end=' ')
ips_dict = {}
for ip in ips:
    if ip in ips_dict:
        ips_dict[ip] += 1
    else:
        ips_dict[ip] = 1
print("\nIP Address Count:")
for ip, count in ips_dict.items():
    print(f"{ip}: {count} time(s)")
print("\nSuspicious IP Addresses:")
for ip, count in ips_dict.items():
    if count > 1:
        print(f"{ip} is suspicious with {count} occurrences.")
