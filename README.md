# i- doit API client
api client for the i-doit cmdb JSON RPC API in python3


quite early state ...

## Usage:

#### import the client ####
```python
from idoitapiclient import IdoitApiClient as idoit
```

#### set up the connection to the api
```python
url = 'https://demo.i-doit.com/src/jsonrpc.php'
auth = ('admin', 'admin')
apikey = 'c1ia5q'

# create instance 
call = idoit(url, auth, apikey)

# build a dictionary with the needed params  
params = {
             "jsonrpc": "2.0",
             "method": "cmdb.object.create",
             "params":  {
                 "type": "C__OBJTYPE__SERVER", 
                 "title": "FancyName", 
                        },
             }
             
# call the generic request method
call.generic_request(params)
```
returns the (error)message from API   


## Objects 
### Find object by its name

```python

call.retrieve_object_id(name)
```
given __name__ as string  <br />
method returns __id__ as int or __false__ if object is not found

### Delete object by its id
:exclamation: careful object ist deleted not archived :exclamation:
```python

call.delete_object_by_id(object_id)
```
given __object_id__ as int  <br />
method returns __True__ if object is deleted and __false__ if object_id is not found


## Links
- [i-doit community page](https://www.i-doit.org/)
- [i-doit pro page](https://i-doit.com)
- [i-doit pro demo](https://demo.i-doit.com)
- [i-doit knowledge base](https://kb.i-doit.com/display/en)
- [i-doit API reference](https://kb.i-doit.com/download/attachments/7831613/i-doit%20JSON-RPC%201.8.3.pdf?version=1&modificationDate=1488357023614&api=v2)