import json
import os

THRESHOLD = float(os.getenv("THRESHOLD"))


def lambda_handler(event, context):
    
    inferences = event["body"]["inferences"]
    meets_threshold = any([float(x) >= THRESHOLD for x in inferences])
    
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")
        
    return {
        'statusCode': 200,
        'body': event["body"]
    }
