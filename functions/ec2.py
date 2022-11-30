import boto3
from botocore.exceptions import ClientError
from functions.helper import handle_datetime_values



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
        

def get_instance_types(regions=None):
    """
    Get available instance types with regions
    """
    ec2_client = boto3.client('ec2')
    try:
        if regions is None:
            response = ec2_client.describe_instance_type_offerings()
        else: 
            response = ec2_client.describe_instance_type_offerings(
            LocationType = "region",
            Filters = [
                    {
                    'Name': 'location',
                    'Values': regions
                    }
                ]   
            )
        return response['InstanceTypeOfferings']
    except ClientError as e:
        print(e)
        return False





def get_instances(keypair=None):
    """
    """
    ec2 = boto3.client('ec2')

    try:
        if keypair is None:
            reservations = ec2.describe_instances()["Reservations"]            
        else:
            Filters=[{"Name": "key-name", "Values": [keypair]}]
            reservations = ec2.describe_instances(Filters=Filters)["Reservations"]
        instances = []
        for reservation in reservations:
            for instance in reservation["Instances"]:
                to_keep = [
                    'ImageId', 'InstanceId', 'InstanceType', 'KeyName', 'LaunchTime', 'Monitoring', 'Placement', 
                    'PrivateDnsName', 'PrivateIpAddress', 'ProductCodes', 'PublicDnsName', 'State', 
                    'SubnetId', 'VpcId', 'Architecture', 'ClientToken', 'Hypervisor', 'RootDeviceName', 
                    'RootDeviceType', 'SecurityGroups', 'VirtualizationType', 'CpuOptions', 
                    'CapacityReservationSpecification', 'HibernationOptions','PlatformDetails'
                    ]
                instance = {k:v for k,v in instance.items()  if k in to_keep}
                instance = handle_datetime_values(instance)
                instances.append(instance)
        return instances
    except ClientError as e:
        print(e)
        return False