
from flask import Flask
from flask_restful import Api
from resources.s3 import * 
from resources.keypair import * 
from resources.security_group import *
from resources.ec2 import * 

app = Flask(__name__)
api = Api(app)

# EC2
api.add_resource(EC2InstancesTypes, '/api/ec2/instances/types') # GET Available Instance Types
api.add_resource(EC2Instances, '/api/ec2/instances') # GET instances data (KEYPAIR can be given as query parameter to filter)

# Security Group
api.add_resource(AllSecurityGroups, '/api/sg/all') # GET all Security Groups
api.add_resource(SecurityGroupsByIds, '/api/sg/ids') # GET Security Groups by IDs
api.add_resource(SecurityGroup, '/api/sg/create') # Create a Security Group
api.add_resource(SecurityGroupRule, '/api/sg/rule') # Update/Delete security group rule

# Key Pairs
api.add_resource(AllKeyPairs, '/api/keypair/all') # GET all keypairs
api.add_resource(KeyPair, '/api/keypair') # Create key pair

# S3
api.add_resource(Bucket, '/api/s3/bucket/create') # Create bucket
api.add_resource(AllBuckets, '/api/s3/bucket/all') # List all buckets
api.add_resource(FilteredBuckets, '/api/s3/bucket/filter') # Filter buckets with regions and keywords(optional)
api.add_resource(BucketPolicy, '/api/s3/bucket/policy') # Update/Delete bucket policy
api.add_resource(Versioning, '/api/s3/bucket/versioning') # Enable/disable versioning 
api.add_resource(Object, '/api/s3/bucket/object') # Upload/Delete objects
api.add_resource(AllObjects, '/api/s3/bucket/object/all') # Get all objects


@app.route('/')
def index():
    pass

app.run(host="0.0.0.0", port=5000, debug=True)
