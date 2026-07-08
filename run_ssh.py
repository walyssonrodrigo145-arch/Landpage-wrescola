import paramiko
import os

local_dir = r"c:\Users\walysson\Documents\cool-nobel"
remote_dir = "/root/wr-music-app/landpage"

files_to_upload = ["index.html", "styles.css", "script.js", "image1.jpg", "image2.jpg", "logo.png"]

try:
    print("Connecting to VPS...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('76.13.228.159', username='root', password='Walysson2003@', timeout=10)
    
    sftp = ssh.open_sftp()
    
    for f in files_to_upload:
        local_path = os.path.join(local_dir, f)
        remote_path = f"{remote_dir}/{f}"
        if os.path.exists(local_path):
            print(f"Uploading {f}...")
            sftp.put(local_path, remote_path)
            
    sftp.close()
    ssh.close()
    print("Upload completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
