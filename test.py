__author__ = 'sapanovich'
from PerconaMonitoring import reportingcluster
import argparse


def main():
    cli_args = argparse.ArgumentParser(description='Util for getting percona cluster service', version='0.0.1')
    cli_args.add_argument('--node_ip', dest='node_ip', action='store', help='Node ip')
    cli_args.add_argument('--list', dest='list', action='store_true')
    args = cli_args.parse_args()
    if args.node_ip is None:
        return 1
    else:
        con = reportingcluster.ReportingCluster(user='admin', passwd='admin', host=args.node_ip, name='test')
    if args.list:
        print con.get_zabbix_node_list()
    return 0


if __name__ == "__main__":
    main()
