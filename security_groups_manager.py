__author__ = 'romanl'

import iptc
ADD_TEMPLATE = '{ip}/255.255.255.255'

class IpTablesManager(object):
    def __init__(self):
        self._chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    def add_ips_to_block_list(self, ips):
        #chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        for ip in ips:
            rule = iptc.Rule()
            rule.in_interface = 'eth+'
            rule.src = ADD_TEMPLATE.format(ip=ip)
            target = iptc.Target(rule, 'DROP')
            rule.target = target
            self._chain.insert_rule(rule=rule)

    def remove_ips_from_block_list(self, ips):
        pass

    def get_blacklist(self):
        return self._chain.rules

    def get_whitelist(self):
        pass


def main(*args, **kwargs):

    mgr = IpTablesManager()
    mgr.add_ips_to_block_list(['9.9.9.9'])
    print [rule.src for rule in mgr.get_blacklist()]

if __name__ == '__main__':
    main()