import boto3
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        bucket_name ='<BUCKET_NAME>'
        topic_arn = '<SNS_TOPIC_ARN>'
        
        response = s3.list_objects_v2(Bucket=bucket_name)
        object_count = response.get('KeyCount', 0)

        if object_count == 0:
            message = f"S3 Bucket '{bucket_name}' is empty."
            sns.publish(
                TopicArn=topic_arn,
                Subject='[ALERT] Empty S3 Bucket',
                Message=message
            )

        return {
            'statusCode': 200,
            'body': f"Checked {bucket_name}: {object_count} object(s) found."
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise e
