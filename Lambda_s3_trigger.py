import json
import os
import boto3
from urllib.parse import unquote_plus
import glob


def lambda_handler(event, context):
    # TODO implement
    #print(event['multiValueQueryStringParameters'])
    
    # Get bucket name and file name from s3
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = unquote_plus(event["Records"][0]["s3"]["object"]["key"])
    
    
    # using s3 client
    s3 = boto3.client('s3')
    # Download file from s3 to lambda temp storage
    s3.download_file(bucket_name, s3_file_name, os.path.join("/tmp",s3_file_name))
    files = glob.glob("/tmp"+"/*.json")
    with open(files[0], 'r') as f:
        data = json.load(f)
    print(data)
    
    return {
        'statusCode': 200
    }
