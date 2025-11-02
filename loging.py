import shutil
import os
import datetime
import logging

logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logfile = "server.log"
backup_folder = "backup_logs"

try:
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
        logging.info(f"{backup_folder} folder created successfully")

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    shutil.copy(logfile, f"{backup_folder}/server_{timestamp}.log")
    logging.info("Backup created successfully!")

except FileNotFoundError:
    logging.error("Log file not found!")
except PermissionError:
    logging.error("Permission denied!")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
finally:
    logging.info("Backup operation completed")
