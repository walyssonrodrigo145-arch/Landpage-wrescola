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
    
    dps = execute_command(ssh, "docker ps -a | grep caddy")
    print("--- Docker PS (caddy) ---")
    print(dps)

    logs = execute_command(ssh, "docker logs wr-music-app-caddy-1 --tail 30")
    print("--- Caddy Logs ---")
    print(logs)

    curl_test = execute_command(ssh, "curl -I -s http://escola.wrmusicpro.com.br")
    print("--- Curl Test ---")
    print(curl_test)
    
    ssh.close()
except Exception as e:
    print(f"Error: {e}")
