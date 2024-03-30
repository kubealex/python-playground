import boto3
from environs import Env

env = Env()
env.read_env()
s3_endpoint = env("AWS_S3_ENDPOINT")
s3_access_key = env("AWS_S3_ACCESS_KEY")
s3_secret_token = env("AWS_S3_SECRET_TOKEN")

session = boto3.session.Session()
s3_client = session.client(
    endpoint_url=s3_endpoint,
    service_name="s3",
    aws_access_key_id=s3_access_key,
    aws_secrßßet_access_key=s3_secret_token,
    use_ssl=True,
    verify=False,
)
print(s3_client.list_buckets())
