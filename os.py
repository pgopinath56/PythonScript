import os
import sys

Host = os.getenv("HOSTNAME")
username = os.getenv("LANG")

print(f"the hostname is {Host}")
print(f"{username}")

env_name = sys.argv[1]
rel= sys.argv[2]
print(f"The env is {env_name}")
print(f"{rel}")
