__author__ = 'tomerz'
from requests import get
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from datetime import datetime, date
from json import dumps
from xml.etree import ElementTree
from time import sleep

#Defines
AWS_ID = 'AKIAIUP2RDZ5ICKX2JRQ'
AWS_PASS = 'rrQcsSEtweIAKtRw3WOzMBfOtFNQUPO6ncrALhcx'
#Update Interval In Minutes
UPDATE_INTERVAL = 30


class IPService(object):
    """
    Services Abstract Class
    """
    def _request_ips(self):
        raise NotImplementedError("Should have implemented this")

    def _parse_ips(self):
        raise NotImplementedError("Should have implemented this")

    def get_ips(self):
        raise NotImplementedError("Should have implemented this")


class DShield(IPService):
    """
    DShield Service
    """
    def _request_ips(self):
        num_of_ips = 1000
        today = date.today().isoformat()
        req = get("http://www.dshield.org/api/topips/attacks/{0}/{1}".format(num_of_ips, today))
        return req.content

    def _parse_ips(self):
        ips = list()

        root = ElementTree.fromstring(self._request_ips())
        for ipaddress in root.findall("ipaddress"):
            source = ipaddress.find("source")
            ips.append(".".join([num.lstrip('0') for num in source.text.split('.')]))

        return ips

    def get_ips(self):
        return self._parse_ips()


class TorStatus(IPService):
    """
    Tor Status Service
    """
    def _request_ips(self):
        req = get("http://torstatus.blutmagie.de/ip_list_all.php/Tor_ip_list_ALL.csv")
        return req.content

    def _parse_ips(self):
        res = self._request_ips()
        return res.split("\n")

    def get_ips(self):
        filtered_res = filter(None, self._parse_ips())
        return filtered_res


class ServiceTypes(object):
    """
    Service Types Abstract Class
    """
    def get_ips(self):
        raise NotImplementedError("Should have implemented this")


class MaliciousIPS(ServiceTypes):
    """
    Malicious IPS Collector
    """
    def get_ips(self):
        dshield = DShield()
        return {self.__class__.__name__: dshield.get_ips()}


class TorIPS(ServiceTypes):
    """
    Tor IPS Collector
    """
    def get_ips(self):
        tor_status = TorStatus()
        return {self.__class__.__name__: tor_status.get_ips()}


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
    """
    Main Function
    """
    conn = S3Connection(AWS_ID, AWS_PASS)
    #Create Bucket If Needed
    try:
        conn.create_bucket('iron_block_ips')
    finally:
        bucket = conn.get_bucket("iron_block_ips")

    key = Key(bucket)
    key.key = 'blacklist_json'

    while True:
        iron_ips = IronBlockIPS.get_ips()
        key.set_contents_from_string(dumps(iron_ips))
        print '{0}\t=>\tUpdated {1} IPs.'.format(datetime.now(), get_ips_length(iron_ips))
        sleep(UPDATE_INTERVAL * 60)

if __name__ == "__main__":
    main()