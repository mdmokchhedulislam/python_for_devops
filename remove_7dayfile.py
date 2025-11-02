

from datetime import datetime, timedelta
import os
import shutil


DAYS_OLD = 7

source_folder = "backup_logs"
backupfolder = "backup"


# time = datetime.datetime.now().strftime("%y_%m_%d")
cot_of_time =datetime.now() - timedelta(days=DAYS_OLD)

print(cot_of_time)


for filename in os.listdir(source_folder):
    print(filename)
    filepath = os.path.join(source_folder, filename)
    print(filepath)
    
    if os.path.isfile(filepath) & filename.endswith(".log"):
        print("this is logfile")
        
        mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
        
        print(mtime)
        if mtime < cot_of_time:
            try:
                shutil.move(filepath, os.path.join(backupfolder, filename))
                

            except Exception as e:
                print(e)
        else:
            print("not old")