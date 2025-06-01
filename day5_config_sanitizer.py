config = {
  "firewall": "enabled",
  "ssh": "open",
  "dns": "8.8.8.8",
  "password": "admin123",
  "secret_key": "XYZ123456",
}
# This script sanitizes a configuration dictionary by removing sensitive information.
santized_tuple = tuple({key: value for key, value in config.items() if key not in ["password", "secret_key"]})
# Print the sanitized configuration 
print("Sanitized Configuration:")
print(santized_tuple)
