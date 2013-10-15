__author__ = 'tomerz'
from requests import get
from csv import reader


class BlockedIPS(object):
    """
    Abstract Class
    """
    def _request_ips(self):
        raise NotImplementedError("Should have implemented this")

    def _parse_ips(self):
        raise NotImplementedError("Should have implemented this")

    def get_ips(self):
        raise NotImplementedError("Should have implemented this")


class DShield(BlockedIPS):
    """
    DShield Malicious IPS
    """
    pass


class TorStatus(BlockedIPS):
    """
    Tor Malicious IPS
    """
    pass


class MaliciousIPS(object):
    """
    Malicious IPS Collector
    """
    def get_ips(self):
        pass


def main():
    req = get("http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv")
    res = req.content

    print res

if __name__ == "__main__":
    main()