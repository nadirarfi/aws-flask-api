from flask_restful import Resource
from functions.security_group import *
from flask import request

class AllSecurityGroups(Resource):
    def get(self):
        return get_all_security_groups()   


class SecurityGroupsByIds(Resource):
    def get(self):
        group_ids = request.args.get("group_ids").split(",")
        return get_security_groups_by_ids(group_ids=group_ids)


class SecurityGroup(Resource):
    def post(self):
        """
        Create a security group
        """
        data = request.get_json()
        if data:           
            return create_security_group(**data)

class SecurityGroupRule(Resource):
    def post(self):
        """
        Create security group rule
        """
        data = request.get_json()
        return True


    def put(self):
        """
        Modify security group Rule
        """
        data = request.get_json()
        return True