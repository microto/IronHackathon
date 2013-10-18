from MalliciousIPBlocker import IronBlockIPS
from iptables_manager import IpTablesManager
import json
from boto.s3.connection import S3Connection
from boto.s3.key import Key

#Defines
AWS_ID = ''
AWS_PASS = ''


class IronWall(object):
    def __init__(self):
        self.ips = {}

    def main(self):
        self.ips = IronBlockIPS().get_ips()


        conn = S3Connection(AWS_ID, AWS_PASS)
        bucket = conn.get_bucket("iron_block_ips")
        key = Key(bucket)
        key.key = 'blacklist_json'
        self.ips = json.loads(key.get_contents_as_string())
        self.ips = self.ips['MaliciousIPS']

        mgr = IpTablesManager()
        mgr.add_ips_to_block_list(self.ips)



if __name__ == "__main__":
    o = IronWall()
    o.main()