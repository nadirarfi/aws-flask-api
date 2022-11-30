import boto3
from botocore.exceptions import ClientError


def get_all_keypairs():
    """
    Retrieve all available key pairs
    """
    try:
        ec2 = boto3.client("ec2")
        key_pairs = ec2.describe_key_pairs()['KeyPairs']
        key_names = [ key_pair['KeyName'] for key_pair in key_pairs]
        return key_names
    except ClientError as e:
        print(e)
        return False

def get_keypair(keyname:str):
    try:
        ec2 = boto3.client("ec2")        
        keypair = ec2.describe_key_pairs(KeyNames=[keyname])['KeyPairs'][0]
        date_time = keypair['CreateTime']
        keypair.update(CreateTime = date_time.strftime("%m/%d/%Y, %H:%M:%S")) 
        return keypair
    except ClientError as e:
        print(e)
        return False

def create_keypair(keyname: str):
    """
    Create keypair and save it in a pem file
    """
    try:
        ec2 = boto3.client("ec2")
        new_keypair = ec2.create_key_pair(KeyName=keyname)
        return new_keypair
    except ClientError as e:
        print(e)
        return False

