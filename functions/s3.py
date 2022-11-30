import os
import boto3
import json
from botocore.exceptions import ClientError

def create_bucket(bucket_name:str, region_name:str):
    """
    Create a bucket
    """    
    try:
        s3_resource = boto3.resource('s3') 
        response = s3_resource.create_bucket(
            Bucket= bucket_name, 
            CreateBucketConfiguration= {
                "LocationConstraint": region_name
            }
        ) 
        code = response['ResponseMetadata']['HTTPStatusCode']
        return True
    except ClientError as e:
        print(e)
        return False

def get_all_buckets():
    """
    Get all buckets
    """
    try:
        s3_resource = boto3.resource('s3') 
        all_buckets = [bucket.name for bucket in s3_resource.buckets.all()] # List all buckets
        return all_buckets
    except ClientError as e:
        print(e)
        return False


def filter_buckets(region_name:str, keywords=""):
    """
    Filter buckets based on a specific region as well as additional keywords
    """
    try:
        s3_client = boto3.client('s3')
        all_buckets = get_all_buckets()
        filtered_buckets = []
        for bucket_name in all_buckets:
            response = s3_client.get_bucket_location(Bucket= bucket_name)
            bucket_region = response['LocationConstraint']
            if bucket_region == region_name:
                if keywords:
                    for key in keywords:
                        if key in bucket_name:
                            filtered_buckets.append(bucket_name)
                else:
                    filtered_buckets.append(bucket_name)
        return filtered_buckets
    except ClientError as e:
        print(e)
        return False


def update_bucket_policy(bucket_name: str, bucket_policy:dict):
    """
    Update Bucket Policy
    """
    try:
        s3_resource = boto3.resource('s3') 
        bucketpolicy = s3_resource.BucketPolicy(bucket_name)
        response = bucketpolicy.put(Policy=json.dumps(bucket_policy))
        code = response['ResponseMetadata']['HTTPStatusCode']
        if code == 204:
            print("Successful request. Bucket Policy has been updated.")
            return True
    except ClientError as e:
        print(e)
        return False


def delete_bucket_policy(bucket_name: str):
    """
    Delete Bucket Policy
    """
    try:
        s3_resource = boto3.resource('s3') 
        bucketpolicy = s3_resource.BucketPolicy(bucket_name)
        response = bucketpolicy.delete()
        code = response['ResponseMetadata']['HTTPStatusCode']
        if code == 204:
            print("Successful request. Bucket Policy has been deleted.")
            return True
    except ClientError as e:
        print(e)
        return False

    
def versioning(bucket_name:str, action:str):
    """
    Enable versioning

    """
    try:
        s3_resource = boto3.resource('s3')         
        versioning = s3_resource.BucketVersioning(bucket_name)
        if action == "enable":
            versioning.enable() 
        if action == "disable":
            versioning.suspend()
        print(f"Versioning status: {versioning.status}")
        return True
    except ClientError as e:
        print(e)
        return False


def upload_file(file_path:str, bucket_name:str, object_name=None):
    """Upload a file to an S3 bucket
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket(bucket_name) # Get bucket 
        response = bucket.upload_file(Filename= file_path, Key=object_name) # Upload object to S3
        print("File has been successfully uploaded!")
        return True
    except ClientError as e:
        print(e)
        return False


def upload_many_files(bucket_name:str, folder_path:str):
    """
    """
    for path, subdirs, all_files in os.walk(folder_path): # Scan all files within subdirectories etc...
        for file in all_files:
            file_path = os.path.join(path, file) # File path     
            upload_file(file_path= file_path, bucket_name= bucket_name)
    return True


def delete_objects(bucket_name:str, objects:list):
    """Delete a file from S3 bucket
    """
    try:
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket(bucket_name) # Get bucket 
        response = bucket.delete_objects(Delete = {'Objects': [ {'Key': obj} for obj in objects ]})
        print("Objects have been deleted.")
        return True
    except ClientError as e:
        print(e)
        return False