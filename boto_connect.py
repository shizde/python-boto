import boto3

class S3(object):
    """
     A class used to represent an Animal

    ...

    Attributes
    ----------
    bucket_name : str
        a formatted string to print out what the animal says
    region_name : str
        the name of the animal

    Methods
    -------
    get(key: str)
        Prints the animals name and what sound it makes
    
    put(key: str, value: str)
        Prints the animals name and what sound it makes
    
    pop(key: str) -> str
        Prints the animals name and what sound it makes
    
    __getitem__(key: str) -> str
        Prints the animals name and what sound it makes
    
    __setitem__(key: str, value: str)
        Prints the animals name and what sound it makes
    
    __delitem__(key: str) -> None
        Prints the animals name and what sound it makes
    
    __contains__(key: str) -> bool
        Prints the animals name and what sound it makes
    
    keys(prefix: str ='') -> str
        Prints the animals name and what sound it makes
    
    items(prefix: str='') -> tuple
        Prints the animals name and what sound it makes
    
    """
    def __init__(self, **kwargs):
        self.bucket_name = kwargs.get('bucket_name', 'test-for-boto')
        self.region      = kwargs.get('region_name', 'eu-west-1')
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

    def __contains__(self, key: str) -> bool:
        check = False
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if key == item['Key']:
                check = True    
        
        return check

    def keys(self, prefix: str ='') -> str:
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if prefix:
                if prefix in item['Key']:
                    yield item['Key']
            else:
                yield item['Key']

    # TODO : Multi-thread
    def items(self, prefix: str='') -> tuple:
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            for k in item:
                if k == 'Key':
                    yield (k, item[k])

if __name__ == '__main__':
    test_dict = {'bucket_name':'test-for-boto','region_name':'eu-west-1'}
    test = S3(**test_dict)