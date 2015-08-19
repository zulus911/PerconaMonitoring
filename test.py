__author__ = 'sapanovich'
from PerconaMonitoring import reportingcluster
import argparse


def main():
    cli_args = argparse.ArgumentParser(description='Util for getting status percona cluster service')
    cli_args.add_argument('--version', action='version', version="0.0.1")
    cli_args.add_argument('--node_ip', dest='node_ip', action='store', help='Node ip')
    cli_args.add_argument('--list', dest='list', action='store_true', help="List ip cluster nodes")
    cli_args.add_argument('--status_cluster', dest='status_cluster', action='store_true', help='Cluster status')
    cli_args.add_argument('--status_node', dest='status_node', action='store_true', help='Node status')
    cli_args.add_argument('--size_cluster', dest='size_cluster', action='store_true', help="number node's in cluster")
    args = cli_args.parse_args()
    if args.node_ip is None:
        print "Please use cluster/node ip"
        return 1
    else:
        con = reportingcluster.ReportingCluster(user='admin', passwd='admin', host=args.node_ip, name='test')
    if args.list:
        print con.get_zabbix_node_list()
        return 0
    if args.status_cluster:
        print con.get_cluster_status()
        return 0
    if args.status_node:
        print con.get_node_status()
        return 0
    if args.size_cluster:
        print con.get_cluster_size()
        return 0
    print "Execute python test.py --help for help"
    return 0

if __name__ == "__main__":
    exit(main())
