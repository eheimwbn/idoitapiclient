# i- doit API client
small api client for the i-doit cmdb JSON RPC API in python3

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
                     "title": "LX0003", 
                     "apikey": "c1ia5q"},
                     "id": 71
                     }
```

##### call the generic request method
```
call.generic_request(params)
```