import os

def checkit ():
   x = os.getcwd()
   return x


foo = checkit()

print ("this is foo", foo)