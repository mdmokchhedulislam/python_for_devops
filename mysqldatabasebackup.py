import subprocess
from datetime import datetime

db_user = "admin"
db_password = "password123"
db_name = "projectdb"

backup_file = f"/tmp/{db_name}_{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}.sql"

backup_cmd = ["mysqldump", "-u", db_user, f"-p{db_password}", db_name]

with open(backup_file, "w") as f:
    subprocess.run(backup_cmd, stdout=f, check=True)

print("Database backup successful!")



# 3. Upload to S3

s3_bucket = "myproject-backups"
s3_key = backup_file.split("/")[-1] 

aws_access_key = "YOUR_AWS_ACCESS_KEY"
aws_secret_key = "YOUR_AWS_SECRET_KEY"
region_name = "us-east-1"

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region_name
)

try:
    s3.upload_file(backup_file, s3_bucket, s3_key)
    print(f"Backup uploaded to S3: s3://{s3_bucket}/{s3_key}")
except Exception as e:
    print(" Upload failed:", e)