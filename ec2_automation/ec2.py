import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2", region_name="us-east-1")

INSTANCE_ID = "i-0abcd1234efgh5678"  # from aws or terraform output


def start_instance():
    try:
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        print(f"EC2 {INSTANCE_ID} started")
    except ClientError as e:
        if "InvalidInstanceID.NotFound" in str(e):
            print(f"EC2 not found with ID {INSTANCE_ID}")
        else:
            print(f"Error: {e}")


def stop_instance():
    try:
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        print(f"EC2 {INSTANCE_ID} stopped")
    except ClientError as e:
        if "InvalidInstanceID.NotFound" in str(e):
            print(f"EC2 not found with ID {INSTANCE_ID}")
        else:
            print(f"Error: {e}")


if __name__ == "__main__":
    choice = input("Start (s) or Stop (x) EC2? : ").lower()
    if choice == "s":
        start_instance()
    elif choice == "x":
        stop_instance()
    else:
        print("Invalid choice")
