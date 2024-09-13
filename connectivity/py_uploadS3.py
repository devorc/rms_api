import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)


def file_move(path, upload_filename):
    s3, s3_res = get_s3()
    try:
        s3.upload_file(path, get_bucket(), upload_filename, ExtraArgs={'ACL': 'public-read'})
        os.remove(path)
    except Exception as e:
        print(e)


def get_s3():
    try:
        s3 = boto3.client('s3', region_name=os.getenv("AWS_REGION_NAME"), aws_access_key_id=os.getenv("AWS_ACCESS_ID"),
                          aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
        s3_res = boto3.resource('s3', region_name=os.getenv("AWS_REGION_NAME"), aws_access_key_id=os.getenv("AWS_ACCESS_ID"),
                                aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
        return s3, s3_res
    except Exception as e:
        print(e)


def get_bucket():
    return os.getenv("AWS_S3_BUCKET")


def delete_file(file_path):
    s3, s3_res = get_s3()
    my_bucket = get_bucket()
    my_object = s3.delete_object(Bucket=my_bucket, Key=file_path)
    return my_object
