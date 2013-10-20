__author__ = 'tomerz'


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


class ServiceTypes(object):
    """
    Service Types Abstract Class
    """
    def get_ips(self):
        raise NotImplementedError("Should have implemented this")