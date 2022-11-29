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
        return 
    except ClientError as e:
        return str(e)


def get_all_buckets():
    """
    Get all buckets
    """
    try:
        s3_resource = boto3.resource('s3') 
        all_buckets = [bucket.name for bucket in s3_resource.buckets.all()] # List all buckets
        return all_buckets
    except ClientError as e:
        return str(e)


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
        return str(e)
        

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
            return "Successful request. Bucket Policy has been updated."
    except ClientError as e:
        return str(e)


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
            return "Successful request. Bucket Policy has been deleted."
    except ClientError as e:
        return str(e)
        
    
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
        return f"Versioning status: {versioning.status}" 
    except ClientError as e:
        return str(e)    