from flask_restful import Resource
from functions.ec2 import *
from flask import request


class EC2Instances(Resource):

    def get(self):
        """
        Get all instances with the option to filter with a keypair parameter        
        http://X.X.X.X/api/ec2/instances?keypair=NADIR_KEY_PAIR
        """
        query_params = request.args.to_dict()
        if "keypair" in query_params.keys():
            keypair = query_params["keypair"]
            return get_instances(keypair=keypair)
        else:
            return get_instances()



class EC2InstancesTypes(Resource):
    def get(self):
        """
        Get instance types

        """
        query_params = request.args.to_dict()
        if "regions" in query_params.keys():
            regions = query_params["regions"]
            return get_instance_types(regions=regions)
        else:
            return get_instance_types()


