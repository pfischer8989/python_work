#!/usr/bin/env python
# from __future__ import print_function
import pyeapi
# from jsonrpclib import Server

# load the conf file and connect to the node
pyeapi.load_config('con.conf')
node = pyeapi.connect_to('mgmt01')

response = node.enable('show version')

print response
   
print (("The switch's system MAC addess is", response[0]['result']["systemMacAddress"]))

