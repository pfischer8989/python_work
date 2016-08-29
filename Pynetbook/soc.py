#!/usr/local/bin/python3
# Python Networking 

# importing the socket module
import socket
from binascii import hexlify

mod = dir(socket)

# get the local fulley qualified domain name of the host
host_name = socket.getfqdn()

# get the IP address of the host
ip = socket.gethostbyname(host_name)

print "The local hostname is ", host_name
print "The local IP: ", ip

# Get the remote hosts IP address
def get_remote_machine_info():
    remote_host = 'www.catdevnull.ca'
    try:
       print "The Remote IP address: %s" %socket.gethostbyname(remote_host)
    except socket.error, err_msg:
       print "%s: %s" %(remote_host, err_msg)


# find the name for the following open ports
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
    print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

# change the IP addr to hex
def hexify(x):
	for ip_addr in [ip]:
		packed_ip = socket.inet_aton(ip_addr)
		unpacked = socket.inet_ntoa(packed_ip)
		print "IP Address: %s => Packed: %s, Unpacker: %s" %(ip_addr, hexlify(packed_ip), unpacked)


# get service name for port
def servicename(port, protocolname):
	print "Port: %s => service_anem: %s" %(port, socket.getservbyport(port, protocolname))

# convert to bytes
def convert_int():
	data = 11833
	print "Orginal: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data))
	print "Orginal: %s => Short host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data))

# Set the socket timeout to 100  
def set_sock_timeout():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(100)
	print "Current sock timeout %s" %s.gettimeout()


get_remote_machine_info()
find_service_name()
hexify(ip)
servicename(3389, 'tcp')
convert_int()
set_sock_timeout()


