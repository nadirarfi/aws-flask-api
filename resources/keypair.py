from flask_restful import Resource
from functions.keypair import *
from flask import request, send_file
import json


class AllKeyPairs(Resource):
    def get(self):
        """
        Get all key pairs in AWS account
        """
        return get_all_keypairs()


class KeyPair(Resource):
    def get(self):
        """
        Get keypair metadata
        """
        query_params = request.args.to_dict()
        keyname = query_params["keyname"]
        return get_keypair(keyname= keyname)

    def post(self):
        """
        Create a keypair
        """
        data = request.get_json()
        keyname = data["keyname"]
        keypair =  create_keypair(keyname= keyname)
        if keypair:
            return keypair["KeyMaterial"]
        else:
            return False