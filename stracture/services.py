__author__ = 'tomerz'
from requests import get
from datetime import date
from xml.etree import ElementTree
from re import findall, DOTALL, sub, search

from abstract import IPService


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


class HideMyAss(IPService):
    """
    Tor Status Service
    """
    def _parse_ips(self):
        ips = list()
        i = 1

        while i < 100:
            req = get("http://hidemyass.com/proxy-list/%d" % i)
            res = req.content
            try:
                table = findall('<table id="listtable".*?>(.*?)</table>', res, DOTALL)[0]
            except IndexError:
                break

            trs = findall('<tr class=".*?"  rel="\d+">(.*?)</tr>', table, DOTALL)
            for tr in trs:
                td = findall('<td>(.*?)</td>', tr, DOTALL)
                style = findall("<style>(.*?)</style>", td[0], DOTALL)[0]
                td[0] = sub(style, "", td[0])
                hidden_class = findall('\.(.*?)\{display:none}', style)
                for klass in hidden_class:
                    td[0] = sub('<[^>]*?class="%s">\d+</[^>]*?>' % klass, "", td[0])
                td[0] = sub('<[^>]*?style="display:none">(\d+)</[^>]*?>', "", td[0])
                ips.append(sub('<[^>]*?>', '', td[0]))
            if search('<li class="inactivepagination nextpageinactive">Next.*?</li>', res):
                break
            i += 1
        return ips

    def get_ips(self):
        return self._parse_ips()
