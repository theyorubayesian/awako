import base64
import json
import os

import boto3

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    """
    Receive base64 encoded data, decode and 
    make inferences
    """
    image = base64.b64decode(event["body"]["image_data"])
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='image/png',
        Body=image
    )
    event["body"]["inferences"] = eval(response["Body"].read().decode("utf-8"))
    
    return {
        'statusCode': 200,
        'body': event["body"]
    }
