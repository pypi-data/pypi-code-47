#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Le référentiel d'information de Guichet Entreprises est mis à disposition
# selon les termes de la licence Creative Commons Attribution - Pas de
# Modification 4.0 International.

# Pour accéder à une copie de cette licence, merci de vous rendre à l'adresse
# suivante :
# http://creativecommons.org/licenses/by-nd/4.0/
# ou envoyez un courrier à Creative Commons, 444 Castro Street, Suite 900,
# Mountain View, California, 94041, USA.
# -----------------------------------------------------------------------------

import logging
import sys
import os
import re
import shutil

from pymdtools import common
from pymdtools import filetools
from pymdtools import mistunege as mistune
from pymdtools import mdfile


from . import ref
from . import normalize

__key_re__ = r"[^\w]*(?P<category>[a-zA-Z]+)[^\w]*(?P<num>[0-9]+)"

# -----------------------------------------------------------------------------
# Get title in md text
# @param title the title of markdown text
# @param lang the language
# @return the corrected text
# -----------------------------------------------------------------------------
def correct_title(title, lang="fr"):
    key = check_key(title)
    info = ref.get_info_ref(key, lang=lang)
    result = "%s - %s" % (info['key'], info['name'])

    return result

# -----------------------------------------------------------------------------
# Check key reference
# @param key the key to check
# @return the key corrected
# -----------------------------------------------------------------------------
def check_key(key):
    result = ""
    match = re.search(__key_re__, key)

    if not match:
        raise Exception('Key error %s is not a key' % (key))

    category = match.group('category').upper()
    if category == "QP":
        category = "DQP"
    if category == "S":
        category = "DS"
    num = int(match.group('num'))

    result = "%s%03d" % (category, num)

    return result


# -----------------------------------------------------------------------------
# Classify ref file
# -----------------------------------------------------------------------------
def classify_md_ref(filename, md_filename):
    result = {}
    filename = os.path.split(md_filename)[1]
    match = re.search(r"(QP|S)[ ]*([0-9][0-9][0-9])", filename.upper())
    match_src = re.search(r"SOURCE", filename.upper())

    result['good'] = (match is not None) and (match_src is None)
    if result['good']:
        result['key'] = check_key(filename)
    return result

# -----------------------------------------------------------------------------
# Classify ref file
# -----------------------------------------------------------------------------
def classify_md_source(filename, md_filename):
    result = {}
    filename = os.path.split(md_filename)[1]
    match_src = re.search(r"SOURCES", filename.upper())
    match_key = re.search(r"(QP|S)[ ]*([0-9][0-9][0-9])", md_filename.upper())
    result['good'] = (match_src is not None) and (match_key is not None)
    if result['good']:
        result['key'] = check_key(match_key.group(0))
    return result

# -----------------------------------------------------------------------------
# Fill the folder with data
# -----------------------------------------------------------------------------
def filter_md(folders_list, classify):
    ref_dict = {}
    bad_list = []

    # -------------------------------------------------------------------------
    def sort_function(md_filename):
        md_filename = common.check_is_file_and_correct_path(md_filename)

        filename = os.path.split(md_filename)[1]
        result_classify = classify(filename, md_filename)

        if result_classify['good']:
            key = result_classify['key']
            if key not in ref_dict:
                ref_dict[key] = []
            ref_dict[key].append(md_filename)
        else:
            bad_list.append(md_filename)
    # -------------------------------------------------------------------------

    for folder in folders_list:
        common.apply_function_in_folder(
            folder, sort_function, filename_ext=".md")

    print("--------------------------------------------")
    print("   Not classified:%s" % len(bad_list))
    print("--------------------------------------------")
    # for filename in bad_list:
    #     print(filename)
    print("--------------------------------------------")
    print("   Too many result")
    print("--------------------------------------------")
    for key in ref_dict:
        if len(ref_dict[key]) > 1:
            print("%s" % key)
            for filename in ref_dict[key]:
                print("\t%s" % filename)

    print("--------------------------------------------")
    print("   Classified %d" % len(ref_dict.keys()))
    print("--------------------------------------------")
    return ref_dict


# -----------------------------------------------------------------------------
# Fill the folder with data
# -----------------------------------------------------------------------------
def fill_referential(sources, dest, fun_classify, ext, do_copy=True):
    logging.info("Fill folder start %s", ext)

    ref_sources = filter_md(sources, fun_classify)

    if not do_copy:
        return

    print("--------------------------------------------")
    print("Find %s files " % (len(ref_sources.keys())))
    print("--------------------------------------------")
    files_exists = {}
    for key in ref_sources:
        src_filename = ref_sources[key][0]
        dest_filename = os.path.join(dest,
                                     ref.get_info_ref(key)['path'],
                                     ref.get_info_ref(key)['filename'] + ext)

        dest_filename = common.set_correct_path(dest_filename)

        if os.path.isfile(dest_filename):
            files_exists[key] = src_filename
        else:
            print("%s - copy file %s" % (key, dest_filename))
            shutil.copy(src_filename, dest_filename)


# -----------------------------------------------------------------------------
# Check folder Tree
# -----------------------------------------------------------------------------
def check_folder_tree(root):
    root = common.check_folder(root)

    # check normalize folder
    normalize_folder_ok = []
    normalize_folder_ko = []
    for key in ref.get_info_ref_keys():
        normalize_folder = os.path.join(root, ref.get_info_ref(key)['path'])
        if os.path.isdir(normalize_folder):
            normalize_folder_ok.append(normalize_folder)
        else:
            normalize_folder_ko.append(normalize_folder)

    print("--------------------------------------------")
    print("   Folder OK:%s" % len(normalize_folder_ok))
    print("   Folder to create:%s" % len(normalize_folder_ko))
    print("--------------------------------------------")

    for folder in normalize_folder_ko:
        print("Create %s" % folder)
        os.makedirs(folder)

# -----------------------------------------------------------------------------
# Check folder Tree
# -----------------------------------------------------------------------------
def count_files(dest):
    keys = ref.get_info_ref_keys()

    count = {}
    langs = ['fr', 'en', 'src']  # "src" special lang

    for key in keys:
        the_ref = ref.get_info_ref(key)
        if the_ref['category'] not in count:
            count[the_ref['category']] = {'nb': 0}
            for lang in langs:
                count[the_ref['category']][lang] = 0

        count[the_ref['category']]['nb'] += 1

        for lang in langs:
            temp = ref.get_info_ref(key, lang=lang)
            target_filename = os.path.join(dest,
                                           temp['path'],
                                           temp['filename'])
            if os.path.isfile(target_filename):
                count[the_ref['category']][lang] += 1

    for category in count:
        msg = "%5s -> " % category
        for lang in langs:
            msg += " %3s (%3s/%3s)" % (lang, count[category][lang],
                                       count[category]['nb'])
        print(msg)


# -----------------------------------------------------------------------------
# Apply to file ref
# -----------------------------------------------------------------------------
def apply_to_fileref(lang="fr", key_filter=None,
                     apply_fun=None, save=False, backup=True, refresh=True,
                     **kwargs):
    logging.info("Apply fun to %s", key_filter)
    keys = ref.get_ref(lang=lang, refresh=refresh)

    # filter keys
    if key_filter:
        pattern = re.compile(key_filter)
        sub_list = []
        for k in keys:
            if pattern.search(k) is not None:
                sub_list.append(k)
        keys = sub_list

    # filter lang
    sub_list = []
    for k in keys:
        if lang in ref.get_ref(k):
            sub_list.append(k)
    keys = sub_list

    logging.info("Found %s keys", len(keys))

    if not isinstance(apply_fun, list):
        apply_fun = [apply_fun]

    count = 0
    count_max = len(keys)

    # Apply fun
    for key in keys:
        temp = ref.get_ref(key, lang=lang)

        target_filename = common.set_correct_path(temp['filename'])

        count += 1
        logging.info("%03d/%03d - Apply to %s %s", count, count_max,
                     key, target_filename)
        if not os.path.isfile(target_filename):
            logging.info("%03d/%03d --> not a file", count, count_max)
            continue

        md_file = mdfile.MarkdownContent(filename=target_filename,
                                         backup=backup, **kwargs)

        for the_fun in apply_fun:
            if the_fun is not None:
                md_file = the_fun(md_file, key, lang)

        if save:
            md_file.process_tags()
            md_file.write()
