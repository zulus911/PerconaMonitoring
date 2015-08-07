__author__ = 'sapanovich'
from PerconaMonitoring import reportingcluster
import argparse


def main():
    cli_args = argparse.ArgumentParser(description='Util for getting percona cluster service')
    cli_args.add_argument('--node_ip', dest='node_ip', action='store', help='Node ip')
    cli_args.add_argument('')