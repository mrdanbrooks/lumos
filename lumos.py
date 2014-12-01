#!/usr/bin/env python
""" lumos - udp interface for bottlerocket x10 control

TODO:
    - commandline args to br command and allowed expressions
"""
import re
import subprocess
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

# allowed expressions
allowed = re.compile('^m[123](,m[123])* on$')

# bottle rocket command
br_cmd = "br -x/dev/ttyUSB0"

class LumosReceiver(DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        # Filter input for allowed commands
        if allowed.search(data) is None:
            print "Rejected %s" % data
            return
        print "Received %s" % data
        ret = subprocess.call(br_cmd+" "+data,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if not ret == 0:
            print "Command Failed!"
        else:
            print "success"


reactor.listenMulticast(8005, LumosReceiver(), listenMultiple=True)
reactor.run()
