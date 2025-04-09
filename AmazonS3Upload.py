import boto3
import os


AWS_A = "####################"
AWS_S = "######################"
AWS_BUCKET_NAME = "workflow-with-python-awss3-rds-glue"
AWS_REGION = "eu-north-1"
LOCAL_FOLDER = r"C:\Learn\Project\UnzipRawFile"
S3_PREFIX = "Source_RawFile"


s3_client = boto3.client(
    service_name='s3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_A,
    aws_secret_access_key=AWS_S
)


for root, _, files in os.walk(LOCAL_FOLDER):
    for filename in files:
        local_path = os.path.join(root, filename)
        relative_path = os.path.relpath(local_path, LOCAL_FOLDER)
        s3_key = f"{S3_PREFIX}/{relative_path}".replace("\\", "/")
        s3_client.upload_file(local_path, AWS_BUCKET_NAME, s3_key)
        print(f"Uploaded: {local_path} to s3://{AWS_BUCKET_NAME}/{s3_key}")
