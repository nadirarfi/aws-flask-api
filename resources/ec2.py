from flask_restful import Resource
from functions.ec2 import *




class EC2(Resource):

    def get(self):
        return {'ec2': 'world'}

    def post(self):
        pass

