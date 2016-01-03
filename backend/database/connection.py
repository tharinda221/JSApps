# import libraries
from __future__ import print_function
import boto3

# import classes
import config


def getConnection():
    return boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id="anything",
                          aws_secret_access_key="anything", endpoint_url="http://localhost:8000")
