#!/usr/bin/env python
# Using Unix commands in Python

import subprocess
import argparse



def disk_space():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering system info with %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])


def uname():
    uname = "uname"
    uname_arg = "-a"
    subprocess.call([uname, uname_arg])

def route():
    route = 'netstat'
    route_arg1 = '-r'
    route_arg2 = '-n'
    subprocess.call([route, route_arg1, route_arg2])



def intArgs():
    parser = argparse.ArgumentParser(description="Sample Parser")

    parser.add_argument('-u', '--uname', help='i.e -u uname')
    parser.add_argument('-r', '--route', help='i.e dump route table')

    return parser.parse_args()

def parseArgs(args):
    if args.uname and args.route:
        print ("calling {0}".format(args.uname))
        print("calling {0}".format(args.route))
        uname()
        route()
    elif args.uname:
        print ("calling".format(args.uname))
        uname()
    elif args.route:
        print("calling".format(args.route))
        route()
    else:
        print ("No Arguements passed")

def main():
    args = intArgs()
    parseArgs(args)

if __name__ == '__main__':
    main()
