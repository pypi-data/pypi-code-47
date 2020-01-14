from PcapAnalyzeHelper import pcap_parse, features, pcap_summarize
import time
import sys


def pcap_stat(pcaps):
    """
    This function generate general statistics from pcaps.
    """
    start = time.time()
    df = pcap_summarize.loadPcap(pcaps)

    ## process payload
    df = pcap_parse.process_payload(df, pld_vec=0)

    print("-" * 4 + "check protocol" + "-" * 4)
    pcap_summarize.cate_summary(df, col="proto")
    print("-" * 4 + "check source port" + "-" * 4)
    pcap_summarize.cate_summary(df, col="src_port")
    print("-" * 4 + "check source IP" + "-" * 4)
    pcap_summarize.cate_summary(df, col="src_IP")
    print("-" * 4 + "check destination port" + "-" * 4)
    pcap_summarize.cate_summary(df, col="dst_port")
    print("-" * 4 + "check IP length" + "-" * 4)
    pcap_summarize.cate_summary(df, col="IP_len")
    pcap_summarize.num_summary(df, col="IP_len")
    print("-" * 4 + "check IP flags" + "-" * 4)
    pcap_summarize.cate_summary(df, col="IP_flags")
    print("-" * 4 + "chksum" + "-" * 4)
    pcap_summarize.cate_summary(df, col="chksum")
    print("-" * 4 + "check ttl" + "-" * 4)
    pcap_summarize.num_summary(df, col="ttl")

    if 17 in df["proto"].values:
        print("-" * 4 + "check UDP payload" + "-" * 4)
        pcap_summarize.cate_summary(df[df["proto"] == 17], col="payload_hex")

    if 1 in df["proto"].values:
        print("-" * 4 + "check the TCP flags" + "-" * 4)
        pcap_summarize.cate_summary(df, col="tcp_flags")
        print("-" * 4 + "check the TCP ACK (A)" + "-" * 4)
        pcap_summarize.num_summary(df, col="tcp_ack")
        print("-" * 4 + "check window (S)" + "-" * 4)
        pcap_summarize.num_summary(df, col="window")

    print("parse passed {elapsed} seconds".format(elapsed=time.time() - start))

