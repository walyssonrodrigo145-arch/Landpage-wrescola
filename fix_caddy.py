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
    if "escola.wrmusicpro.com.br" not in caddyfile:
        append_str = "\n\nescola.wrmusicpro.com.br {\n    root * /srv/landpage\n    file_server\n}\n"
        new_caddyfile = caddyfile.strip() + append_str
        
        cmd = f"cat << 'EOF' > /root/wr-music-app/Caddyfile\n{new_caddyfile}\nEOF"
        execute_command(ssh, cmd)
        
        execute_command(ssh, "docker exec wr-music-app-caddy-1 caddy reload --config /etc/caddy/Caddyfile")
        print("Fixed Caddyfile and reloaded Caddy.")
    else:
        print("Caddyfile already has escola.")
        
    ssh.close()
except Exception as e:
    print(f"Error: {e}")
