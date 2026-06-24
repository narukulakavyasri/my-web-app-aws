-
import os
import boto3
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Replace with your S3 bucket name
BUCKET_NAME = "cloud-server-monitor-logs-kavya"

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# Upload file
try:
    s3.upload_file(
        "logs/server.log",  # Local file path
        BUCKET_NAME,        # S3 bucket name
        "server.log"        # File name in S3
    )
    print("Upload successful!")
except Exception as e:
    print("Error:", e)