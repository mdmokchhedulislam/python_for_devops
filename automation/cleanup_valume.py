import boto3
from botocore.exceptions import ClientError

def cleanup_volumes():
 
    ec2 = boto3.resource('ec2', region_name='us-east-1')  

    print(f"Scanning for unused EBS volumes in region us-east-1...\n")


    filters = [{'Name': 'status', 'Values': ['available']}]

    try:
        volumes = ec2.volumes.filter(Filters=filters)  
        found = False

        for volume in volumes:
            found = True
            print(f"[INFO] Found unused volume: {volume.id} | Size: {volume.size}GB | AZ: {volume.availability_zone}")

        if not found:
            print("No unused volumes found matching criteria")

    except ClientError as e:
        print(f"[ERROR] Could not list volumes: {e}")

if __name__ == "__main__":
    cleanup_volumes()
