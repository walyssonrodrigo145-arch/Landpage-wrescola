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
    
    dc = execute_command(ssh, "cat /root/wr-music-app/docker-compose.yml")
    if "./landpage:/srv/landpage" not in dc:
        dc = dc.replace("- ./Caddyfile:/etc/caddy/Caddyfile", "- ./Caddyfile:/etc/caddy/Caddyfile\n      - ./landpage:/srv/landpage")
        
        cmd = f"cat << 'EOF' > /root/wr-music-app/docker-compose.yml\n{dc}\nEOF"
        execute_command(ssh, cmd)
        
        execute_command(ssh, "cd /root/wr-music-app && docker compose up -d --force-recreate caddy")
        print("Fixed docker-compose and restarted Caddy.")
    else:
        print("Volume was already there.")
        
    ssh.close()
except Exception as e:
    print(f"Error: {e}")
