
import json
import base64
import boto3
import datetime

def upload(event, context):
    """
    curl -X POST -H "Content-Type: application/pdf" --data-binary (base64 ../../Downloads/123.pdf) https://shglld5li7.execute-api.us-east-1.amazonaws.com/dev/upload
    """
    BUCKET_NAME = 'upload-file-s3-dev-serverlessdeploymentbucket-mluyxljlbxvv'
    body = event.get("body", None)
    if body is None:
        return {"statusCode": 400, "body": "Missing the file"}

    try:
        file_content = base64.b64decode(body)
    except Exception as e:
        return {"statusCode": 400, "body": str(e)}

    file_path = f'pdf/  test-{datetime.datetime.now()}.pdf'
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        return {"statusCode": 400, "body": str(e)}

    return {
        'statusCode': 200,
        "body": file_path
    } 