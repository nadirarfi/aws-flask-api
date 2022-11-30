import boto3
from botocore.exceptions import ClientError



def get_endpoints():
    """
    Retrieve all available endpoints
    """
    try:
        ec2 = boto3.client("ec2")
        Response = ec2.describe_regions()
        Regions = Response['Regions']
        endpoints = [ region['Endpoint'] for region in Regions]
        return endpoints
    except ClientError as e:
        print(e)
        
