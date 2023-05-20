import json
import os
import boto3

client = boto3.client('dynamodb')
#table_name = os.environ["table_name"]
table_name = "trend_dyn"

def lambda_handler():
    # TODO implement
    response = client.put_item(
        TableName=table_name,
        Item={"id" : {"S": "2222"}, "batch_num": {"N": "3232"}, "hero_name": {"S":"Batman"}})
    return response

print(lambda_handler())
