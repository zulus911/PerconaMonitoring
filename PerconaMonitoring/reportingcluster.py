__author__ = 'sapanovich'

import MySQLdb
from json import dumps


class ReportingCluster:
    DB_USER = ''
    DB_HOST = ''
    DB_NAME = ''
    DB_PASS = ''

    def __init__(self, host, name, user, passwd):
        self.DB_PASS = passwd
        self.DB_NAME = name
        self.DB_HOST = host
        self.DB_USER = user

    def connect_to_mysql(self):
        try:
            con = MySQLdb.connect(host=self.DB_HOST, user=self.DB_USER, passwd=self.DB_PASS, db=self.DB_NAME)
        except:
            print 'error'
        return con.cursor()

    def get_cluster_ip(self):
        result = []
        cursor = self.connect_to_mysql()
        sql = "SHOW GLOBAL STATUS LIKE 'wsrep_incoming_addresses';"
        cursor.execute(sql)
        for row in cursor.fetchall():
            for i in str(row[1]).split(','):
                result.append(i.split(':')[0])
        return result

    def get_cluster_status(self):
        cursor = self.connect_to_mysql()
        sql = "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';"
        cursor.execute(sql)
        for row in cursor.fetchall():
            if row[1] == 'Primary':
                return 1
            else:
                return 0

    def get_cluster_size(self):
        cursor = self.connect_to_mysql()
        sql = "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';"
        cursor.execute(sql)
        for row in cursor.fetchall():
            return row[1]

    def get_node_status(self):
        cursor = self.connect_to_mysql()
        sql = "SHOW GLOBAL STATUS LIKE 'wsrep_local_state';"
        cursor.execute(sql)
        for row in cursor.fetchall():
            return row[1]

    def get_zabbix_node_list(self):
        list_ip = self.get_cluster_ip()
        zabbix_keys = []
        for i in list_ip:
            zabbix_keys.append({'{#PERCONANODE}': i})
        return dumps({'data': zabbix_keys})
