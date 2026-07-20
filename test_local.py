import paramiko
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('76.13.228.159', username='root', password='Walysson2003@', timeout=10)
    
    stdin, stdout, stderr = ssh.exec_command("cat /root/promocao-whats/Caddyfile && echo '---' && cat /root/promocao-whats/docker-compose.yml")
    print(stdout.read().decode('utf-8'))
    ssh.close()
except Exception as e:
    print(e)
