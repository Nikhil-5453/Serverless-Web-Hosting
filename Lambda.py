import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourDynamoDBTableName')  # Replace your DB name, make sure items given properly

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        response = table.put_item(Item=data)
        return {
            'statusCode': 200,
            'body': json.dumps('Data stored successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error storing data: {str(e)}')
        }