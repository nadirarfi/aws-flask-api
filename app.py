
from flask import Flask
from flask_restful import Api
from resources.s3 import * 
from resources.security_group import *
from resources.ec2 import * 

app = Flask(__name__)
api = Api(app)

# EC2
#api.add_resource(EC2, '/api/ec2/')

# Security Group
api.add_resource(AllSecurityGroups, '/api/sg/all')
api.add_resource(SecurityGroupsByIds, '/api/sg/ids')
api.add_resource(SecurityGroup, '/api/sg/create')



# S3
api.add_resource(Bucket, '/api/s3/bucket/create')
api.add_resource(AllBuckets, '/api/s3/bucket/all')
api.add_resource(FilteredBuckets, '/api/s3/bucket/filter')
api.add_resource(BucketPolicy, '/api/s3/bucket/policy')
api.add_resource(Versioning, '/api/s3/bucket/versioning')




@app.route('/')
def index():
    pass

app.run(host="0.0.0.0", port=5000, debug=True)
