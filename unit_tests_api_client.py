import unittest
from idoitapiclient import IdoitApiClient as doit


class ApiClientTestCase(unittest.TestCase):

    def test_initialize(self):

        auth = ('admin', 'admin')
        url = 'https://demo.i-doit.com/src/jsonrpc.php'
        ut = doit(auth, url)
        self.assertEqual(ut.auth, ('admin', 'admin'))
        self.assertEqual(ut.url, 'https://demo.i-doit.com/src/jsonrpc.php')

    def test_generic_method(self):
        params = {"jsonrpc": "2.0",
                  "method": "cmdb.object.create",
                  "params": {"type": "C__OBJTYPE__SERVER", "title": "LX0007", "apikey": "c1ia5q"},
                  "id": 71}
        auth = ('admin', 'admin')
        auth2 = ('adin', 'admin')
        url = 'https://demo.i-doit.com/src/jsonrpc.php'
        ut = doit(auth, url)
        self.assertIn('created', ut.generic_request(params))
        ut2 =doit(auth2,url)
        self.assertIn('username', ut2.generic_request(params))

if __name__ == '__main__':
    unittest.main()
