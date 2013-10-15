__author__ = 'romanl'

import boto

class SecurityGroupManager(object):
    def __init__(self, **kwargs):
        super(object, self).__init__()
        self._connection = kwargs['username']

    def add_ips_to_block_list(self, ips, security_groups=[]):
        pass

    def remove_ips_from_block_list(self, ips, security_groups=[]):
        pass

    def get_security_groups(self, with_ips=False):
        pass


def main(*args, **kwargs):
    mgr = SecurityGroupManager()

if __name__ == '__main__':
    main()