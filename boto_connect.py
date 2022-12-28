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
            response = client.put_object(
                Bucket=self.bucket_name,
                Key=key
            )
            return "OK"
        except Exception as e:
            return e

    def pop(self, key: str) -> str:
        try:
            get(key)
            response = client.delete_object(
                Bucket=self.bucket_name,
                Key=key
            )
        except Exception as e:
            return e

    def __getitem__(self, key: str) -> str:
        get(key)

    def __setitem__(self, key: str, value: str):
        put(key)

    def __delitem__(key: str):
        pop(key)

    def __contains__(key: str) -> bool:
        pass

    def keys(prefix: str ='') -> str:
        pass

    def items(prefix: str='') -> tuple:
        pass

if __name__ == '__main__':
    test_dict = {'bucket_name':'test-FOR-boto','region_name':'EU-west-1'}
    test = S3(**test_dict)