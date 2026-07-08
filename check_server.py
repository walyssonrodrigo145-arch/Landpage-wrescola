import paramiko

def execute_command(ssh, command):
    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read().decode('utf-8', errors='ignore')
    return out

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('76.13.228.159', username='root', password='Walysson2003@', timeout=10)
    
    caddyfile = execute_command(ssh, "cat /root/wr-music-app/Caddyfile")
    print("--- Caddyfile ---")
    print(caddyfile)
    
    dc = execute_command(ssh, "cat /root/wr-music-app/docker-compose.yml")
    print("--- docker-compose.yml ---")
    print(dc)
    
    dps = execute_command(ssh, "docker ps -a")
    print("--- Docker PS ---")
    print(dps)
            
    ssh.close()
except Exception as e:
    print(f"Error: {e}")
