#!/usr/bin/env python3

"""
    this module tries to get system network interface and
    get mac address, ip address for each interface
"""

import re
from sysinfo import SysInfo
from subprocess import Popen, PIPE

class NetInterface():
    """
        get system networkk interfacing information
    """
    
    def __init__(self):
        self.devlist = self.getinterface()
        self.devtail = self.ifconfig()

    def getinterface(self):
        """
            get all network interfaces
        """
        check = SysInfo()
        if not check.systemcheck:
            return None
        
        try:
            netdev = open('/proc/net/dev','rb').read().split('\n')
        except IOError:
            return None
        
        devlist = []
        for i in netdev:
            if ':' in i:
                devlist.append(i.split(':')[0].replace(' ',''))
        #print(devlist)
        return devlist
    
    def ifconfig(self):
        """
            get each interface device MAC address and ip address
            through python PIPE with ifconfig command
        """
        ifcon = Popen(['ifconfig'], stdout=PIPE)
        con = ifcon.stdout.read()

        ret = []
        remac = re.compile(r"[0-9A-F:0-9A-F:0-9A-F:0-9A-F:0-9A-F:0-9A-F]{17}", re.IGNORECASE)
        reip  = re.compile(r"[0-9.0-9.0-9.0-9]{7,15}")
        index = []
        for i in self.devlist:
            index.append(con.find(i))
        index.sort()
        index.append(None)

        for i in range(len(self.devlist)):
            segment = con[index[i]:index[i+1]]
            for i in self.devlist:
                if i in segment:
                    dev = i
            #match mac and ip address
            mac = remac.findall(segment)
            ip  = reip.findall(segment)
            if mac:
                if ip:
                    ret.append({dev:(mac[0], ip[0])})
                else:
                    ret.append({dev:(mac[0], None)})
            else:
                if ip:
                    ret.append({dev:(None, ip[0])})
        return ret

def test():
    testnet = NetInterface()

if __name__ == '__main__':
    test()