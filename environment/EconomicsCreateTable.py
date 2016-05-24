from __future__ import print_function # Python 2/3 compatibility
import boto3

#dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")

table = dynamodb.create_table(
    TableName='BLS',
    KeySchema=[
        {
            'AttributeName': 'OCC_CODE',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'OCC_GROUP',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'OCC_CODE',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'OCC_GROUP',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)