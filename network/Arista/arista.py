import pyeapi

node = pyeapi.connect_to('10.0.100.9')

from pprint import pprint as pp
pp(node.enable('show version'))