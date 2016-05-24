#MoviesLoadData.py
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")

table = dynamodb.Table('BLS')

with open("national.json") as json_file:
    jobs = json.load(json_file, parse_float = decimal.Decimal)
    for job in jobs:
        OCC_CODE = job['OCC_CODE']
        OCC_GROUP = job['OCC_GROUP']
        TOT_EMP = job['TOT_EMP']

        print("Adding BLS:", OCC_CODE, TOT_EMP)

        table.put_item(
           Item={
               'OCC_CODE': OCC_CODE,
               'OCC_GROUP': OCC_GROUP,
               'TOT_EMP': TOT_EMP,
            }
        )