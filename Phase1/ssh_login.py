import paramiko

# Target machine details
host = "192.168.0.172"
port = 22

# Read credentials from files
with open("username.txt", "r") as f:
    username = f.read().strip()
with open("passwords.txt", "r") as f:
    password = f.read().strip()

# Initialize the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the host
    client.connect(hostname=host, port=port, username=username, password=password)
    print(f"[+] Successfully connected to {host}")
    
    # Execute the 'whoami' command
    stdin, stdout, stderr = client.exec_command("whoami")
    output = stdout.read().decode().strip()
    print(f"[+] Command output: {output}")
    
    # Close the connection
    client.close()
except Exception as e:
    print(f"[-] Connection failed: {e}")
