import boto3

s3_client = boto3.client('s3')

type(s3_client)

buckets = s3_client.list_buckets()['Buckets']

'ask-dg.com'

bucket_name = [bucket['Name'] for bucket in buckets]

bucket_name