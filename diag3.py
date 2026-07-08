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
    
    files = execute_command(ssh, "ls -la /root/wr-music-app/landpage")
    print("--- Landpage files ---")
    print(files)

    ssh.close()
except Exception as e:
    print(f"Error: {e}")
