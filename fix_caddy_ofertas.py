import paramiko
import time

def execute_command(ssh, command):
    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read().decode('utf-8', errors='ignore')
    err = stderr.read().decode('utf-8', errors='ignore')
    if err:
        print(f"STDERR: {err}")
    return out

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('76.13.228.159', username='root', password='Walysson2003@', timeout=10)
    
    caddyfile = execute_command(ssh, "cat /root/promocao-whats/Caddyfile")
    if "escola.wrmusicpro.com.br" not in caddyfile:
        append_str = "\n\nescola.wrmusicpro.com.br {\n    root * /srv/landpage\n    file_server\n}\n"
        new_caddyfile = caddyfile.strip() + append_str
        
        cmd = f"cat << 'EOF' > /root/promocao-whats/Caddyfile\n{new_caddyfile}\nEOF"
        execute_command(ssh, cmd)
        print("Updated Caddyfile.")
    
    dc = execute_command(ssh, "cat /root/promocao-whats/docker-compose.yml")
    if "/root/wr-music-app/landpage:/srv/landpage" not in dc:
        new_dc = dc.replace("- ./Caddyfile:/etc/caddy/Caddyfile", "- ./Caddyfile:/etc/caddy/Caddyfile\n      - /root/wr-music-app/landpage:/srv/landpage")
        cmd2 = f"cat << 'EOF' > /root/promocao-whats/docker-compose.yml\n{new_dc}\nEOF"
        execute_command(ssh, cmd2)
        print("Updated docker-compose.yml.")
    
    print("Recreating caddy container...")
    execute_command(ssh, "cd /root/promocao-whats && docker compose up -d --force-recreate caddy")
    print("Fixed Caddy config for escola.wrmusicpro.com.br")
    
    ssh.close()
except Exception as e:
    print(f"Error: {e}")
