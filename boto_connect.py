import boto3

class Connection:
    list_of_keys = []
    def __init__(self, key: str):
        self.__key = ''



    def get(self, key: str) -> BytesIO:
        pass

    def put(self, key: str, value: BytesIO):
        pass 

    def pop(self, key: str) -> BytesIO:
        pass

    def __getitem__(self, key: str) -> BytesIO:
        pass

    def __setitem__(self, key: str, value: BytesIO):
        pass

    def __delitem__(key: str):
        pass

    def __contains__(key: str) -> bool:
        pass

    def keys(prefix: str ='') -> str:
        return self.__key

    def items(prefix: str='') -> tuple:
        pass

