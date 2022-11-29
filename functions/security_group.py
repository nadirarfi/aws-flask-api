import boto3
from botocore.exceptions import ClientError


# Get all security groups
def get_all_security_groups():
    """
    Get all security groups
    """
    try:
        ec2 = boto3.client("ec2")
        all_security_groups = ec2.describe_security_groups()['SecurityGroups']
        n_security_groups = len(all_security_groups)
        return all_security_groups
    except ClientError as e:
        return str(e)
    

# Get security groups by ids
def get_security_groups_by_ids(group_ids:list):
    """
    Get security groups by IDs
    GroupIds = ["sg-04fc6229c4d89146a"]   
    """
    try:
        ec2 = boto3.client("ec2")
        selected_security_groups = ec2.describe_security_groups(GroupIds=group_ids)['SecurityGroups']
        return selected_security_groups
    except ClientError as e:
        return str(e)
        
