import requests
import json
import random


class IdoitApiClient():
    """
    idoit JSON-RPC client
    in python 3
    """

    def __init__(self, url: str, auth: tuple, apikey: str):
        """
        :param auth: basic auth for i-doit api  as tuple with ('name', 'password')
        :param apikey: api key generated by i-doit 
        :param url: url to i-doit api as string 'https://demo.i-doit.com/src/jsonrpc.php'
        """
        self.headers = {"Content-Type": "application/json"}
        self.auth = auth
        self.url = url
        self.apikey = apikey
        self.api_id = random.randint(1, 99)

    def generic_request(self, params: dict):
        """
        generic call to api
        :param params: dict with api method and api params 
        :return: API message as string 
        """
        params['params']['apikey'] = self.apikey
        params['id'] = self.api_id
        response = requests.post(self.url, auth=self.auth, headers=self.headers, data=json.dumps(params))
        dict = json.loads(response.text)
        #print(dict)
        if 'error' in dict.keys():
            return dict['error']['data']['error']
        else:
            return dict['result']

    def retrieve_object_id(self, name: str):
        """
        retrieves cmdb id of given object
        :param name: name of the object as string
        :return: id as int if fond, Flase if not found
        """
        params = {
            "jsonrpc": "2.0",
            "method": "cmdb.objects",
            "params": {
                'filter': {

                },
                "language": "en"},
        }
        params['params']['filter']['title'] = name
        result = self.generic_request(params)
        if not result == []:
            return int(result[0]['id'])
        else:
            return False

    def delete_object_by_id(self, object_id: int):
        """
        Deletes object by its id
        :param object_id: object id as integer
        :return: True if successful, False if errors appeared 
        """
        params = {
            "jsonrpc": "2.0",
            "method": "cmdb.object.delete",
            "params": {
                'status': 'C__RECORD_STATUS__DELETED',
               },
        }
        params['params']['id'] = object_id
        result = self.generic_request(params)
        if not result == []:
            return result['success']
        else:
            return False



