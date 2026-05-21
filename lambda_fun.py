import json
import boto3
import pandas as pd
import io

s3 = boto3.client('s3')

DEST_BUCKET = 'csv-processed-data-yuvan'

def lambda_handler(event, context):

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=source_bucket, Key=source_key)

    csv_content = response['Body'].read()

    df = pd.read_csv(io.BytesIO(csv_content))

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove null rows
    df = df.dropna()

    # Convert column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    output_buffer = io.StringIO()

    df.to_csv(output_buffer, index=False)

    processed_key = f"cleaned-{source_key}"

    s3.put_object(
        Bucket=DEST_BUCKET,
        Key=processed_key,
        Body=output_buffer.getvalue()
    )

    return {
        'statusCode': 200,
        'body': json.dumps('CSV processed successfully')
    }
