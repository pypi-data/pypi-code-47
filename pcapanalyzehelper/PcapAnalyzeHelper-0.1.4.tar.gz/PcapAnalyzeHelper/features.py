# This gives a column names of the dataframe
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import TCP, UDP

cols = [
    "tos",
    "IP_len",
    "IP_flags",
    "ttl",
    "proto",
    "src_IP",
    "dst_IP",
    "IP_chksum",
    "src_port",
    "dst_port",
    "tcp_seq",
    "tcp_ack",
    "tcp_flags",
    "chksum",
    "window",
    "payload_hex",
]

ip_fileds = [field.name for field in IP().fields_desc]
tcp_fields = [field.name for field in TCP().fields_desc]
udp_fields = [field.name for field in UDP().fields_desc]
