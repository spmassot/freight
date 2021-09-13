import boto3
import config

from io import BytesIO


class S3Client:
    client = boto3.client('s3')

    @classmethod
    def all_buckets(cls):
        return [b['Name'] for b in cls.client.list_buckets()['Buckets']]

    @classmethod
    def initialize_bucket(cls, bucket_to_initialize):
        if bucket_to_initialize not in cls.all_buckets():
            cls.client.create_bucket(
                ACL='private',
                CreateBucketConfiguration={
                    'LocationConstraint': 'us-east-1'
                }
            )

    @classmethod
    def create_folder(cls, folder_name):
        cls.client.put_object(
            Bucket=config.BUCKET,
            Body='',
            Key=folder_name+'/'
        )

    @classmethod
    def put_file_in_folder(cls, file_name, file_data, folder_name):
        cls.client.put_object(
            Bucket=config.BUCKET,
            Body=file_data,
            Key=folder_name+'/'+file_name
        )

    @classmethod
    def list_objects(cls):
        response = cls.client.list_objects(Bucket=config.BUCKET).get('Contents')
        if response:
            return [x['Key']  for x in response]
        else:
            return []
