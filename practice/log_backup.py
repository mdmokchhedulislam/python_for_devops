import shutil
import os
import datetime

logfile = "server.log"
backup_folder = "backup_logs"

try:
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
        print(f'{backup_folder} folder created successfully')

    time_stamps = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    shutil.copy(logfile, f"{backup_folder}/server_{time_stamps}.log")
    print("Log backup created successfully!")

except FileNotFoundError:
    print(f"Error: The log file '{logfile}' was not found. Please check the file path.")

except PermissionError:
    print("Error: Permission denied! You don’t have access to read or write the file.")

except shutil.SameFileError:
    print("Source and destination are the same file!")

except Exception as e:
    print(f"Unexpected error occurred: {e}")

else:
    print("Backup process completed without errors.")
