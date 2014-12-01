#!/usr/bin/env python
""" lumos - udp interface for bottlerocket x10 control

TODO:
    - commandline args to br command and allowed expressions, and listening port
"""
import sys
sys.DONT_WRITE_BYTECODE = True
import re
import subprocess
import syslog
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

# allowed expressions
allowed = re.compile('^m[123](,m[123])* on$')

# bottle rocket command
br_cmd = "br -x/dev/ttyUSB0"


class LumosReceiver(DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        if allowed.search(data) is None:
            syslog.syslog(syslog.LOG_ALERT, "Lumos: Rejected '%s' sent from host %s" % (data, host))
            return
        cmd = br_cmd+" "+data.strip()
        ret = subprocess.call(cmd,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            syslog.syslog("Lumos: Called '%s' from %s" % (cmd, host))
        else:
            syslog.syslog(syslog.LOG_ALERT, "Lumos: Failed to call '%s' from %s" % (cmd, host))


reactor.listenMulticast(8005, LumosReceiver(), listenMultiple=True)
reactor.run()
