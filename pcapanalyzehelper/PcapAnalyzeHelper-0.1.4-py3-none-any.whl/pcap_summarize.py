from PcapAnalyzeHelper import pcap_parse, features
from scapy.all import *
from scapy.all import sniff
from scapy.utils import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def loadPcap(pcaps):
    df = pd.DataFrame(columns=features.cols)
    for pcap in pcaps:
        pcapRead = sniff(offline=pcap)
        pcapParsed = pcap_parse.pcap2df(pcapRead)
        df = pd.concat(
            [df, pd.DataFrame([x for x in pcapParsed], columns=features.cols)]
        )

    return df


def cate_summary(df, col, plot=False, num_to_disp=10):
    """
    This function takes the categorical input and do statistics summary and plot.
    
    df: the dataframe;
    col: the categorical column name;
    plot: True to plot histogram;
    num_to_disp: the top number we want to display;
    
    returns the summary of this categorical column and plot if set True.
    """
    series = df[col]
    print("=" * 30)
    if df[col].isnull().sum() > 0:
        Missing = df[col].isnull().sum()
        print("----missing percent----")
        print(Missing / df.shape[0])
    print("----Distribution----")
    print(series.describe())
    print("----Top Levels----")
    lvl_summary = pd.DataFrame(
        df[col].value_counts().nlargest(num_to_disp) / df.shape[0]
    )
    print(lvl_summary)
    if plot:
        plt.figure(figsize=(12, 6))
        ax = sns.countplot(x=col, data=df)
        ax.set(xlabel=col, ylabel="Count")
        plt.show()
    print("=" * 30)


def num_summary(df, col, hist_plt=False):
    """
    This function takes the numerical input and do statistics summary and plot.
    
    df: the dataframe;
    col: the categorical column name;
    plot: True to plot histogram;
    
    returns the summary of this numerical column and plot if set True.
    """
    series = df[col]
    print("=" * 30)
    # if df[col].isnull().sum() > 0:
    Missing = df[col].isnull().sum()
    if Missing > 0:
        print("----missing percent----")
        print(Missing / df.shape[0])
    pct = Missing / df.shape[0]
    if pct < 0.5:
        print("----Distribution of Percentiles----")
        
        qtils = pd.DataFrame(series.quantile([0, 0.1, 0.25, 0.5, 0.75, 0.95, 0.995, 1]))
        print(qtils)
        # print("----Discretize into buckets based on quantile----")
        # series_bucket = pd.qcut(series, [0, 0.15, 0.95, 1], duplicates="drop")
        # print(series_bucket.value_counts() / series_bucket.shape[0])
    if hist_plt:
        plt.figure(figsize=(15, 6))
        plt.hist(df[col], bins=20)
        plt.show()
    print("=" * 30)

