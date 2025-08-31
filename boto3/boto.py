import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mokchhedulislamdemobucketwithboto3',
 
)

response = client.delete_bucket(
    Bucket='mokchhedulislamdemobucket',
)

print(response)