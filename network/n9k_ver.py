import requests
import json

"""
Modify these please
"""
url='http://10.0.100.22/ins'
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

# print (response)

# 

def jdefault(o):
	return o.__dict__

dictver = json.dumps(response, default=jdefault)

# Identify what type the object is
print response.__class__

# print out the dictionaries key values
print (response.keys())

# Print out the doctionaries values

print (response.values())

# This is messy but works if you want to get things out of nested dictionaries
print response.get("result").get("body").get("kickstart_ver_str")
print response.get("result").get("body").get("chassis_id")
print response.get("result").get("body").get("memory")
print response.get("result").get("body").get("bios_ver_str")
print response.get("result").get("body").get("host_name")

# A better way? 
result = response['result']
body = result['body']

hostname = body['host_name']

# convert if it is a number
bootflash = int (body['bootflash_size'])

print "This is result", result

print "This is body", body

print "The hostname is ",hostname

print "This is bootflash", bootflash





# Looping through the dicts to get what i want. 
# for item in response:
#	print "here she is!", response[item]
#	if item == "result":
#		res = response[item]
#		for x in res:
#			print ("this is result", res[x])
#			if x == "body":
#			 	juice = res[x]
#			 	print "this is juice", juice
#			 	for y in juice:
#			 		print "this is the juice yo!", juice[y]
#
# print "This is the hostname", juice[key:10]


	#for y in response:
		#response.get(y)
	  #  print (y)
	#print (y)





# pretty JSON printing
# print json.dumps(response, sort_keys=True, indent=4)


# for line in dictver:
	#x = json.loads(line)
#	print(line)


# print(json.dumps(response))

# parsed_json = json.loads(response)

