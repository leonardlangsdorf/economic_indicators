#MoviesDeleteTable.py
from __future__ import print_function # Python 2/3 compatibility
import boto3

#dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")

table = dynamodb.Table('BLS')

table.delete()