import requests
import json

"""
Modify these please
"""



url='http://10.0.100.21/ins'
switchuser='admin'
switchpassword='put_your_password_here'

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
      "cmd": "feature nxapi",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "feature lldp",
      "version": 1
    },
    "id": 3
  },
    {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "feature bash-shell",
      "version": 1
    },
    "id": 4
  },


]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

