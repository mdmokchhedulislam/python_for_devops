import os
import time

LOG_DIR = "/var/log/myapp"
DAYS = 7 

def cleanup_logs():
    current_time = time.time()
    for filename in os.listdir(LOG_DIR):
        if filename.endswith(".log"):
            file_path = os.path.join(LOG_DIR, filename)
            file_age = os.stat(file_path).st_mtime
            
            if current_time - file_age > (DAYS * 86400):
                print(f"Deleting old log: {filename}")
                os.remove(file_path)

if __name__ == "__main__":
    cleanup_logs()