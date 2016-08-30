import requests
import json

"""
Modify these please
"""
url='http://10.0.100.21/ins'
switchuser='admin'
switchpassword='99'

myheaders={'content-type':'application/json-rpc'}
payload=[
    {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "conf t",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "logging server 10.0.100.101 use-vrf management",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "copy run start",
      "version": 1
    },
    "id": 2
  },


 

]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

