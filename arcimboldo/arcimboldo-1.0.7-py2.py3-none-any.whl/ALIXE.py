#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a program written by Claudia Millan
# E-mail cmncri@ibmb.csic.es

# Import libraries
# Future imports
from __future__ import print_function
from __future__ import unicode_literals
#from __future__ import division

# Python Modules
from builtins import range
from future import standard_library
standard_library.install_aliases()
import configparser
from collections import Counter
import collections
import pickle
import copy
import math
import itertools
import io
import operator
import os
import shutil
import sys
import time
from multiprocessing import Pool
from termcolor import colored

# Our own modules
import alixe_library as al

def main():
    now = time.time()

    # Reading input from command line / bor

    # NOTE CM maybe some header like in the ARCIMBOLDOs
    if len(sys.argv) == 1:
        print("Email support: ", colored("bugs-borges@ibmb.csic.es", 'blue'))
        print("\nALIXE website: ", colored("http://chango.ibmb.csic.es", 'blue'))
        print("\n")
        print("\nUsage: ")
        print("\nTo generate an example of configuration file: ALIXE.py -f name_conf.bor")
        print("\nTo run with a configuration file: ALIXE.py name_conf.bor ")
        print("\nTo run by command line: ALIXE.py -m mode -i input_folder or arcimboldo_bor -c path_to_chescat_executable ")
        sys.exit(0)
    elif len(sys.argv) == 2: # then it is an ALIXE configuration file
        path_alibor = sys.argv[1]
        # Defaults are found in al.defaults_alixe
        Config = configparser.ConfigParser()
        # Read the defaults first
        Config.readfp(io.StringIO(al.defaults_alixe))
        # Now include whatever found in the user's bor file (we should validate it)
        Config.read(path_alibor)
        path_merged_bor = 'temp.bor'
        file_merged_bor = open(path_merged_bor,'w')
        Config.write(file_merged_bor)
        del file_merged_bor
        ali_confdict = al.read_confibor_alixe(path_merged_bor)
    elif len(sys.argv) == 3: # check the -f
        if sys.argv[1] == '-f':
            try:
                f = open(sys.argv[2], "w")
                f.write(al.defaults_alixe)
                f.close()
            except:
                # print the traceback
                print('Some error occured while writing the configuration file')
                sys.exit(1)
            sys.exit(0)
    else: # Then it must be command line
        #print('SHERLOCK command line options ')
        # /Users/claudia/Dropbox/borges-arcimboldo_claudev/ARCIMBOLDO_FULL/ALIXE.py -m monomer -i tryLTG.bor -c path_chescat
        for indi in range(1,len(sys.argv)):
            if sys.argv[indi] == '-m':
                alixe_mode=sys.argv[indi+1]
            if sys.argv[indi] == '-i':
                alixe_input_info=sys.argv[indi+1]
            if sys.argv[indi] == '-c':
                path_chescat=sys.argv[indi+1]
        #print('SHERLOCK alixe_mode, alixe_input_info',alixe_mode, alixe_input_info)
        ali_confdict = al.generate_minimal_ali_confdict_from_mode_and_input(alixe_mode, alixe_input_info, path_chescat)




    folder_mode, ali_confdict = al.validate_confdict_alixe(ali_confdict)
    print(al.check_dir_or_make_it(ali_confdict['output_folder'], remove=True))

    log_file = open(os.path.join(ali_confdict['output_folder'], 'autoalixe.log'), 'w')
    initial_string = '\n Command line used for autoalixe, started at ' + str(now) + ' was ' + " ".join(sys.argv)
    log_file.write(initial_string)

    list_tuples_pools = []
    PoolTup = collections.namedtuple('PoolTup', 'key_input_info sub_clust_key sub_clust_path')
    if not folder_mode:
        # General structure, as many bors as given
        for i in range(ali_confdict['n_pools']):
            # Save the names and paths for the pools for later steps
            keyinputinfo = 'input_info_' + str(i + 1)
            sub_clust_key = 'clustpool_' + str(i + 1)
            sub_clust_path = os.path.join(ali_confdict['output_folder'], sub_clust_key)
            new_tuple = PoolTup(key_input_info=keyinputinfo, sub_clust_key=sub_clust_key, sub_clust_path=sub_clust_path)
            list_tuples_pools.append(new_tuple)
            # Read the bor file from the ARCIMBOLDO run
            config_obj_arci = configparser.ConfigParser()
            config_obj_arci.read(ali_confdict[keyinputinfo])
            # Generate the clustering folder for this particular pool
            al.check_dir_or_make_it(sub_clust_path, remove=True)
            # Get the computing info from one of them, e.g. the first (I just need one)
            if i == 0:
                ali_confdict = al.get_computing_info_for_alixe(config_obj_arci, ali_confdict)
                ali_confdict = al.get_general_paths_for_alixe(config_obj_arci, ali_confdict)

            # NOTE CM: I am HERE, now need to modify the function of the arcirun
            # in order to prepare each folder separatedly
            al.link_file(folder_for_link=sub_clust_path, path_orifile=ali_confdict['hkl_file'],
                         name_link='reflection.hkl')
            if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                print("\nYou have an ent file, a post-mortem analysis of MPE will be performed")
                al.link_file(folder_for_link=sub_clust_path, path_orifile=ali_confdict['ent_file'],
                             name_link="final_solution.ent")
            ali_confdict = al.get_arcirun_info_for_alixe(config_obj_arci, ali_confdict, sub_clust_path)
            ali_confdict[sub_clust_path]['compute_phs'] = False
    else:  # Folder mode, no previous info from the solutions in principle
        # General structure, as many folders as given
        for i in range(ali_confdict['n_pools']):
            keyinputinfo = 'input_info_' + str(i + 1)
            sub_clust_key = 'clustpool_' + str(i + 1)
            sub_clust_path = os.path.join(ali_confdict['output_folder'], sub_clust_key)

            # initialise the dictionary for this clustering folder
            ali_confdict[sub_clust_path]={}

            new_tuple = PoolTup(key_input_info=keyinputinfo, sub_clust_key=sub_clust_key, sub_clust_path=sub_clust_path)
            list_tuples_pools.append(new_tuple)
            al.check_dir_or_make_it(sub_clust_path, remove=True)
            # list files to understand whether PDBs only or phs files
            list_input_files = os.listdir(ali_confdict[keyinputinfo])
            list_phs = []
            list_pdb = []
            for inp in list_input_files:
                fullpathinp = os.path.join(ali_confdict[keyinputinfo], inp)
                fullpathclu = os.path.join(sub_clust_path, inp)
                shutil.copy(fullpathinp, fullpathclu)
                if inp.endswith('.phs') or inp.endswith('.phi'):
                    list_phs.append(fullpathclu)
                elif inp.endswith('.pdb') or inp.endswith('.pda'):
                    list_pdb.append(fullpathclu)
            if len(list_phs) == 0:
                # Then we need to compute the phs out of the pdb files
                ali_confdict[sub_clust_path]['compute_phs'] = True
            else:
                ali_confdict[sub_clust_path]['compute_phs'] = False

            # We need to set the information required in folder mode that is not available, like we do in bor mode for
            # TODO: once I know all I need put this into a function. Need to sort out all parameters
            # al.get_arcirun_info_for_alixe
            # al.get_computing_info_for_alixe
            # al.get_general_paths_for_alixe
            # e.g. path shelxe
            # e.g. modification shelxe line if there is an ent
            if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                print("\nYou have an ent file, a post-mortem analysis of MPE will be performed")
                al.link_file(folder_for_link=sub_clust_path, path_orifile=ali_confdict['ent_file'],
                             name_link="final_solution.ent")
                ali_confdict['shelxe_line_alixe']=ali_confdict['shelxe_line_alixe']+' -x'



    ent_present = True if 'ent_file' in ali_confdict.keys() else False

    dictio_fragments = {}
    if not folder_mode:
        # Now, depending on the type of run in the case of ARCIMBOLDO input:
        # get the files
        # change their names
        # and link them to the clustering folder

        # Again, general, as many runs as we have set
        for i, ele in enumerate(list_tuples_pools):
            keyinputinfo, sub_clust_key, sub_clust_path = ele[0], ele[1], ele[2]
            # NOTE CM: Need to decide whether this mode stays in the standalone or is only implemented internally for lite
            # if ali_confdict['type_run'] == 'ARCIMBOLDO' and mode.startswith('ens1_frag'):
            #     fragment = mode[9:]
            #     print('Getting the files from an ARCIMBOLDO_LITE run, from the folder of frag ', fragment)
            #     dict_sorted_input = al.get_files_from_ARCIMBOLDO_for_ALIXE(wd=wd_run, clust_fold=clust_fold, fragment=fragment,
            #                                                                hard_limit_phs=hard_limit_phs)

            if ali_confdict[sub_clust_path]['type_run'] == 'ARCIMBOLDO' and \
                    (ali_confdict['alixe_mode'] == 'multimer' or ali_confdict['alixe_mode'] == 'monomer'):
                print('Getting the files from the fragment ', ali_confdict['fragment'], ' of an ARCIMBOLDO_LITE run')
                dict_sorted_input = al.get_files_from_ARCIMBOLDO_for_ALIXE(wd=ali_confdict[sub_clust_path]['wd_run'],
                                                                           clust_fold=sub_clust_path,
                                                                           fragment=ali_confdict['fragment'],
                                                                           hard_limit_phs=ali_confdict[
                                                                               'limit_sol_per_rotclu'])
            elif ali_confdict[sub_clust_path]['type_run'] == 'ARCIMBOLDO' and ali_confdict['alixe_mode'] == 'cc_analysis':
                print('Getting the files from an ARCIMBOLDO_LITE run, fragment number ', fragment)
                dict_sorted_input = al.get_files_from_ARCIMBOLDO_for_ALIXE(wd=ali_confdict[sub_clust_path]['wd_run'],
                                                                           clust_fold=sub_clust_path,
                                                                           fragment=ali_confdict['fragment'],
                                                                           hard_limit_phs=ali_confdict[
                                                                               'limit_sol_per_rotclu'])
            # elif ali_confdict['type_run'] == 'ARCIMBOLDO' and ali_confdict['alixe_mode'] == 'fish':
            #     # NOTE CM then this is performed for all fragments to get all solutions
            #     dict_all_frags = {}
            #     for fichiens in range(1, int(fragment_search)+1):
            #         dict_sorted_input = al.get_files_from_ARCIMBOLDO_for_ALIXE(wd=wd_run, clust_fold=clust_fold, fragment=str(fichiens),
            #                                                                    hard_limit_phs=hard_limit_phs)
            #         dict_all_frags = al.merge_dicts(dict_all_frags,dict_sorted_input)
            elif ali_confdict[sub_clust_path]['type_run'] == "BORGES":
                print('Getting the files from a BORGES run')
                fragment = 1
                dict_sorted_input = {}
                for id_clu in os.listdir(os.path.join(ali_confdict[sub_clust_path]['wd_run'], '9_EXP')):
                    print("Getting files from rotation cluster ", id_clu)
                    # NOTE CM: Only the rigid body refined solutions are taken in the case of BORGES runs
                    dict_sorted_input[id_clu] = al.get_files_from_9_EXP_BORGES(wd=ali_confdict[sub_clust_path]['wd_run'],
                                                                               clust_fold=sub_clust_path,
                                                                               cluster_id=id_clu, mode=9,
                                                                               hard_limit_phs=ali_confdict[
                                                                                   'limit_sol_per_rotclu'])

            print("\nCompleted linking of files in ", sub_clust_path)

            # Checking the figures of merit of the single solutions

            # Just add the key of the pool
            dictio_fragments[sub_clust_key] = {}


            list_pdbs = al.list_files_by_extension(sub_clust_path, 'pda')
            for pdb in list_pdbs:
                dictio_fragments[sub_clust_key][pdb[:-4]] = {'rot_cluster': None, 'llg': None, 'zscore': None,
                                                             'initcc': None, 'efom': None, 'pseudocc': None,
                                                             'list_MPE': None}
            list_phs = al.list_files_by_extension(sub_clust_path, 'phs')
            n_single_solutions = len(list_pdbs)

            print("\nThere are ", n_single_solutions, " single solutions in ", sub_clust_path)

            # FOMs from lst files
            dictio_fragments = al.get_FOMs_from_lst_files_in_folder(dictio_fragments=dictio_fragments,
                                                                    ali_confdict=ali_confdict)

            # From SUMs
            gimble = al.check_if_gimble(ali_confdict[sub_clust_path]['type_run'],
                                        ali_confdict[sub_clust_path]['wd_run'])

            dictio_fragments = al.get_FOMs_from_sum_files_in_folder(wd=ali_confdict[sub_clust_path]['wd_run'],
                                                                    clust_fold=sub_clust_path,
                                                                    dictio_fragments=dictio_fragments,
                                                                    keypool=sub_clust_key,
                                                                    gimble=gimble,
                                                                    program=ali_confdict[sub_clust_path]['type_run'],
                                                                    fragment=ali_confdict['fragment'])

            # Generate the list of rotation clusters that are available for clustering in the pool
            list_rot_cluster = al.get_list_rotation_clusters_from_dictio_fragments(dictio_fragments, sub_clust_key)
            ali_confdict[sub_clust_path]['list_rotation_clusters'] = list_rot_cluster

            # Save information about FOMs of fragments in a file that is readable as a table
            al.write_info_frag_from_dictio_frag(dictio_fragments=dictio_fragments, clust_fold=sub_clust_path,
                                                keypool=sub_clust_key, ali_confdict=ali_confdict)

            # If plotting option is active, prepare plots describing the solutions
            if ali_confdict['plots']:
                al.plots_info_frag(path_files=sub_clust_path, ali_confdict=ali_confdict, folder_mode=folder_mode)

            if i == ali_confdict['n_pools'] - 1:
                # Getting the symmetry information and setting up the files needed
                # NOTE CM: This is just performed on the last iteration
                # NOTE CM: This means that if we ever attempt with different datasets we should change this
                path_sym = os.path.join(ali_confdict[sub_clust_path]['wd_run'], 'best.pda')
                if not os.path.exists(path_sym):
                    path_sym = os.path.join(ali_confdict[sub_clust_path]['wd_run'], 'best.pdb')
                ali_confdict['path_sym'] = path_sym
                # NOTE CM: I think I don't need all of this for the ins
                # anymore with current chescat unless we call shelxe later
                ali_confdict = al.generate_sym_data(ali_confdict['path_sym'], ali_confdict, sub_clust_path)


    else:
        for i, ele in enumerate(list_tuples_pools):
            keyinputinfo, sub_clust_key, sub_clust_path = ele[0], ele[1], ele[2]
            #print('keyinputinfo, sub_clust_key, sub_clust_path',keyinputinfo, sub_clust_key, sub_clust_path)
            list_rot_cluster = ['0']  # just a dummy id, the same for all of them
            ali_confdict[sub_clust_path]['list_rotation_clusters'] = list_rot_cluster
            ali_confdict = al.generate_sym_data(ali_confdict['path_sym'], ali_confdict, sub_clust_path)

            dictio_fragments[sub_clust_key] = {}
            if ali_confdict[sub_clust_path]['compute_phs']:
                # Check if pda or pdbs
                list_pdbs = al.list_files_by_extension(sub_clust_path, 'pda')
                if not list_pdbs:
                    al.get_pdas_for_all_pdbs(sub_clust_path)
                    list_pdbs = al.list_files_by_extension(sub_clust_path, 'pda')
                al.get_links_for_all(sub_clust_path, ali_confdict['hkl_file'][:-4],'pda', 'hkl')
                if 'ent_file' in ali_confdict.keys():
                    al.get_links_for_all(sub_clust_path, ali_confdict['ent_file'][:-4],'pda', 'ent')
                al.phase_all_in_folder_with_SHELXE(ali_confdict['shelxe_line_alixe'], sub_clust_path,
                                                   ali_confdict['shelxe_path'], ali_confdict['number_cores_parallel'],
                                                   False)

                # Now we could get information back from these shelxe runs
                for pdb in list_pdbs:
                    dictio_fragments[sub_clust_key][pdb[:-4]] = {'rot_cluster': None, 'llg': None, 'zscore': None,
                                                                 'initcc': None, 'efom': None, 'pseudocc': None,
                                                                 'list_MPE': None}
                # FOMs from lst files
                dictio_fragments = al.get_FOMs_from_lst_files_in_folder(dictio_fragments=dictio_fragments,
                                                                        ali_confdict=ali_confdict)

                # Save information about FOMs of fragments in a file that is readable as a table
                al.write_info_frag_from_dictio_frag(dictio_fragments=dictio_fragments, clust_fold=sub_clust_path,
                                                    keypool=sub_clust_key, ali_confdict=ali_confdict)

                # If plotting option is active, prepare plots describing the solutions
                if ali_confdict['plots']:
                    al.plots_info_frag(path_files=sub_clust_path, ali_confdict=ali_confdict, folder_mode=folder_mode)


    #######################################
    # Modes of autoalixe: core algorithms #
    #######################################
    if ali_confdict['alixe_mode'] == 'fish':
        dict_clust_by_rotclu = {}
        # NOTE CM: this is a dummy id but will cause problems in the writing of the output
        # , so we have to exit the mode while we do something more standard for the output
        dict_clust_by_rotclu['0'] = {}
        phs_files = al.list_files_by_extension(path=clust_fold, extension='phs', fullpath=False)
        # preparing the parallel mode using more than one reference
        total_references = len(list_references_fish)
        print('\n*****************************************************************************************')
        print('\n The number of cores available to use in the fishing parallel mode will be ', n_cores)
        print('\n The number of references to attempt will be ', total_references)
        print('\n*****************************************************************************************\n\n')
        # In this case, all attempts are independent, it is totally parallel, I can run all the jobs
        list_references_names = [os.path.basename(ele)[:-4] for ele in list_references_fish]
        list_pool_names = [os.path.basename(ele)[:-4] for ele in phs_files]
        list_equal_names = [ele for ele in list_references_names if ele in list_pool_names]
        if len(list_equal_names) == len(list_references_names):
            print('The references are already part of the pool, there is no need to compute anything else')
            list_references_fish = [ele + '.phs' for ele in list_references_names]
        else:
            print('The references are not part of the pool')
            if phs_ref:
                for fichito in list_references_fish:
                    al.link_file(clust_fold, fichito, os.path.basename(fichito))
            else:
                print('TODO: phs files should be generated out of the input coordinate files')
                sys.exit(0)
        list_ls_to_process = []
        for i, path_phs1 in enumerate(list_references_fish):
            name_ref = os.path.basename(path_phs1)[:-4]
            path_ls = os.path.join(clust_fold, name_ref + '_ref.ls')
            al.link_file(clust_fold, path_sym, path_ls[:-3] + ".pda")
            lsfile = open(path_ls, 'w')
            lsfile.write(os.path.basename(path_phs1) + '\n')
            for j in range(len(phs_files)):
                phs_namefile = os.path.basename(phs_files[j])
                if phs_namefile != name_ref + '.phs':
                    lsfile.write(phs_namefile + '\n')
            del lsfile
            list_ls_to_process.append((os.path.basename(path_ls), j - i + 1, os.path.basename(path_phs1)))

        # start your parallel workers at the beginning of your script
        total_ref = len(list_references_fish)
        if total_ref < n_cores:
            pool = Pool(total_ref)
            print('\n\n Opening the pool with ', total_ref, ' workers')
        else:
            pool = Pool(n_cores)
            print('\n\n Opening the pool with ', n_cores, ' workers')

        # prepare the iterable with the arguments
        list_args = []
        for op, tuplels in enumerate(list_ls_to_process):
            namels = tuplels[0]
            phs_in_ls = tuplels[1]
            phs_ref = tuplels[2]
            list_args.append((namels[:-3], clust_fold, path_phstat, resolution, 0, tolerance_first_round, 3,
                              orisub, weight, oricheck, cc_calc))

        # execute a computation(s) in parallel
        pool.map(al.call_phstat_for_clustering_in_parallel_pool, list_args)

        # turn off your parallel workers at the end of your script
        print('Closing the pool')
        pool.close()

        for op, tuplels in enumerate(list_ls_to_process):
            namels = tuplels[0]
            phs_in_ls = tuplels[1]
            phs_ref = tuplels[2]
            output_file = open(os.path.join(clust_fold, namels[:-3] + '.out'), 'r')
            output_content = output_file.read()
            print('***************************************\n')
            print(output_content)
            print('****************************************\n')

            dictio_result, total_runtime = al.read_phstat_isa_clusterization_output(output_content, 3, phs_in_ls)
            al.write_sum_file_from_dictio_result(os.path.join(clust_fold, namels[:-3] + '.sum'), dictio_result)
            name_phi = namels[:-3] + '.phi'
            path_phi = os.path.join(clust_fold, namels[:-3] + '.phi')
            dict_clust_by_rotclu['0'][name_phi] = {'dictio_result': dictio_result, 'n_phs': len(dictio_result.keys()),
                                                   'dict_FOMs': {}}

        # NOTE: clu is a fake id at this point
        for clufa in dict_clust_by_rotclu.keys():
            for clukey in dict_clust_by_rotclu[clufa]:
                if dict_clust_by_rotclu[clufa][clukey]['n_phs'] > 1:
                    print('This reference ', clukey, ' did fish something ')
                    print('Check ', clukey[:-4] + '.sum')
                else:
                    print('No fish!')
        sys.exit(0)


    elif ali_confdict['alixe_mode'] == 'monomer' or ali_confdict['alixe_mode'] == 'multimer':

        for i, ele in enumerate(list_tuples_pools):
            keyinputinfo, sub_clust_key, sub_clust_path = ele[0], ele[1], ele[2]

            # Prepare the input to perform phase clustering inside each rotation cluster
            sizerotclu = len(list_rot_cluster)

            # NOTE CM: This block is required for ARCIMBOLDO_LITE runs only I think (well, for runs with more than 1 frag)
            # NOTE CM: Maybe it can be moved to a function
            new_list_rot_cluster = []
            for i, ele in enumerate(list_rot_cluster):
                list_clu = ele.split('_')
                list_clu = [int(ele) for ele in list_clu]
                list_clu = sorted(list_clu)
                list_clu = [str(ele) for ele in list_clu]
                new_list_rot_cluster.append('_'.join(list_clu))

            # Prepare for saving the output
            dict_clust_by_rotclu = {}  # final dictionary to save the resulting ALIXE clusters

            # Iteration for clustering within each rotation cluster
            for indx, rotclu in enumerate(new_list_rot_cluster):

                print('\n************************************************************************************************')
                print('\n We are processing rotation cluster ', rotclu, ' which is the ', indx + 1, ' out of ', sizerotclu)
                print(
                    '\n************************************************************************************************\n\n')
                if not folder_mode:
                    list_phs_full = [dict_sorted_input[str(rotclu)][i] for i in range(len(dict_sorted_input[str(rotclu)]))]
                    list_phs_rotclu = al.sort_list_phs_rotclu_by_FOM(list_phs_full=list_phs_full,
                                                                     fom_sorting=ali_confdict['fom_sorting'],
                                                                     dictio_fragments=dictio_fragments,
                                                                     keypool=sub_clust_key)
                else:
                    list_phs_rotclu = al.list_files_by_extension(sub_clust_path, 'phs')

                dict_clust_by_rotclu = al.ALIXE_clustering_on_a_set(ali_confdict, dict_clust_by_rotclu, rotclu,
                                                                    list_phs_rotclu,
                                                                    sub_clust_path, tolerance='first')

            # write the output in table format
            al.prepare_output_tables_clustering_alixe(dict_clust_by_rotclu, ali_confdict, sub_clust_path, sub_clust_key,
                                                      dictio_fragments, folder_mode)
            # write the output in pkl format to retrieve it later on
            al.prepare_pickle_clustering_alixe(dict_clust_by_rotclu, sub_clust_path, sub_clust_key)

            # If plotting option is active, prepare plots describing the clustering
            if ali_confdict['plots']:
                path_info_clust = os.path.join(sub_clust_path, sub_clust_key + "_info_clust_table")
                al.plots_info_clust(path_info_clust=path_info_clust, ali_confdict=ali_confdict,
                                    folder_mode=folder_mode)

            # Now we need to either proceed to the second step or finish

            if ali_confdict['alixe_mode'] == 'multimer':

                list_input_clust = al.get_clusters_from_dict_clust_by_rotclu(dict_clust_by_rotclu)
                list_input_clust = [ os.path.join(sub_clust_path,ele) for ele in list_input_clust]
                if len(list_input_clust) > 1:
                    dict_clust_second_round = {}
                    dict_clust_second_round = al.ALIXE_clustering_on_a_set(ali_confdict, dict_clust_second_round, 'R2',
                                                                        list_input_clust,
                                                                        sub_clust_path, tolerance='second')
                    #print('\n SHERLOCK dict_clust_second_round',dict_clust_second_round)
                    # write the output in table format
                    al.prepare_output_tables_clustering_alixe_second_round(dict_clust_second_round, ali_confdict,
                                                                           sub_clust_path, sub_clust_key,
                                                                           dictio_fragments, folder_mode)
                    # write the output in pkl format to retrieve it later on
                    #al.prepare_pickle_clustering_alixe(dict_clust_by_rotclu, sub_clust_path, sub_clust_key)

                    # If plotting option is active, prepare plots describing the clustering
                    # NEED TO CHANGE THE NAMES ETC
                    #if ali_confdict['plots']:
                    #    al.plots_info_clust(path_files=sub_clust_path, postmortem=ali_confdict['postmortem'],
                    #                        folder_mode=folder_mode)

                    if ali_confdict['expansions']:
                         al.perform_SHELXE_expansions_from_dictio_cluster(dict_clust_second_round,
                                                                          ali_confdict, sub_clust_path)

                else:
                    print('\n There was only a single cluster formed in the first step, no second step will be performed')
            else: # Then is monomer, check if expansions and otherwise exit
                if ali_confdict['expansions']:
                    al.perform_SHELXE_expansions_from_dictio_cluster(dict_clust_by_rotclu, ali_confdict, sub_clust_path)

    elif ali_confdict['alixe_mode'].startswith('ens1_frag'):
        print('\n Pending to complete implementation')
        # dict_clust_by_rotclu = {}
        # rotclu = 'arci'  # In this case we consider all clusters together
        # list_phs_full = [dict_sorted_input[key][i] for key in dict_sorted_input.keys() for i in
        #                  range(len(dict_sorted_input[key]))]
        # list_tuple_sort = []
        # for phs in list_phs_full:
        #     phs_key = phs[:-4]
        #     list_tuple_sort.append((phs, dictio_fragments[phs_key]['zscore'], dictio_fragments[phs_key]['llg'],
        #                             dictio_fragments[phs_key]['initcc']))
        # if fom_sorting == 'CC':
        #     list_tuple_sort.sort(key=lambda x: x[3], reverse=True)
        # elif fom_sorting == 'LLG':
        #     list_tuple_sort.sort(key=lambda x: x[2], reverse=True)
        # elif fom_sorting == 'ZSCORE':
        #     list_tuple_sort.sort(key=lambda x: x[1], reverse=True)
        # list_phs_full = [list_tuple_sort[i][0] for i in range(len(list_tuple_sort))]
        # if phstat_version == 'fortran':
        #     # 1) Write an ls file with the list of phs
        #     ref_phs = list_phs_full[0]
        #     path_ls = os.path.join(clust_fold, "first_round.ls")
        #     lsrotfile = open(path_ls, 'w')
        #     # NOTE: I need to use a relative path because fortran does not accept such long paths
        #     for i in range(len(list_phs_full)):
        #         phs_namefile = (os.path.split(list_phs_full[i]))[1]
        #         # phs_relative_path = os.path.join('./CLUSTERING', phs_namefile)
        #         # lsrotfile.write(phs_relative_path + '\n')
        #         lsrotfile.write(phs_namefile + '\n')
        #     lsrotfile.close()
        #     if not os.path.exists(os.path.join(clust_fold, "first_round.ins")):
        #         al.link_file(clust_fold, path_ins, "first_round.ins")
        #     if not os.path.exists(os.path.join(clust_fold, "first_round.pda")):
        #         al.link_file(clust_fold, path_sym, "first_round.pda")
        #     # 3) Launch the function in alixe_library
        #     dict_clust_by_rotclu[rotclu] = al.clustering_phstat_isa_under_a_tolerance(name_phstat='first_round',
        #                                                                               wd=clust_fold,
        #                                                                               path_phstat=path_phstat,
        #                                                                               tolerance=tolerance_first_round,
        #                                                                               resolution=resolution, seed=seed,
        #                                                                               n_cycles=cycles, orisub=orisub,
        #                                                                               weight=weight, idrotclu=rotclu)
    elif ali_confdict['alixe_mode'] == 'cc_analysis':
        for i, ele in enumerate(list_tuples_pools):
            keyinputinfo, sub_clust_key, sub_clust_path = ele[0], ele[1], ele[2]

            phs_files = al.list_files_by_extension(path=sub_clust_path, extension='phs', fullpath=False)
            if not phs_files:
                print('\n There were not phs files found, trying to get phi files')
                phs_files = al.list_files_by_extension(path=sub_clust_path, extension='phi', fullpath=False)
            table_cc_names = open(os.path.join(sub_clust_path, 'corresp_names_ccfiles.txt'), 'w')
            dict_cc_names = {}
            list_ls_to_process = []
            for i, phs1 in enumerate(phs_files):
                table_cc_names.write(str(i + 1) + '\t' + os.path.basename(phs1) + '\n')
                dict_cc_names[os.path.basename(phs1)] = str(i + 1)
                if i < len(phs_files) - 1:
                    path_ls = os.path.join(sub_clust_path, "ref" + str(i + 1) + '.ls')
                    if not os.path.exists(os.path.join(sub_clust_path, path_ls[:-3] + ".pda")):
                        os.link(ali_confdict['path_sym'], os.path.join(sub_clust_path, path_ls[:-3] + ".pda"))
                    lsfile = open(path_ls, 'w')
                    for j in range(i, len(phs_files)):
                        # print '   And including ',phs_files[j]
                        phs_namefile = os.path.basename(phs_files[j])
                        lsfile.write(phs_namefile + '\n')
                    del lsfile
                    list_ls_to_process.append((os.path.basename(path_ls), j - i + 1, os.path.basename(phs1)))
            del table_cc_names

            # start your parallel workers at the beginning of your script
            pool = Pool(int(ali_confdict['number_cores_parallel']))
            print('\n\n Opening the pool with ', ali_confdict['number_cores_parallel'], ' workers')

            # prepare the iterable with the arguments
            list_args = []
            for op, tuplels in enumerate(list_ls_to_process):
                namels = tuplels[0]
                phs_in_ls = tuplels[1]
                phs_ref = tuplels[2]
                list_args.append((namels[:-3], sub_clust_path, ali_confdict['path_chescat'],
                                 ali_confdict['resolution_merging'], 1, 100, 1, ali_confdict['origin_search'],
                                 ali_confdict['weight'], ali_confdict['oricheck'], ali_confdict['map_cc'], True))

            # execute a computation(s) in parallel
            pool.map(al.call_chescat_for_clustering_global, list_args)

            # turn off your parallel workers at the end of your script
            print('Closing the pool')
            pool.close()

            input_for_ccanalysis = open(os.path.join(sub_clust_path, 'alixecc.dat'), 'w')
            info_relations = open(os.path.join(sub_clust_path, 'global_table.dat'), 'w')
            info_relations.write('%-35s %-35s %-12s %-12s %-12s %-12s %-12s %-12s \n' % (
                'File1', 'File2', 'mapCC', 'wMPD', 'diffwMPD', 'shiftX', 'shiftY', 'shiftZ'))

            for op, tuplels in enumerate(list_ls_to_process):
                namels = tuplels[0]
                phs_in_ls = tuplels[1]
                phs_ref = tuplels[2]
                output_path = os.path.join(sub_clust_path, namels[:-3] + '.out')
                list_dictio_results = al.process_chescat_output_multiseed(output_path, 1, phs_in_ls, 1)
                dictio_result = {}
                list_remove = []
                dictio_result, list_remove, clubool = al.process_list_dictio_results_to_global(list_dictio_results,
                                                                                               dictio_result,
                                                                                               list_remove,
                                                                                               namels[:-3],
                                                                                               sub_clust_path)
                # Note: in this case, there is only one cycle so dictio_result first and last entries are the same
                ref_id = dict_cc_names[phs_ref]
                for keyphi in dictio_result.keys():
                    keyphs = os.path.basename(keyphi)[:-8]+'.phs'
                    comp_id = dict_cc_names[keyphs]
                    comp_name = os.path.basename(keyphi)
                    if ref_id == comp_id:
                        continue
                    mapcc_scaled1 = (dictio_result[keyphi][0][2][keyphs]['mapcc_first']) / 100
                    wmpd = dictio_result[keyphi][0][2][keyphs]['wMPE_first']
                    diffwmpd = dictio_result[keyphi][0][2][keyphs]['diff_wMPE_first']
                    shiftx = dictio_result[keyphi][0][2][keyphs]['shift_first'][0]
                    shifty = dictio_result[keyphi][0][2][keyphs]['shift_first'][1]
                    shiftz = dictio_result[keyphi][0][2][keyphs]['shift_first'][2]
                    input_for_ccanalysis.write('\t' + str(ref_id) + '\t' + str(comp_id) + '\t' + str(mapcc_scaled1) + '\n')
                    info_relations.write('%-35s %-35s %-12s %-12s %-12s %-12s %-12s %-12s \n' % (
                        phs_ref, comp_name, mapcc_scaled1, wmpd, diffwmpd, shiftx, shifty, shiftz))
            del input_for_ccanalysis
            del info_relations
            # Remove the phi files resulting from this mode
            phi_to_remove = al.list_files_by_extension(sub_clust_path, 'phi')
            phi_to_remove = [ele for ele in phi_to_remove if (os.path.basename(ele)).startswith('ref')]
            for phi in phi_to_remove:  # Remove all the files with ref, not only the phi
                try:
                    os.remove(phi)
                    os.remove(phi[:-4] + '.ls')
                    os.remove(phi[:-4] + '.pda')
                    # At the moment I keep them just to be able to check if everything is OK.
                    # os.remove(phi[:-4]+'.out')
                except:
                    pass

    # Print final time and close log file before finishing
    new_now = time.time()
    final_string = '\nTotal time spent in running autoalixe is ' + str((new_now - now)) + ' seconds , or ' + str(
        (new_now - now) / 60) + ' minutes \n Command line used was ' + " ".join(sys.argv)
    log_file.write(final_string)
    print(final_string)
    del log_file


if __name__ == "__main__":
    main()
