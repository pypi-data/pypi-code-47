import numpy as np
import pandas as pd
from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import TCP, UDP
import binascii
import functools as fct


def ip2long(ip):
    """
    convert an IP string to long
    """
    ip2num = fct.reduce(lambda a, b: (a << 8) + b, map(int, ip.split(".")), 0)
    return ip2num


def pcap2df_lgt(pcap):
    """
    This function gives the 5 tuple infromation of pcap
    """
    for packet in pcap:

        proto = packet[IP].proto
        src_IP = packet[IP].src
        dst_IP = packet[IP].dst

        layer_type = type(packet[IP].payload)

        try:
            src_port = packet[layer_type].sport
            dst_port = packet[layer_type].dport
        except:
            src_port = None
            dst_port = None
        yield (proto, src_IP, dst_IP, src_port, dst_port)


def pcap2df(pcap):
    """
    This function extracts the fields from IP, TCP and UDP for each packet.
    """
    for packet in pcap:
        tos = packet[IP].tos
        IP_len = packet[IP].len
        IP_flags = packet[IP].flags
        ttl = packet[IP].ttl
        proto = packet[IP].proto
        src_IP = packet[IP].src
        dst_IP = packet[IP].dst
        IP_chksum = packet[IP].chksum
        layer_type = type(packet[IP].payload)

        try:
            src_port = packet[layer_type].sport
            dst_port = packet[layer_type].dport
        except:
            src_port = None
            dst_port = None
        try:
            tcp_seq = packet[layer_type].seq
            tcp_ack = packet[layer_type].ack
            tcp_flags = packet[layer_type].flags
            chksum = packet[layer_type].chksum
            window = packet[layer_type].window
        except:
            tcp_seq = None
            tcp_ack = None
            tcp_flags = None
            chksum = None
            window = None
        # if UDP protocol, check the payload
        if proto == 17:
            payload_hex = binascii.hexlify(packet[layer_type].payload.original)
        else:
            payload_hex = None
        yield (
            tos,
            IP_len,
            IP_flags,
            ttl,
            proto,
            src_IP,
            dst_IP,
            IP_chksum,
            src_port,
            dst_port,
            tcp_seq,
            tcp_ack,
            tcp_flags,
            chksum,
            window,
            payload_hex,
        )


def process_payload(df, pld_vec=0, cut=20):
    """
    df: The dataFrame parsed from pcapfile;
    pld_vec : to vectorize the payload or not; return the first 20 digits of the hexified number if 0; return 256 vector with
              corresponding counts as feature value.
    
    This function process the payload and return the dataframe afterwards.
    """
    if pld_vec == 0:
        df["payload_hex"] = df["payload_hex"].apply(
            lambda x: "" if x is None else x.decode()[0:cut]
        )

        return df
    else:
        df["payload_hex"] = df["payload_hex"].apply(
            lambda x: "" if x is None else x.decode()
        )
        # arr stores the unique payload
        arr = []
        for load in list(df["payload_hex"].unique()):
            arr.append(load)

        # payload vectors are seperated by each every 2 digits
        vec_dict = list(set([arr[0][i : i + 2] for i in range(0, len(arr[0]), 2)]))
        for vect in arr[1:]:
            vec_tmp = [vect[i : i + 2] for i in range(0, len(vect), 2)]
            for wd in vec_tmp:
                if wd not in vec_dict:
                    vec_dict.append(wd)
        token_dict = {key: 0 for key in vec_dict}

        # this function create a dictionary with key as 2-digits gram and value as the count
        def map_vec(token_dict, wd_lst):
            hmap = token_dict.copy()
            for wd in wd_lst:
                if wd in hmap:
                    hmap[wd] = hmap[wd] + 1
                else:
                    hmap[wd] = 1
            return hmap

        # create payload_vector dataframe which is  the count of each 2-digits gram
        payload_vec = []
        for arrlst in arr:
            test = [arrlst[i : i + 2] for i in range(0, len(arrlst), 2)]
            payload_vec.append(map_vec(token_dict, test))

        payload_vec = pd.DataFrame(payload_vec)
        pld_cols = list(payload_vec.columns)
        payload_vec = pd.concat([payload_vec, pd.Series(arr)], axis=1).rename(
            columns={0: "original"}
        )
        df_new = pd.merge(
            df, payload_vec, left_on="payload_hex", right_on="original", how="left"
        )

        return pld_cols, df_new
