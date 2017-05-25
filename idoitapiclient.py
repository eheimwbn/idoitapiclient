import requests
import json


class IdoitApiClient():
    """
    idoit JSON-RPC client
    in python 3
    """

    def __init__(self, auth: tuple, url: str):
        """
        :param auth: basic auth for i-doit api  as tuple with ('name', 'password')
        :param url: url to i-doit api as string 'https://demo.i-doit.com/src/jsonrpc.php'
        """
        self.headers = {"Content-Type": "application/json" }
        self.auth = auth
        self.url = url

    def generic_request(self, params: dict):
        """
        generic call to api
        :param params: dict with api method and api params 
        :return: API message as string 
        """
        response = requests.post(self.url, auth=self.auth, headers=self.headers, data=json.dumps(params))
        dict = json.loads(response.text)
        print(dict)
        if 'error' in dict.keys():
            return dict['error']['data']['error']
        elif dict['result']['success'] is True:
            return dict['result']['message']

