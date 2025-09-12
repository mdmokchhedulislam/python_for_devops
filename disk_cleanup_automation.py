import os
import time

LOG_DIR =  "/var/logs/myapp/"


def disk_clean_up_automation():
    for file in os.listdir(LOG_DIR):
        filepath = os.path.join(LOG_DIR, file)
        if os.path.isfile(filepath) and time.time() - os.path.getmtime(filepath)>7*86400:
            os.remove(filepath)