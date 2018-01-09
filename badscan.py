#/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

#clear screen

#subprocess.call('clear', shell=True)

#user input/dns lookup

remoteServer = raw_input("enter a host to scan...")

remoteServerIP = socket.gethostbyname(remoteServer)

#user notification

print "-" * 60

print "wait while port scanner completes!...."

print "-" * 60

# take starting timestamp

t1 = datetime.now()


#declare list of open ports

openports = []

#iterate over common ports

try:
    for port in range (1,81):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:     Open".format(port)
            openports.append(port)

        else:
            print "Port {}:     Closed".format(port)

        sock.close()


#user quit

except KeyboardInterrupt:

    print "exiting"
    sys.exit()


#error handling

except socket.gaierror:

    print "Hostname could not be resolved"
    sys.exit

except socket.error:

    print "could not connect to server"
    sys.exit

#check end time

t2 = datetime.now()

#calc script runtime

total = t2 - t1

#print time to complete

print "scan completed in " , total
print "\n"
print "RESULTS"

for port in openports:
    print "\n"
    print "Open Port:   " + str(port)