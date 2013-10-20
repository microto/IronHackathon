__author__ = 'tomerz'
from datetime import datetime

from stracture.servicetypes import *
from json import dumps
#from time import sleep


#Update Interval In Minutes
UPDATE_INTERVAL = 30


class IronBlockIPS(ServiceTypes):
    """
    IronBlock Collector
    """
    @staticmethod
    def get_ips():
        #Create Ips Object
        ips = dict()

        #Create TorIPS Instance And Update
        tor_ips = TorIPS().get_ips()
        ips.update(tor_ips)

        #Create MaliciousIPS Instance And Update
        malicious_ips = MaliciousIPS().get_ips()
        ips.update(malicious_ips)

        #Create MaliciousIPS Instance And Update
        proxy_ips = ProxyIPS().get_ips()
        ips.update(proxy_ips)

        #Create DateTime Instance And Update
        ips.update({'DateTime': str(datetime.now())})

        #Return Ips Object
        return ips


def get_ips_length(ip_dicts):
    size = 0
    val = ip_dicts.values()

    for i in range(len(val) - 1):
        size += len(val[i])

    return size


def main():
    #Configuration
    print dumps(IronBlockIPS.get_ips())

if __name__ == "__main__":
    main()