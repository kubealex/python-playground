import boto3
import os
s3_endpoint = os.getenv("AWS_S3_ENDPOINT")
s3_access_key = os.getenv("AWS_S3_ACCESS_KEY")
s3_secret_token = os.getenv("AWS_S3_SECRET_TOKEN")

session = boto3.session.Session()
s3_client = session.client(endpoint_url=s3_endpoint, service_name='s3', aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_token, use_ssl=True, verify=False)
print(s3_client.list_buckets())
