__author__ = 'tomerz'
from requests import get


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
        pass

    def _parse_ips(self):
        pass

    def get_ips(self):
        pass


class TorStatus(IPService):
    """
    Tor Status Service
    """
    def _request_ips(self):
        req = get("http://torstatus.blutmagie.de/ip_list_all.php/Tor_ip_list_ALL.csv")
        res = req.content
        return res

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
        pass


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
        tor_ips = TorIPS()
        ips = tor_ips.get_ips()
        return ips


def main():
    """
    Test Function (Main)
    """
    print IronBlockIPS.get_ips()

if __name__ == "__main__":
    main()