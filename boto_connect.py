import boto3

class S3(object):
    """
     A class used to connect to a S3 Bucket and manage this interaction.

    ...

    Attributes
    ----------
    dict: 
        bucket_name : str
            The bucket name inside S3
        region_name : str
            The AWS region where the bucket is located

    Methods
    -------
    get(key: str)
        Retrieve an object from the S3 bucket using a given key
    
    put(key: str, value: str)
        Put a new object in the S3 bucket. Can also modift the content of and existing object
    
    pop(key: str) -> str
        Removes the object from the S3 bucket and returns it
    
    __getitem__(key: str) -> str
        Nicer interface for get()
    
    __setitem__(key: str, value: str)
        Nicer interface for put()
    
    __delitem__(key: str) -> None
        Nicer interface for pop(). Does not return anything
    
    __contains__(key: str) -> bool
        Checks if a given object exists inside the S3 bucket
    
    keys(prefix: str ='') -> str
        Generator that yields the keys from the S3 bucket. Option to filter with a prefix
    
    items(prefix: str='') -> tuple
        Generator that yields tuples with key-value pairs.
    
    """
    def __init__(self, **kwargs):
        """
        Parameters
        ----------
        bucket_name : str
            The bucket name inside S3
        region : str
            The AWS region where the bucket is located
        """
        self.bucket_name = kwargs.get('bucket_name', 'test-for-boto')
        self.region      = kwargs.get('region_name', 'eu-west-1')
        self.conn        = boto3.client('s3', region_name=self.region)

    def get(self, key: str):
        """
        Parameters
        ----------
        key : str
            S3 key from the object that must be retrieved
        """
        try:
            response = self.conn.get_object(
                Bucket=self.bucket_name,
                Key=key
            )
            return response
        except Exception as e:
            return e 

    def put(self, key: str, value: str):
        """
        Parameters
        ----------
        key : str
            S3 key from the object that must be sent
        value : str
            Content of the object being sent
        """
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
        """
        Parameters
        ----------
        key : str
            S3 key from the object that must be deleted
        """
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
        """ Nicer interface for get() """
        return self.get(key)

    def __setitem__(self, key: str, value: str):
        """ Nicer interface for put() """
        return self.put(key, value)

    def __delitem__(self, key: str) -> None:
        """ Nicer interface for pop(). Does not return anything """
        self.pop(key)
        return None

    def __contains__(self, key: str) -> bool:
        """
        Parameters
        ----------
        key : str
            S3 key from the object that will be checked if exists inside the S3 bucket
        """
        check = False
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if key == item['Key']:
                check = True    
        
        return check

    def keys(self, prefix: str ='') -> str:
        """
        Parameters
        ----------
        prefix : str
            Part of the key for the object that will be retrieved. Optional.
        """
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if prefix:
                if prefix in item['Key']:
                    yield item['Key']
            else:
                yield item['Key']

    # TODO : Multi-thread
    def items(self, prefix: str='') -> tuple:
        """
        Parameters
        ----------
        prefix : str
            Part of the key for the object that will be retrieved. Optional.
        """
        for item in self.conn.list_objects(Bucket=self.bucket_name)['Contents']:
            if prefix:
                if prefix in item['Key']:
                    for k in item:
                        if k == 'Key':
                            yield (k, item[k])
            else:
                for k in item:
                        if k == 'Key':
                            yield (k, item[k])



if __name__ == '__main__':
    # TEST PROCEDURE
    ## Setting up the connection and files to be created, retrieved and deleted
    file_for_tests = 'dummy_file_for.txt'
    test_dict = {'bucket_name':'test-for-boto','region_name':'eu-west-1'}
    test = S3(**test_dict)
    ## First set of tests: 'main' functions
    print(test.put("main_file.txt","This file will not be deleted for Third set of tests."))
    print(test.put(file_for_tests,"some text inside of it"))
    print(test.get(file_for_tests))
    print(test.pop(file_for_tests))
    ## Second set of tests: 'interface' functions
    print(test.__setitem__(file_for_tests,"new content inside of the file"))
    print(test.__getitem__(file_for_tests))
    print(test.__delitem__(file_for_tests))
    ## Third set of tests: check functions
    print(test.put(file_for_tests,"some text inside of it"))
    print(test.__contains__(file_for_tests))
    print(test.__contains__("dummy_name_nor_present.txt"))
    print(next(test.keys("")))
    print(next(test.keys(file_for_tests)))
    print(next(test.items("")))
    print(next(test.items(file_for_tests)))

