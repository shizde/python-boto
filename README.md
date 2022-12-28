# python-boto

Class to connect to S3 using Python and boto3.
This is a implementation of a exercise to create a class in order to organize and help the access of a S3 Bucket.

## Connection

```
connection_dictionary = { 'bucket_name': str,'region_name': str }
```

- dict:
  - bucket_name : str
    - The bucket name inside S3
  - region_name : str
    - The AWS region where the bucket is located

```
connection_instance = S3(**test_dict)
```

## Methods

`get(key: str)` - Retrieve an object from the S3 bucket using a given key

`put(key: str, value: str)` - Put a new object in the S3 bucket. Can also modift the content of and existing object

`pop(key: str)` -> str - Removes the object from the S3 bucket and returns it

`__getitem__(key: str)` -> str - Nicer interface for get()

`__setitem__(key: str, value: str)` - Nicer interface for put()

`__delitem__(key: str)` -> None - Nicer interface for pop(). Does not return anything

`__contains__(key: str)` -> bool - Checks if a given object exists inside the S3 bucket

`keys(prefix: str ='')` -> str - Generator that yields the keys from the S3 bucket. Option to filter with a prefix

`items(prefix: str='')` -> tuple - Generator that yields tuples with key-value pairs.
