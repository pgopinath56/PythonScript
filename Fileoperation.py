try:
    with open('servers.txt') as file:
        for line in file:
            servers = line.strip().split(",")
            print(servers)
    for server in servers:
        print(f"Connecting to {server}...")
except Exception as e:
    print(e)

with open('env.txt') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=')
            print(f"{key} = {value}")
