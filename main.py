from MalliciousIPBlocker import IronBlockIPS
from iptables_manager import IpTablesManager

class IronWall(object):
    def __init__(self):
        self.ips = {}

    def main(self):
        self.ips = IronBlockIPS().get_ips()
        print "Adding %s ips" % len(self.ips['TorIPS'])
        mgr = IpTablesManager()
        mgr.add_ips_to_block_list(self.ips['TorIPS'])
        #print [rule.src for rule in mgr.get_blacklist()]

if __name__ == "__main__":
    o = IronWall()
    o.main()