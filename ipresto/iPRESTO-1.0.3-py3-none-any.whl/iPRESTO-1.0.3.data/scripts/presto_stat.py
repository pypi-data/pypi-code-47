#!python
'''
Author: Joris Louwen
Student number: 960516530090

Script to convert the genes in BGCs into strings of domains, filter BGCs
based on similarity, and detect sub-clusters based on a statistical method
and an LDA alorithm.

Usage:
python3 presto-stat.py -h

Example usage:
python3 presto-stat.py -i ./testdata -o ./testdata_domains
--hmm_path ./domains/Pfam_100subs_tc.hmm --exclude final -c 12 -e True

Notes:
Only handles first cluster from a gbk file

Required:
python 3 (build on python 3.6)
Biopython
hmmscan
networkx
'''

import argparse
from Bio import SeqIO
from Bio import SearchIO
from collections import OrderedDict, Counter, defaultdict
from copy import deepcopy
from functools import partial
from glob import glob, iglob
from itertools import combinations, product, islice, chain
from math import floor, log10
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
import networkx as nx
from operator import itemgetter
import os
import random
import re
from statsmodels.stats.multitest import multipletests
import subprocess
from sympy import binomial as ncr
import time

def get_commands():
    parser = argparse.ArgumentParser(description="The PRESTO-STAT module from\
        iPRESTO which detects statistical sub-clusters in BGCs by turning\
        BGCs from gbk files into strings of domains using a domain hmm\
        database, after which redundancy is reduced by filtering out similar\
        BGCs, and sub-clusters are detected according to Del Carratore et\
        al. (2019).")
    parser.add_argument("-i", "--in_folder", dest="in_folder", help="Input \
        directory of gbk files", required=True)
    parser.add_argument("--exclude", dest="exclude", default=["final"],
        nargs="+", help="If any string in this list occurs in the gbk \
        filename, this file will not be used for the analysis. \
        (default: final)")
    parser.add_argument("-o", "--out_folder", dest="out_folder", 
        required=True, help="Output directory, this will contain all output \
        data files.")
    parser.add_argument("--hmm_path", dest="hmm_path", required=True,
        help="File containing domain hmms that is hmmpress-processed.")
    parser.add_argument("-c", "--cores", dest="cores", default=cpu_count(), 
        help="Set the number of cores the script may use (default: use all \
        available cores)", type=int)
    parser.add_argument("-v", "--verbose", dest="verbose", required=False,
        action="store_true", default=False, help="Prints more detailed \
        information.")
    parser.add_argument("-d", "--domain_overlap_cutoff", 
        dest="domain_overlap_cutoff", default=0.1, help="Specify at which \
        overlap percentage domains are considered to overlap. Domain with \
        the best score is kept (default=0.1).")
    parser.add_argument("-e", "--exclude_contig_edge",
        dest="exclude_contig_edge", default=False, help="\
        Exclude clusters that lie on a contig edge (default = false)",\
        action="store_true")
    parser.add_argument("-m", "--min_genes", dest="min_genes", default=0,
        help="Provide the minimum size of a BGC to be included in the \
        analysis. Default is 0 genes", type=int)
    parser.add_argument("--min_doms", dest="min_doms", default=0,
        help="The minimum amount of domains in a BGC to be included in the \
        analysis. Default is 0 domains", type=int)
    parser.add_argument("--sim_cutoff", dest="sim_cutoff", default=0.95,
        help="Cutoff for cluster similarity in redundancy filtering (default:\
        0.95)", type=float)
    parser.add_argument("-p", "--pval_cutoff", dest="pval_cutoff", \
        default = 0.1, type=float, help='P-value cutoff for determining a \
        significant interaction in module detection (default: 0.1)')
    parser.add_argument("--use_fastas", dest="use_fastas", default=None, \
        help="Use already created fasta files from some folder")
    parser.add_argument("--use_domtabs", dest="use_domtabs", default=None, \
        help="Use already created domtables from some folder")
    parser.add_argument("--include_list", dest="include_list", default=None, \
        help="If provided only the domains in this file will be taken into \
        account in the analysis. One line should contain one Pfam ID \
        (default: None - meaning all Pfams from database)")
    parser.add_argument("--start_from_clusterfile", default=None, help="A file\
        with BGCs and domain-combinations to start with (csv and domains in a\
        gene separated by ';'). This overwrites in_folder (which still has to\
        be supplied symbolically) and use_domtabs/use_fastas.")
    parser.add_argument("--no_redundancy_filtering",default=False,help="If \
        provided, redundancy filtering will not be performed",\
        action="store_true")
    return parser.parse_args()

def process_gbks(input_folder, output_folder, exclude, exclude_contig_edge,\
    min_genes, cores, verbose, existing_fasta_folder):
    '''Convert gbk files from input folder to fasta files for each gbk file

    input_folder, outpu_folder: str
    exclude: list of str, files will be excluded if part of the file name
        is present in this list
    exclude_contig_edge: bool
    min_genes: int
    verbose: bool, print additional info to stdout
    '''
    if not os.path.isdir(output_folder):
        subprocess.check_call("mkdir {}".format(output_folder), shell = True)
    if input_folder.endswith('/'):
        base, inf = os.path.split(input_folder[:-1])
    else:
        base, inf = os.path.split(input_folder)
    out_fasta = os.path.join(output_folder, inf+'_fasta')
    if not os.path.isdir(out_fasta):
        subprocess.check_call("mkdir {}".format(out_fasta), shell = True)
    print("\nProcessing gbk files into fasta files.")
    files = iglob(os.path.join(input_folder, "*.gbk"))
    done = []
    pool = Pool(cores, maxtasksperchild=20)
    for file_path in files:
        pool.apply_async(convert_gbk2fasta, args=(file_path, out_fasta,\
            exclude_contig_edge, min_genes, exclude, verbose, \
            existing_fasta_folder), callback=lambda x: done.append(x))
    pool.close()
    pool.join()
    processed = [val for val in done if val]
    fastas_in_existing_folder = [val for val in processed if type(val)==str]
    excluded = len([val for val in done if val == False])
    filtered = len([val for val in done if val == None])
    print("Processed {} gbk files into {} fasta files.".format(\
        len(processed)+excluded+filtered, len(processed)))
    print(" excluded {} files containing {}".format(excluded,\
        ' or '.join(exclude)))
    print(" filtered {} files that didn't pass constraints".format(\
        filtered))
    return out_fasta, fastas_in_existing_folder

def convert_gbk2fasta(file_path, out_folder, exclude_contig_edge, min_genes,\
    exclude, verbose, existing_fasta_folder):
    '''Convert one gbk file to a fasta file in out_folder

    file_path, out_folder: strings
    exclude_contig_edge: bool
    min_genes: int
    verbose: bool, print additional info to stdout

    Returns True for a successful conversion to fasta, None if there is a
    contig edge or min_genes is not passed. False is returned if any of
    the exclude list is in the filename

    If the fasta file already exists in the existing_fasta_folder, the fasta
    file is not created, True is returned
    '''
    file_name = os.path.split(file_path)[1]
    if any([word in file_name for word in exclude]):
        return False
    name = file_name.split('.gbk')[0]
    name_extend = '{}.fasta'.format(name)
    outfile = os.path.join(out_folder, name_extend)
    if existing_fasta_folder:
        existing_file = os.path.join(existing_fasta_folder, name_extend)
    else:
        existing_file = 'not_an_existing_file'
    seqs = OrderedDict()
    num_genes = 0
    if not os.path.isfile(outfile) and not os.path.isfile(existing_file):
        try:
            record = next(SeqIO.parse(file_path, 'genbank'))
        except ValueError as e:
            print(" Excluding {}: {}".format(file_path, e))
            return
        for feature in record.features:
            if feature.type == 'cluster':
                if "contig_edge" in feature.qualifiers:
                    if feature.qualifiers["contig_edge"][0] == "True":
                        if exclude_contig_edge:
                            if verbose:
                                print("  excluding {}: {}".format(file_name,\
                                    "contig edge"))
                            return
            if feature.type == 'CDS':
                gene_id = "gid:"
                if "gene" in feature.qualifiers:
                    gene_id += feature.qualifiers.get('gene',"")[0]
                    gene_id = gene_id.replace('_','-')
                protein_id = "pid:"
                if "protein_id" in feature.qualifiers:
                    protein_id += feature.qualifiers.get('protein_id',"")[0]
                    protein_id = protein_id.replace('_','-')
                start = feature.location.start
                end = feature.location.end
                strand = feature.location.strand
                if strand == 1:
                    strand = '+'
                else:
                    strand = '-'
                loc = 'loc:{};{};{}'.format(start,end,strand)
                head = '_'.join([name,gene_id,protein_id,loc])
                head = head.replace(">","") #loc might contain this
                head = head.replace("<","")
                header = ">{}_{}".format(head, num_genes+1)
                header = header.replace(' ','') #hmmscan uses space as delim
                seqs[header] = feature.qualifiers.get('translation',[""])[0]
                if seqs[header] == '':
                    print('  {} does not have a translation'.format(header))
                num_genes +=1
        if num_genes < min_genes:
            if verbose:
                print("  excluding {}: less than {} genes".format(file_path,\
                    min_genes))
            return
        with open(outfile, 'w') as out:
            for seq in seqs:
                compl_header = '{}/{}'.format(seq,num_genes)
                out.write('{}\n{}\n'.format(compl_header, seqs[seq]))
    elif not os.path.exists(outfile):
            return existing_file
    return True

def run_hmmscan(fasta_file, hmm_file, out_folder, verbose, \
    existing_dom_folder):
    """
    Runs hmmscan on fasta file to generate a domtable file

    fasta_file, hmm_file, out_folder: strings of file paths
    verbose: bool
    """
    if os.path.isfile(fasta_file):
        name = os.path.split(fasta_file)[1].split('.fasta')[0]
        new_name = name+".domtable"
        out_name = os.path.join(out_folder, new_name)
        if existing_dom_folder:
            existing_out_name = os.path.join(existing_dom_folder, new_name)
        else:
            existing_out_name = './not_an_existing_file'
        log = os.path.join(out_folder, 'hmmlog.txt')
        if not os.path.isfile(out_name) and not \
            os.path.isfile(existing_out_name):
            hmmscan_cmd = (\
                "hmmscan -o {} --cpu 0 --domtblout {} --cut_tc {} {}".format(\
                log, out_name, hmm_file, fasta_file))
            if verbose:
                print("  " + hmmscan_cmd)
            subprocess.check_call(hmmscan_cmd, shell=True)
        elif os.path.isfile(out_name):
            if verbose:
                print("  {} existed. hmmscan not run again".format(out_name))
        else:
            #return the existing file
            if verbose:
                print("  {} existed. hmmscan not run again".format(\
                    existing_out_name))
            return existing_out_name
    else:
        raise SystemExit("Error running hmmscan: {} doesn't exist".format(\
            fasta_file))
    return False

def hmmscan_wrapper(input_folder, hmm_file, verbose, cores, \
    existing_fasta_files, existing_dom_folder):
    '''
    Runs hmmscan on all fasta files in input_folder with hmm_file as hmm db

    input_folder, hmm_file: strings of file paths
    verbose: bool, if True print additional information
    cores: int, amount of cores to use
    existing_fasta_files: list of str, filepaths of existing fastas to use
    existing_dom_folder: str, file path to a folder to see if a domtab
        already exists
    '''
    if input_folder.endswith('/'):
        out_folder = input_folder[:-7]+'_domtables'
    else:
        out_folder = input_folder[:-6]+'_domtables'
    if not os.path.isdir(out_folder):
        subprocess.check_call("mkdir {}".format(out_folder), shell = True)
    print("\nRunning hmmscan on fastas to generate domtables.")
    if existing_fasta_files:
        files = glob(os.path.join(input_folder, "*.fasta")) + \
            existing_fasta_files
    else:
        files = glob(os.path.join(input_folder, "*.fasta"))
    pool = Pool(cores, maxtasksperchild=20)
    #maxtasksperchild=1:each process respawns after completing 1 chunk
    done = []
    for file_path in files:
        pool.apply_async(run_hmmscan,args=(file_path, hmm_file,
            out_folder, verbose, existing_dom_folder),
            callback=lambda x: done.append(x))
    pool.close()
    pool.join() #make the code in main wait for the pool processes to finish
    domtabs_in_existing_folder = [val for val in done if val]
    print("Processed {} fasta files into domtables.".format(\
        len(files)))
    return out_folder, domtabs_in_existing_folder

def check_domtab(domtab_iterable):
    '''To check if an assertion error is raised while parsing

    domtab_iterable: generator, result of SearchIO.parse
    returns the same generator
    '''
    try:
        first = next(domtab_iterable)
    except StopIteration:
        #no dom hits, parse_domtab will deal with this
        return iter([])
    except AssertionError:
        #some kind of error with the domtable file
        return False
    return chain([first],domtab_iterable)

def parse_domtab(domfile, clus_file, sum_file, min_overlap, verbose):
    '''Parses domtab into a cluster domain file (csv)

    domfile: string, file path
    clus_file: open file for writing
    sum_file: open file for writing
    min_overlap : float, the amount of overlap two domains must have for it
        to be considered overlap

    clus_file will look like this:
    Clus1,dom1;dom2,-(gene without domain)\\nClus2,dom1..
    Genes are separated by commas while domains in the genes are separated
        by ;
    '''
    if verbose:
        print("  parsing domtable {}".format(domfile))
    queries = SearchIO.parse(domfile, 'hmmscan3-domtab')
    cds_before = 0
    #list of lists for the domains in the cluster where each sublist is a gene
    cluster_doms = []
    stop = False
    while not stop:
        try:
            query = next(queries)
        except AssertionError:
            #some kind of error with the domtable file
            print('  error in parsing {} this file is excluded'.format(\
                domfile))
            return
        except StopIteration:
            #end of queries/queries is empty
            stop = True
        else:
            #for every cds that has a hit
            dom_matches = []
            q_id = query.id
            #make sure that bgcs with _ in name do not get split
            bgc,q_id = q_id.split('_gid')
            q_id = q_id.split('_')
            cds_num, total_genes = map(int,q_id[-1].split('/'))
            sum_info = [q.split(':')[-1] for q in q_id[:-1]]
            #for every hit in each cds
            for hit in query:
                match = hit[0]
                domain = match.hit_id
                range_q = match.query_range
                bitsc = match.bitscore
                dom_matches.append((domain, range_q, bitsc))
            dels = []
            if len(query) > 1:
                for i in range(len(query)-1):
                    for j in range(i+1, len(query)):
                        #if there is a significant overlap delete the one with
                        #the lower bitscore
                        if sign_overlap(dom_matches[i][1],dom_matches[j][1],
                            min_overlap):
                            if dom_matches[i][2] >= dom_matches[j][2]:
                                dels.append(j)
                            else:
                                dels.append(i)
            cds_matches = [dom_matches[i] for i in range(len(query)) \
                if i not in dels]
            cds_matches.sort(key=lambda x: x[1][0])
            #bgc g_id p_id loc orf_num tot_orf dom range bitscore
            for match in cds_matches:
                sum_file.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(bgc, \
                    '\t'.join(sum_info), cds_num, total_genes, match[0], \
                    ';'.join(map(str,match[1])),match[2]))
            cds_doms = tuple(dom_m[0] for dom_m in cds_matches)
            #if a cds has no domains print '-' in output
            gene_gap = cds_num - cds_before -1
            if gene_gap > 0:
                gaps = [('-',) for x in range(gene_gap)]
                cluster_doms += gaps
            cluster_doms.append(cds_doms)
            cds_before = cds_num
    if cds_before == 0:
        print(' excluding {} no domain hits present'.format(domfile))
        return
    end_gap = total_genes - cds_num
    if end_gap > 0:
        gaps = [('-',) for x in range(end_gap)]
        cluster_doms += gaps
    clus_file.write('{},{}\n'.format(\
        os.path.split(domfile)[-1].split('.domtable')[0],
        ','.join(';'.join(gene) for gene in cluster_doms)))
    return cluster_doms

def sign_overlap(tup1, tup2, cutoff):
    '''
    Returns true if there is an overlap between two ranges higher than cutoff

    tup1, tup2: tuples of two ints, start and end of alignment
    cutoff: float, fraction that two alignments are allowed to overlap

    Overlap is be calculated with the smallest domain alignment to be strict
    '''
    overlap = len(range(max(tup1[0], tup2[0]), min(tup1[1], tup2[1])))
    if overlap > 0:
        if overlap > min(abs(tup1[0]-tup1[1]), abs(tup2[0]-tup2[1]))*cutoff:
            return True
    return False

def parse_dom_wrapper(in_folder, out_folder, cutoff, verbose, \
    domtabs_in_existing_folder):
    '''Calls parse_domtab on all domtable files to create a clusterfile

    in_folder, out_folder: strings, filepaths
    cutoff: float, cutoff value for domain overlap
    '''
    print("\nParsing domtables from folder {}".format(in_folder))
    if domtabs_in_existing_folder:
        domtables = glob(os.path.join(in_folder, '*.domtable')) + \
            domtabs_in_existing_folder
    else:
        domtables = iglob(os.path.join(in_folder, '*.domtable'))
    in_name = os.path.split(in_folder)[1].split('_domtables')[0]
    out_file = os.path.join(out_folder, in_name+'_clusterfile.csv')
    sumfile = os.path.join(out_folder, in_name+'_dom_hits.txt')
    stat_file = os.path.join(out_folder, in_name+'_domstats.txt')
    domc = Counter()
    with open(out_file, 'w') as out, open(sumfile,'w') as sumf:
        #bgc g_id p_id loc orf_num tot_orf dom range bitscore
        header = ['bgc','g_id','p_id','location','orf_num','tot_orf',\
            'domain','q_range','bitscore']
        sumf.write('{}\n'.format('\t'.join(header)))
        for domtable in domtables:
            doms = parse_domtab(domtable, out, sumf, cutoff, verbose)
            if doms:
                domc.update(doms)
    with open(stat_file, 'w') as stat:
        stat.write("#Total\t{}\n".format(sum(domc.values())))
        for dom, count in domc.most_common():
            stat.write("{}\t{}\n".format(';'.join(dom),count))
    print("Result in {}".format(out_file))
    print(" statistics about doms in {}".format(stat_file))
    return out_file

def read_clusterfile(infile, m_gens, verbose):
    """Reads a clusterfile into a dictionary of {bgc:[(domains_of_a_gene)]}

    infile: str, filepath
    m_gens: int, minimum of genes with domains a cluster should have
    verbose: bool, if True print additional info

    clusters with less than m_gens genes are not returned
    It also returns a dict {bgc:amount_of_domains} where -'s are not counted
    and all domains of all genes are added to an int
    """
    print("\nReading {}".format(infile))
    filtered = 0
    with open(infile, 'r') as inf:
        clus_dict = OrderedDict()
        for line in inf:
            line = line.strip().split(',')
            clus = line[0]
            genes = line[1:]
            g_doms = [tuple(gene.split(';')) for gene in genes]
            if len([g for g in genes if g != ('-',)]) < m_gens:
                filtered +=1
                if verbose:
                    print("  excluding {} less than min genes".format(clus))
                continue
            if not clus in clus_dict.keys():
                clus_dict[clus] = g_doms
            else:
                print("Clusternames not unique, {} read twice".format(clus))
    print("Done. Read {} clusters".format(len(clus_dict)))
    print(" {} clusters have less than {} genes and are excluded".format(\
        filtered,m_gens))
    return clus_dict

def calc_adj_index(clus1, clus2):
    '''Returns the adjacency index between two clusters

    clus1, clus2: list of str, domainlist of a cluster

    If there is an empty gene between two domains these two domains are not
        adjacent
    '''
    #generate all unique domain pairs
    dom_p1 = {tuple(sorted(dp)) for dp in zip(*(clus1[:-1],clus1[1:])) \
        if not '-' in dp}
    dom_p2 = {tuple(sorted(dp)) for dp in zip(*(clus2[:-1],clus2[1:])) \
        if not '-' in dp}
    #if doms are separated by '-' then there are no dom pairs. if happens ai=0
    if not dom_p1 or not dom_p2:
        return 0.0        
    ai = len(dom_p1 & dom_p2)/len(dom_p1 | dom_p2)
    return ai

def is_contained(clus1, clus2):
    '''
    Returns a bool if all domains from one of the clusters are in the other

    clus1, clus2: list of str, domainlist of a cluster
    '''
    one_in_two = all(dom in clus2 for dom in clus1 if not dom == '-')
    two_in_one = all(dom in clus1 for dom in clus2 if not dom == '-')
    if one_in_two or two_in_one:
        return True
    return False

def generate_edges(dom_dict, cutoff, cores, out_folder):
    '''Returns a pair of clusters in a tuple if ai/contained above cutoff

    dom_dict: dict {clus1:[domains]}, clusters linked to domains
    cutoff: float, between 0-1, when clusters are similar
    cores: int, amount of cores used for calculation

    returns a generator
    '''
    print("\nGenerating similarity scores")
    #temp file storing the edges so they are not in memory and passed in pool
    temp_file = os.path.join(out_folder,'temp.txt')
    loose_dom_dict = {bgc:[d for dom in doms for d in dom] \
        for bgc,doms in dom_dict.items()}
    clusters = loose_dom_dict.items()
    pairs = combinations(clusters,2)
    slice_size = int(ncr(25000,2))
    tot_size = ncr(len(clusters),2)
    slce = islice(pairs,slice_size)
    chunk_num = int(tot_size/slice_size)+1
    tloop=time.time()
    #update tempfile with increments of slice_size
    for i in range(chunk_num):
        if i == chunk_num-1:
            #get chunksize of remainder
            chnksize = int(((tot_size/slice_size % 1 * slice_size) / \
                (cores*20))+1)
            if chnksize < 5:
                chnksize = 5
        else:
            #the default used by map divided by 5
            chnksize = int((slice_size/(cores*20))+1)
        pool =  Pool(cores, maxtasksperchild = 10)
        edges_slce = pool.imap(partial(generate_edge, \
            cutoff = cutoff), slce, chunksize=chnksize)
        pool.close()
        pool.join()
        #write to file
        with open(temp_file,'a') as tempf:
            for line in edges_slce:
                if line:
                    tempf.write('{}\n'.format('\t'.join(map(str,line))))
        slce = islice(pairs,slice_size)
        del(edges_slce,pool)
        if i == 0:
            t = (time.time()-tloop)*chunk_num
            t_str = '  it will take around {}h{}m{}s'.format(int(t/3600),\
                int(t%3600/60), int(t%3600%60)) #based on one loop
    print("Done")
    return temp_file

def generate_edge(pair, cutoff):
    '''
    Calculate similarity scores between two bgcs and return if above cutoff

    pair: tuple of 2 strings, 2 clusternames
    d_dict: dict of {clustername:domains}
    cutoff: float
    A tuple is returned that can be read as an edge by nx.Graph.add_edges_from
    '''
    # init_doms(p1,p2)
    (p1,clus1),(p2,clus2) = pair
    #unpack the domains from the gene tuples
    # clus1 = [d for dom in doms1 for d in dom]
    # clus2 = [d for dom in doms2 for d in dom]
    contained = is_contained(clus1, clus2)
    ai = calc_adj_index(clus1, clus2)
    if ai == None:
        print('  error in generate_edge: {}'.format(pair))
    if contained or ai > cutoff:
        # print(pair,ai,contained)
        return(p1,p2,ai,contained)

def generate_graph(edges, verbose):
    '''Returns a networkx graph

    edges: list/generator of tuples, (pair1,pair2,{attributes})
    '''
    g = nx.Graph()
    g.add_edges_from(edges)
    if verbose:
        print('\nGenerated graph with:')
        print(' {} nodes'.format(g.number_of_nodes()))
        print(' {} edges'.format(g.number_of_edges()))
    return g

def read_edges_from_temp(file_path):
    '''Yields edges from temp file
    '''
    tr='True'
    with open(file_path, 'r') as inf:
        for line in inf:
            line = line.strip('\n').split('\t')
            cont = line[-1]==tr
            tup = (line[0],line[1], {'ai':float(line[2]),'contained':cont})
            yield tup

def find_representatives(clqs, d_l_dict, graph):
    '''
    Returns {representative:[clique]} based on bgc with most domains in clique

    clqs: list of lists of strings, cliques of clusters
    d_l_dict: dict of {clus_name:amount_of_domains(int)}
    graph: networkx graph structure of the cliques
    The longest cluster is chosen (most domains). If there are multiple
        longest clusters then the cluster with the least connections is
        chosen (to preserve most information).
    '''
    reps_dict = OrderedDict()
    dels = set() #set of nodes for which a representative has been found
    for cliq in clqs:
        cliq = [clus for clus in cliq if not clus in dels]
        if cliq:
            domlist = [(clus,d_l_dict[clus]) for clus in cliq]
            maxdoml = max(doms[1] for doms in domlist)
            clus_maxlen = [clus for clus, doml in domlist \
                if doml == maxdoml]
            if len(clus_maxlen) > 1:
                min_degr = min([deg for clus, deg in \
                    graph.degree(clus_maxlen)])
                rep = random.choice([clus for clus in clus_maxlen \
                    if graph.degree(clus) == min_degr])
            else:
                rep = clus_maxlen[0]
            try:
                reps_dict[rep].update(cliq)
            except KeyError:
                reps_dict[rep] = set(cliq)
            cliq.remove(rep)
            dels.update(cliq)
    return reps_dict

def find_all_representatives(d_l_dict, g):
    '''Iterates find_representatives until there are no similar bgcs

    d_l_dict: dict of {clus_name:amount_of_domains(int)}
    g: networkx graph structure containing the cliques
    all_reps_dict: dict of {representative:[represented]}
    '''
    print('\nFiltering out similar bgcs.')
    all_reps_dict = {}
    subg = g.subgraph(g.nodes)
    i = 0
    while subg.number_of_edges() != 0:
        print(\
        '  iteration {}, edges (similarities between bgcs) left: {}'.format(\
            i,subg.number_of_edges()))
        cliqs = nx.algorithms.clique.find_cliques(subg)
        #make reproducible by making the cliqs have the same order every time
        #sort first each cliq alphabetically, then cliqs alphabetically,
        #then on length, so longest are first and order is the same
        cliqs = sorted(sorted(cl) for cl in cliqs if len(cl) > 1)
        cliqs.sort(key=len,reverse=True)
        reps_dict = find_representatives(cliqs, d_l_dict, subg)
        subg = subg.subgraph(reps_dict.keys())
        #merge reps_dict with all_reps_dict
        for key, vals in reps_dict.items():
            if not key in all_reps_dict:
                all_reps_dict[key] = vals
            else:
                #merge represented clusters in a new representative
                newvals = []
                for old_rep in vals:
                    #if statement for bgcs already represented by this 
                    #representative and thus no longer in all_reps_dict
                    if old_rep in all_reps_dict.keys():
                        newv = [v for v in all_reps_dict[old_rep]]
                        newvals += newv
                        del all_reps_dict[old_rep]
                all_reps_dict[key] = set(newvals)
        i+=1
    print("Done. {} representatives chosen for {} bgcs".format(\
        len(all_reps_dict.keys()), g.number_of_nodes()))
    return all_reps_dict

def write_filtered_bgcs(uniq_list, rep_dict, dom_dict, filter_file):
    '''Writes three output files and returns filepath to representatives.csv

    uniq_list: list of strings, bgcs that are not similar to others
    rep_dict: dict of {representative:[represented]}, links representative
        bgcs to bgcs that are filtered out.
    dom_dict: dict of {bgc:[(domains_of_a_gene)]}
    filter_file: str, file path
    Writes three files:
        -filtered_clusterfile.csv: same as clusterfile.csv but without bgcs
        that are filtered out
        -representatives.csv: all the bgcs and their representatives as
        >representative\nbgc1,bgc2\n . also uniq_bgcs are there but just as
        >uniq_bgc1\n>uniq_bgc2\n
        -domstats file only for the representative bgcs
    '''
    rep_file = '{}_representative_bgcs.txt'.format(\
        filter_file.split('_filtered_clusterfile.csv')[0])
    stat_file = '{}_domstats.txt'.format(\
        filter_file.split('_clusterfile.csv')[0])
    domc = Counter()
    with open(filter_file, 'w') as filt, open(rep_file, 'w') as rep:
        for bgc in uniq_list:
            rep.write(">{}\n".format(bgc))
            dom_tups = dom_dict[bgc]
            filt.write("{},{}\n".format(bgc, \
                ','.join(';'.join(gene) for gene in dom_tups)))
            domc.update(dom_tups)
        for bgc in rep_dict.keys():
            rep.write(">{}\n{}\n".format(bgc, ','.join(rep_dict[bgc])))
            dom_tups = dom_dict[bgc]
            filt.write("{},{}\n".format(bgc, \
                ','.join(';'.join(gene) for gene in dom_tups)))
            domc.update(dom_tups)
    with open(stat_file, 'w') as stat:
        stat.write("#Total\t{}\n".format(sum(domc.values())))
        for dom, count in domc.most_common():
            stat.write("{}\t{}\n".format(';'.join(dom),count))
    print("\nFiltered clusterfile containing {} bgcs: {}".format(\
        len(uniq_list)+len(rep_dict.keys()),filter_file))
    print("Representative bgcs file: {}".format(rep_file))
    return rep_file

def remove_infr_doms(clusdict, m_gens, verbose):
    '''Returns clusdict with genes replaced  with (-) if they occur < 3

    clusdict: dict of {cluster:[(domains_of_a_gene)]}
    m_gens: int, minimal distinct genes a cluster must have to be included
    verbose: bool, if True print additional info

    Deletes clusters with 1 unique gene
    '''
    print('\nRemoving domain combinations that occur less than 3 times')
    domcounter = Counter()
    domcounter.update([v for vals in clusdict.values() for v in vals \
        if not v == ('-',)])
    deldoms = [key for key in domcounter if domcounter[key] <= 2]
    print('  {} domain combinations are left, {} are removed'.format(\
        len(domcounter.keys())-len(deldoms),len(deldoms)))
    clus_no_deldoms = {}
    for k,v in clusdict.items():
        newv = [('-',) if dom in deldoms else dom for dom in v]
        doml = len({v for v in newv if not v == ('-',)})
        if doml >= m_gens:
            clus_no_deldoms[k] = newv
        else:
            if verbose:
                print('  {} removed as it has less than min_genes'.format(k))
    print(' {} clusters have less than {} genes and are excluded'.format(\
        len(clusdict.keys()) - len(clus_no_deldoms), m_gens))
    return clus_no_deldoms

def remove_dupl_doms(cluster):
    '''
    Replaces duplicate domains in a cluster with '-', writes domain at the end

    cluster: list of tuples, 