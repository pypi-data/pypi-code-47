from Spitzer.result import export_report, export_table, export_sql

import os
import json

result = {}
hosts = {}

def add_pages(host, pages):
    global result
    check(host)
    result[host]['webpages'] += pages


def add(host, title, text):
    global result
    check(host)
    result[host]['findings'] += {title:text}

def check(host):
    global result
    if host not in result:
        result[host] = {}
        result[host]['findings'] = []
        result[host]['webpages'] = []

def export_vulns():
    f = open(os.path.expanduser("~") + '.spitzer_result.json', 'w+')
    f.write(json.dumps(result))
    f.close()

def save_hosts(nmap):
    global hosts

    for ip, value in nmap.items():
        if ip not in hosts:
            hosts[ip] = {}
        for port, val in value['tcp'].items():
            hosts[ip][port] = [val['name'], val['product'], val['version']]

def get_hosts():
    global hosts
    return hosts

def get_result():
    global result
    return result