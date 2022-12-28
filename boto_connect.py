import boto3
import io


class S3(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self, **kwargs):
        self.region      = kwargs.get('region_name', 'eu-west-1')
        self.bucket_name = kwargs.get('bucket_name', 'test-for-boto')
        self.conn        = boto3.client('s3', region_name=self.region)

    def get(self, key: str):
        try:
            response = self.conn.get_object(
                Bucket=self.bucket_name,
                Key=key
            )
            return response
        except Exception as e:
            return e 

    def put(self, key: str, value: str):
        try:
            response = self.conn.put_object(
                Body=value,
                Bucket=self.bucket_name,
                Key=key
            )
            return response
        except Exception as e:
            return e

    def pop(self, key: str) -> str:
        try:
            retrieve = self.get(key)
            response = self.conn.delete_object(
                Bucket=self.bucket_name,
                Key=key
            )
            return retrieve
        except Exception as e:
            return e

    def __getitem__(self, key: str) -> str:
        self.get(key)

    def __setitem__(self, key: str, value: str):
        self.put(key)

    def __delitem__(key: str):
        self.pop(key)

    def __contains__(key: str) -> bool:
        pass

    def keys(prefix: str ='') -> str:
        pass

    def items(prefix: str='') -> tuple:
        pass

if __name__ == '__main__':
    test_dict = {'bucket_name':'test-FOR-boto','region_name':'EU-west-1'}
    test = S3(**test_dict)