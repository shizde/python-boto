import boto3

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
        return self.get(key)

    def __setitem__(self, key: str, value: str):
        return self.put(key, value)

    def __delitem__(self, key: str) -> None:
        self.pop(key)
        return None

    def list_bucket_objects(self, key: str='') -> list:
        bucket_objects = []
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if key:
                if key in item:
                    bucket_objects.append(item['Key'])
            else:
                bucket_objects.append(item['Key'])
        return bucket_objects

    def __contains__(self, key: str) -> bool:
        if key in self.list_bucket_objects():
            return True
        else: 
            return False

    def keys(self, prefix: str ='') -> str:
        if prefix:
            list_bucket_objects(prefix)
        else:
            list_bucket_objects()

    def items(prefix: str='') -> tuple:
        pass

if __name__ == '__main__':
    test_dict = {'bucket_name':'test-for-boto','region_name':'eu-west-1'}
    test = S3(**test_dict)