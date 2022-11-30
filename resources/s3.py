from flask_restful import Resource
from functions.s3 import *
from flask import request


class AllBuckets(Resource):
    def get(self):
        """
        Get all buckets
        """
        all_buckets = get_all_buckets()
        return all_buckets

class Bucket(Resource):
    def post(self):
        """
        Create Bucket
        """
        data = request.get_json()
        bucket_name = data["bucket"]
        region_name = data["region"]
        return create_bucket(bucket_name=bucket_name, region_name=region_name)



class FilteredBuckets(Resource):
    def get(self):
        """
        Filter buckets by region
        """
        query_params = request.args.to_dict()
        region = query_params["region"]
        if "keywords" in query_params.keys():
            keywords = request.args.get("keywords").split(",")
            return filter_buckets(region_name=region, keywords=keywords)
        else:
            return filter_buckets(region_name=region)


class BucketPolicy(Resource):
    def put(self):
        """
        Update bucket policy

        {
            "region": "eu-north-1",
            "policy": {
                    "Id": "Policy1668494172498",
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                        "Sid": "Stmt1668494168655",
                        "Action": [
                            "s3:GetObject"
                        ],
                        "Effect": "Allow",
                        "Resource": "arn:aws:s3:::nadir-mystaticwebsite/*",
                        "Principal": "*"
                        }
                    ]
                }
            }
        """
        data = request.get_json()
        bucket_name = data["bucket"]
        bucket_policy = data["policy"]
        return update_bucket_policy(bucket_name = bucket_name, bucket_policy= bucket_policy)

    def delete(self):
        """
        Delete bucket policy
        """
        data = request.get_json()
        bucket_name = data["bucket"]
        return delete_bucket_policy(bucket_name = bucket_name)


class Versioning(Resource):
    def post(self):
        """
        Enable versioning for a specific bucket
        
        """
        data = request.get_json()
        bucket_name = data["bucket"]
        action = data["action"]        
        return versioning(bucket_name=bucket_name, action=action)


class Object(Resource):
    def post(self):
        """
        Upload one file into S3 bucket
        {
            "bucket": "nadir-mystaticwebsite",
            "file_path": "M:/dev/nadir/aws-flask-api/s3_files"
        }

        """
        data = request.get_json()
        bucket_name = data["bucket"]
        file_path = data["file_path"]
        if "object_name" in data.keys():
            object_name = data["object_name"]
            return upload_file(file_path= file_path, bucket_name=bucket_name, object_name=object_name)
        return upload_file(file_path= file_path, bucket_name=bucket_name, object_name=None)

    def delete(self):
        """
        Delete some objects

        {
            "bucket": "nadir-mystaticwebsite",
            "objects": [
                "img1.png",
                "img2.png"
            ]
        }

        """
        data = request.get_json()
        bucket_name = data["bucket"]
        objects = data["objects"]        
        return delete_objects(bucket_name= bucket_name, objects= objects)


class AllObjects(Resource):
    def post(self):
        """
        Upload files into S3 bucket
        e.g folder = ""

        {
            "bucket": "nadir-mystaticwebsite",
            "folder_path": "M:/dev/nadir/aws-flask-api/s3_files"
        }

        """
        data = request.get_json()
        bucket_name = data["bucket"]
        folder_path = data["folder_path"]
        return upload_many_files(bucket_name=bucket_name, folder_path=folder_path)
