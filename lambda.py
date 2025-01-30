
import boto3
from datetime import datetime

# יצירת לקוח עבור DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')  

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            # חילוץ גוף ההודעה מ-SQS
            message_body = json.loads(record['body'])  

            # חילוץ פרטי הקובץ מהאירוע של S3 בתוך ההודעה
            s3_event = message_body['Records'][0]  # SQS מכיל את ה-Event של S3 בפנים
            file_name = s3_event['s3']['object']['key']
            bucket_name = s3_event['s3']['bucket']['name']

            # יצירת טיימסטמפ
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # הוספת סטטוס "Processing"
            status = 'Processing'

            # עדכון הרשומה ב-DynamoDB
            table.put_item(
                Item={
                    'FileName': file_name,
                    'BucketName': bucket_name,
                    'Timestamp': timestamp,
                    'Status': status
                }
            )

            print(f"✅ Successfully inserted {file_name} from {bucket_name} into DynamoDB at {timestamp}")

        except Exception as e:
            print(f"❌ Error processing record: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed')
    }
