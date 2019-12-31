
def annotation_snp(res_file, bed_file, p_cut=1.0e-6):
    """
    注释互作检验的SNP信息
    :param res_file: 互作检验结果文件，前两列是互作SNP对的顺序编号，最后一列是P值
    :param bed_file: plink文件
    :param p_cut: P阈值
    :return:
    """
    snp_info = {}
    order = -1
    fin = open(bed_file + '.bim')
    for line in fin:
        order += 1
        arr = line.split()
        snp_info[str(order)] = ' '.join(arr)
    fin.close()
    fout = open(res_file + '.anno', 'w')
    fin = open(res_file)
    line = fin.readline()
    arr = line.split()
    fout.write(' '.join([arr[0], 'snp0_chr', 'snp0_ID', 'snp0_cm', 'snp0_bp', 'snp0_allele1', 'snp0_allele2',
                         arr[1], 'snp1_chr', 'snp1_ID', 'snp1_cm', 'snp1_bp', 'snp1_allele1', 'snp1_allele2']))
    fout.write(' ')
    fout.write(' '.join(arr[2:]))
    fout.write('\n')
    for line in fin:
        arr = line.split()
        if float(arr[-1]) < p_cut:
            fout.write(' '.join([arr[0], snp_info[arr[0]], arr[1], snp_info[arr[1]]]))
            fout.write(' ')
            fout.write(' '.join(arr[2:]))
            fout.write('\n')
    fin.close()
    fout.close()
    return 0
