# i- doit API client
api client for the i-doit cmdb JSON RPC API in python3


quite early state ...

##Usage:

#### import the client ####
```
from idoitapiclient import IdoitApiClient as idoit
```

#### set auth params for the api
```
auth = ('admin', 'admin')
```

#### as well as the url
```
url = 'https://demo.i-doit.com/src/jsonrpc.php'
```

#### create instance
```
call = idoit(auth, url)
```

##### build a dictionary with the needed params  
```
params = {
                     "jsonrpc": "2.0",
                     "method": "cmdb.object.create",
                     "params": 
                     {"type": "C__OBJTYPE__SERVER", 
                     "title": "FancyName", 
                     "apikey": "c1ia5q"},
                     "id": 71
                     }
```

##### call the generic request method
```
call.generic_request(params)
```

## Links
- [i-doit community page](https://www.i-doit.org/)
- [i-doit pro page](https://i-doit.com)
- [i-doit pro demo](https://demo.i-doit.com)
- [i-doit knowledge base](https://kb.i-doit.com/display/en)
- [i-doit API reference](https://kb.i-doit.com/download/attachments/7831613/i-doit%20JSON-RPC%201.8.3.pdf?version=1&modificationDate=1488357023614&api=v2)