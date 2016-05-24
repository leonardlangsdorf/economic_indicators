#MoviesQuery01.py
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

#dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")

table = dynamodb.Table('BLS')

print("Group Total")

response = table.query(
    KeyConditionExpression=Key('OCC_CODE').eq("00-0000")
)

for i in response['Items']:
    print(i['OCC_CODE'], ":", i['OCC_GROUP'])

