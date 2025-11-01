import boto3

s3 = boto3.client("s3")

def upload_file():
    s3.upload_file("data.txt", "my-backup-bucket", "data.txt")
    print("✅ File uploaded to S3!")

upload_file()
