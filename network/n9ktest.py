import requests
import json

"""
Modify these please
"""
url='http://10.0.100.21/ins'
switchuser='admin'
switchpassword='L@bbeR0ck99'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh ver",
      "version": 1
    },
    "id": 1
  }
]


response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

data = json.loads(response)

#print response

#print data[1]