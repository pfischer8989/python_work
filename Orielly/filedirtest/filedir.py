import os
import glob

store = {}

def cwdpath ():
    cwd = os.getcwd()
    return cwd

def dirsearch ():
    dir = glob.glob("*.*")
   
    
    global store

    for x in dir:
    	# global wordcnt =+ 1
        ext = os.path.splitext(x)[1]
       # print(ext)
        
        if ext in store:
           store[ext] += 1
        else:
           store[ext] = 1   
    return store


def output ():
    for key, value in store.items():
        print ("%s has %s " % (key, value))

 

if __name__ == "__main__":
    dirsearch()
    #output()
  

    


