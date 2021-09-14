import base64
import json

import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    """
    This function serializes target data from S3
    """
    
    # Get s3 address from Step Function event input
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    
    with open("/tmp/image.png", "wb") as f:
        s3.download_fileobj(bucket, key, f)
    
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
    
    print("Event: ", event.keys())
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
