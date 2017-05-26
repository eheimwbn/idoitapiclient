import unittest
from idoitapiclient import IdoitApiClient as doit


class ApiClientTestCase(unittest.TestCase):
    """
    Unit Test for idoitapiclient. 
    'online' test run against 'demo.i-doit.com' 
    """

    def setUp(self):

        self.auth = ('admin', 'admin')
        self.auth2 = ('adin', 'admin')

        self.url = 'https://demo.i-doit.com/src/jsonrpc.php'

        self.apikey = 'c1ia5q'

        self.params = {"jsonrpc": "2.0",
                       "method": "cmdb.object.create",
                       "params": {"type": "C__OBJTYPE__SERVER", "title": "LX0007"},
                       "id": 71}
        self.params2 = {"jsonrpc": "2.0",
                        "method": "cmdb.object.create",
                        "params": {"type": "C__OBJTYPE__SERVER", "title": "LX0055"},
                        "id": 71}

    def test_initialize(self):
        ut = doit(self.url, self.auth, self.apikey)
        self.assertEqual(ut.auth, ('admin', 'admin'))
        self.assertEqual(ut.url, 'https://demo.i-doit.com/src/jsonrpc.php')
        self.assertEquals(self.apikey, self.apikey)

    def test_generic_method(self):
        ut = doit(self.url, self.auth, self.apikey)
        self.assertIn('created', ut.generic_request(self.params)['message'])
        ut2 = doit(self.url, self.auth2, self.apikey)
        self.assertIn('username', ut2.generic_request(self.params))
        ut.delete_object_by_id(ut.retrieve_object_id('LX0007'))

    def test_retrieve_object_id(self):
        ut = doit(self.url, self.auth, self.apikey)
        ut.generic_request(self.params)
        self.assertFalse(ut.retrieve_object_id('ffggeezz'))
        self.assertTrue(ut.retrieve_object_id('LX0007') > 0)
        ut.delete_object_by_id(ut.retrieve_object_id('LX0007'))

    def test_delete_object(self):
        ut = doit(self.url, self.auth, self.apikey)
        ut.generic_request(self.params)
        self.assertFalse(ut.delete_object_by_id(ut.retrieve_object_id('ffggeezz')))
        self.assertTrue(ut.delete_object_by_id(ut.retrieve_object_id('LX0007')))


if __name__ == '__main__':
    unittest.main()
