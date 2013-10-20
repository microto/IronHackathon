__author__ = 'tomerz'
from services import *
from abstract import ServiceTypes


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


class ProxyIPS(ServiceTypes):
    """
    Tor IPS Collector
    """
    def get_ips(self):
        hide_my_ass = HideMyAss()
        return {self.__class__.__name__: hide_my_ass.get_ips()}

