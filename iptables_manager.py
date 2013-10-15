__author__ = 'romanl'

import subprocess
import pymongo

conn = pymongo.Connection()
db = conn.iptables
blacklist = db.blacklist
whitelist = db.whitelist


class IpTablesManager(object):

    def add_ips_to_block_list(self, ips):
        counter = 0
        for ip in ips:
            exists = blacklist.find_one({'IP': ip})
            if not exists:
                subprocess.call('iptables -I INPUT -s {0} -j DROP'.format(ip), shell=True)
                blacklist.insert({'IP': ip})
                counter += 1
        print 'Added {0} Rules to table'.format(counter)

    def remove_ips_from_block_list(self, ips):
        for ip in ips:
            subprocess.call('iptables -D INPUT -s {0} -j DROP'.format(ip))

    def get_blacklist(self):
        return blacklist.find()

    def get_whitelist(self):
        return whitelist.find()

    def add_to_whitelist(self, ips):
        for ip in ips:
            exists = blacklist.find_one({'IP': ip})
            if not exists:
                whitelist.insert({'IP': ip})

    def remove_from_whitelist(self, ips):

        for ip in ips:
            whitelist.remove({'IP': ip})

    def flush(self, with_db=True):
        subprocess.call('iptables -t filter -F ', shell=True)

        if with_db:
            blacklist.remove()
            whitelist.remove()


def main(*args, **kwargs):

    mgr = IpTablesManager()


if __name__ == '__main__':
    main()