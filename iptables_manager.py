__author__ = 'romanl'

import iptc
ADD_TEMPLATE = '{ip}/255.255.255.255'


class IpTablesManager(object):

    def add_ips_to_block_list(self, ips):
        import subprocess
        counter = 0
        for ip in ips:
            subprocess.call('iptables -I INPUT -s {0} -j DROP'.format(ip), shell=True)
            counter += 1
        print 'Added {0} Rules to table'.format(counter)
        #for chain_counter in xrange(len(ips)/500):
        #    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        # for ip in ips[chain_counter * 500:(chain_counter + 1) * 500]:

                #rule = iptc.Rule()
                #rule.in_interface = 'eth+'
                #rule.src = ADD_TEMPLATE.format(ip=ip)
                #target = iptc.Target(rule, 'DROP')
                #rule.target = target
                #chain.append_rule(rule=rule)

    def remove_ips_from_block_list(self, ips):
        pass

    def get_blacklist(self):
        return self.rules

    def get_whitelist(self):
        pass


def main(*args, **kwargs):

    mgr = IpTablesManager()
    mgr.add_ips_to_block_list(['9.9.9.9'])
    print [rule.src for rule in mgr.get_blacklist()]

if __name__ == '__main__':
    main()