import boto3
import io

class S3(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    bucket_name = "test-for-boto"

    def __init__(self, *args, **kwargs):
        region = self.kwargs.get('region_name', 'us-east-1')
        self.bucket_name = self.kwargs.get('bucket_name', self.bucket_name)
        self.conn = client('s3', region_name=region)


    def get(self, key: str):
        response = client.get_object(
            Bucket=self.bucket_name,
            Key=key
            )
         

    def put(self, key: str, value: BytesIO):
        response = client.put_object(
            Bucket=self.bucket_name,
            Key=key
        ) 

    def pop(self, key: str) -> BytesIO:
        response = client.delete_object(
            Bucket=self.bucket_name,
            Key=key
        )

    def __getitem__(self, key: str) -> BytesIO:
        pass

    def __setitem__(self, key: str, value: BytesIO):
        pass

    def __delitem__(key: str):
        pass

    def __contains__(key: str) -> bool:
        pass

    def keys(prefix: str ='') -> str:
        pass

    def items(prefix: str='') -> tuple:
        pass

