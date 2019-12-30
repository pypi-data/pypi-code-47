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
import git
import shutil

from pymdtools import common
from pymdtools import filetools
from pymdtools import mistunege as mistune
from pymdtools import mdfile
from pymdtools import mdrender
from pymdtools import convert_md_to_pdf


from . import ref
from . import folder
from . import normalize

# -----------------------------------------------------------------------------
def short_name(name):
    name = common.str_to_ascii(name)
    name = name.replace("'", " ")
    return common.slugify(common.limit_str(name, 30, ' ', min_last_word=3))

# -----------------------------------------------------------------------------
def url_name(name):
    name = common.str_to_ascii(name)
    name = name.replace("'", " ")
    return common.slugify(name)

# -----------------------------------------------------------------------------
# check and change the include file in the header
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_newline(md_content, unused_key=None, unused_lang=None):
    result = md_content.content
    result = result.replace("\r\n", "\n")
    result = result.replace("\n\n\n", "\n\n")
    result = result.replace("\n\n\n\n", "\n\n")
    result = result.replace("\n\n\n\n\n", "\n\n")
    result = result.replace("->\n\n<!-", "->\n<!-")
    result = result.replace("->\n\n\n<!-", "->\n<!-")
    result = result.replace("->\n\n\n\n<!-", "->\n<!-")
    result = result.replace("->\n\n\n\n\n<!-", "->\n<!-")
    result = result.replace("->\n\n\n\n\n\n<!-", "->\n<!-")
    result = result.replace("->\n\n\n\n\n\n\n<!-", "->\n<!-")
    md_content.content = result

    return md_content


# -----------------------------------------------------------------------------
# check and change the include file in the header
#
# @return the MD.
# -----------------------------------------------------------------------------
def code_ape(md_content, unused_key=None, unused_lang=None):
    toc = md_content.toc
    __ape_re__ = r"<li><a.*>(?P<title>.*APE.*)</a></li>"
    match_begin = re.search(__ape_re__, toc)

    # finish if no match
    if not match_begin:
        print("APE Title not found")
        return md_content

    # There is a match
    title = match_begin.group('title')
    ape_part = r"(?P<part>###\s" + re.escape(title) + r".*)\s##\s2"
    ape_part = re.compile(ape_part, re.MULTILINE | re.DOTALL)
    match_part = re.search(ape_part, md_content.content)
    if not match_part:
        print("APE Part not found  -> nothing done")
        return md_content
    part = match_part.group('part')

    verif = re.search("##", part[3:])
    if verif:
        print("WARNING bad part of APE -> nothing done")
        return md_content

    md_content.content = md_content.content.replace(part, "")

    return md_content

# -----------------------------------------------------------------------------
# check and change the include file in the header
#
# @return the MD.
# -----------------------------------------------------------------------------
def header_ge(md_content, unused_key=None, unused_lang=None):
    md_content.set_include_file("ge.txt")
    md_content.del_include_file("license.txt")
    md_content.set_include_file("license-short.txt")
    return md_content

# -----------------------------------------------------------------------------
# check and change the include file in the header
#
# @return the MD.
# -----------------------------------------------------------------------------
def sanitize_var_ge(md_content, key, lang="fr"):
    key = folder.check_key(key)
    lang = lang.lower()[:2]
    main_title = md_content.title
    main_domain = md_content['domain']
    main_category = key.upper()[:2]

    category = {
        "long": {
            "DQ": "Directive Qualification Professionnelle",
            "DS": "Directive Services",
        },
        "short": {"DQ": "dqp", "DS": "ds"},
        "url-short": {"DQ": "gq", "DS": "ge"},
        "url": {
            "DQ": "www.guichet-qualifications.fr",
            "DS": "www.guichet-entreprises.fr"},
    }

    target_value = {
        "key": key,
        "author": "Guichet Entreprises",
        "lang": lang,
        "category": category["long"][main_category],
        "domain": main_domain,
        "title": main_title,
        "url-name": url_name(main_title),
        "url-domain": category["url"][main_category],
        "url-domain-short": category["url-short"][main_category],
        "category-short": category["short"][main_category],
        "domain-short": short_name(main_domain),
        "title-short": short_name(main_title),
    }

    target_value["url"] = "https://%(url-domain)s/"\
        "%(lang)s/%(category-short)s/" \
        "%(domain-short)s/%(url-name)s.html" % target_value

    for var in target_value:
        if var not in md_content:
            print("Add the key=%s: value=%s  " % (var, target_value[var]))
            md_content[var] = target_value[var]
            continue

        if md_content[var] == target_value[var]:
            continue

        print("Problem with the key=%s: value=%s  " % (var, md_content[var]))
        print("                 --> should be=%s  " % target_value[var])
        md_content[var] = target_value[var]

    return md_content


# -----------------------------------------------------------------------------
# check and change the include file in the header
#
# @return the MD.
# -----------------------------------------------------------------------------
def var_ge(md_content, key, lang="fr"):
    data = ref.get_info_ref(key, lang=lang)
    keys = {
        'key': key,
        'author': "Guichet Entreprises",
        'lang': "%(lang)s" % data,
        'category': "%(category-expand)s" % data,
        'domain': "%(domain)s" % data,
        'title': "%(name)s" % data,
        'url-domain': "%(url-expand-ascii)s" % data,
        'url-domain-short': "%(url)s" % data,
        'category-short': "%(category-filename-short-slug)s" % data,
        'domain-short': "%(domain-filename-short-slug)s" % data,
        'title-short': "%(name-filename-short-slug)s" % data,
        'url': "https://%(url-expand-ascii)s/%(lang)s/"
               "%(category-filename-short-slug)s/"
               "%(domain-filename-short-slug)s/"
               "%(name-filename-short-slug)s.html" % data,
        'last-update': "",
    }

    for the_key in keys:
        if the_key not in md_content:
            print('Add %s=%s in %s' % (the_key, keys[the_key],
                                       md_content.full_filename))
            md_content[the_key] = keys[the_key]

    return md_content


# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_title(md_content, key, lang):
    title = md_content.title
    the_ref = ref.get_info_ref(key, lang=lang)

    if title is None:
        title = "None"
    title = title.upper()
    title = title.strip()
    title = re.sub(
        r"^D?((QP|S)?[ ]*)([0-9][0-9][0-9])[ ]*(-|\.)*[ ]*", "", title)

    target_title = "%(name)s" % the_ref
    if target_title != target_title.strip():
        print(">>> Check the reference file for spaces - %s" % key)
        target_title = target_title.strip()

    if common.str_to_ascii(title.upper()) != \
            common.str_to_ascii(target_title.upper()):
        print("KEY=%6s   IN THE FILE TITLE='%s'" % (key, title))
        print("KEY=%6s   IN THE REF  TITLE='%s'" % (key, target_title.upper()))
        print("filename=%s" % (md_content.full_filename))

    # for var in the_ref:
    #     print("%s=%s" % (var, the_ref[var]))

    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def correct_title(md_content, key, lang):
    title = md_content.title
    target_title = "%(name)s" % ref.get_info_ref(key, lang=lang)

    if title is None:
        title = "None"

    if target_title != target_title.strip():
        print(">>> Check the reference file for spaces - %s" % key)
        target_title = target_title.strip()

    if title != target_title:
        print("KEY=%6s   IN THE FILE TITLE='%s'" % (key, title))
        print("KEY=%6s   IN THE REF  TITLE='%s'" % (key, target_title))
        print("filename=%s" % (md_content.full_filename))
        md_content.title = target_title

    # for var in the_ref:
    #     print("%s=%s" % (var, the_ref[var]))

    return md_content

# -----------------------------------------------------------------------------
# get min max from TOC
# -----------------------------------------------------------------------------
def get_min_max(toc, current=None):
    result = current
    if isinstance(toc, list):
        for item in toc:
            result = get_min_max(item, result)
        return result

    key_level = 'level'
    key_children = 'children'

    if key_level in toc:
        if result is None:
            result = [toc[key_level], toc[key_level]]

        if result[0] > toc[key_level]:
            result[0] = toc[key_level]

        if result[1] < toc[key_level]:
            result[1] = toc[key_level]

    if key_children in toc:
        result = get_min_max(toc[key_children], result)

    return result

# -----------------------------------------------------------------------------
# render to test the TOC
# -----------------------------------------------------------------------------
class CheckToc(mdrender.MdRenderer):

    ###########################################################################
    # Initialisation
    ###########################################################################
    def __init__(self, toc, **kwargs):
        mistune.Renderer.__init__(self, **kwargs)
        self.__toc_stack = [toc]
        min_max = get_min_max(toc)
        self.__min_level = min_max[0]
        self.__max_level = min_max[1]
        print("min %s max %s" % (self.__min_level, self.__max_level))

    ###########################################################################
    # Get the level of header
    # @return the current level
    ###########################################################################
    @property
    def current_element(self):
        if len(self.toc_stack) == 0:
            return None
        if len(self.toc_stack[-1]) == 0:
            return None
        return self.toc_stack[-1][0]

    ###########################################################################
    # Get the level of header
    # @return the current level
    ###########################################################################
    @property
    def toc_stack(self):
        return self.__toc_stack

    ###########################################################################
    # set the new level
    # @param value The value to set
    ###########################################################################
    def next_item(self):
        if self.current_element is None:
            return

        children = self.current_element['children']

        self.toc_stack[-1].pop(0)
        self.__toc_stack.append(children)

        while len(self.toc_stack) > 0 and len(self.toc_stack[-1]) == 0:
            self.__toc_stack.pop()

    ###########################################################################
    # Check the header
    ###########################################################################
    def header(self, text, level, raw=None):
        if level < self.__min_level or \
                self.__max_level < level:
            return super().header(text, level, raw)

        result = "%03d - '%s'" % (level, text)
        print(">>> %s" % result)

        current_el = self.current_element
        if current_el is None:
            print("    No more element")
            return result

        if level != current_el['level']:
            print("    level %03d should be %03d" % (level,
                                                     current_el['level']))

        if text != current_el['name']:
            print("         name '%s'\n"
                  "    should be '%s'" % (text, current_el['name']))

        self.next_item()

        return result

# -----------------------------------------------------------------------------
# render to test the TOC
# -----------------------------------------------------------------------------
class DeleteNum(mdrender.MdRenderer):

    ###########################################################################
    # Check the header
    ###########################################################################
    def header(self, text, level, raw=None):
        (text, unused_) = re.subn(r"(([1-9]\°\.\s+)|([a-z]\.\s+))",
                                  r"", text)
        return super().header(text, level, raw)

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_toc(md_content, unused_key, unused_lang):
    # check_toc_renderer = CheckToc()
    # renderer = mistune.Renderer(use_xhtml=True)
    # use this renderer instance
    start_folder = os.path.split(__get_this_filename())[0]
    content = filetools.get_template_file("ds.md", start_folder=start_folder)
    toc = mdfile.MarkdownContent(content=content).toc

    markdown = mistune.Markdown(renderer=CheckToc(toc))
    markdown(md_content.content)

    # check_toc(str(md_content.content))
    # toc = md_content.toc
    # print(toc)
    # for var in the_ref:
    #     print("%s=%s" % (var, the_ref[var]))

    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def delete_num(md_content, unused_key, unused_lang):
    markdown = mistune.Markdown(renderer=DeleteNum())
    md_content.content = markdown(md_content.content)
    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_num(md_content, unused_key, unused_lang):
    __link_re__ = r"\«\s+(([1-9]\°\.\s+)|([a-z]\.\s+))+" \
        r"(?P<content>[\s\S]*?)\s+\»"

    result = md_content.content
    current_text = result

    # search the var
    match_var = re.search(__link_re__, current_text)

    while match_var is not None:
        ref_link = match_var.group('content')
        print('Find the refence "%s"' % ref_link)

        result += current_text[0:match_var.end(0)]
        current_text = current_text[match_var.end(0):]
        match_var = re.search(__link_re__, current_text)

    return md_content


# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def correct_md(md_content, unused_key, unused_lang):
    md_content.content = normalize.correct_markdown_text(md_content.content)
    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def beautify(md_content, unused_key, unused_lang):
    md_content.beautify()
    # text = md_content.content
    # (text, unused_) = re.subn(r":\n\n", r":\n", text)
    # text = text.rstrip()
    # md_content.content = text
    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def convert_pdf(md_content, unused_key, unused_lang):
    pdf_filename = convert_md_to_pdf(md_content.full_filename)
    logging.info("create %s", pdf_filename)
    return md_content

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def list_missing_files(ref_folder, key_filter, lang=None):
    all_keys = ref.get_info_ref_keys()
    result = []

    pattern = re.compile(key_filter)
    sub_list_keys = []
    for k in all_keys:
        if pattern.search(k) is not None:
            sub_list_keys.append(k)

    for key in sub_list_keys:
        data = ref.get_info_ref(key, lang=lang)
        full_filename = os.path.join(ref_folder, data['path'],
                                     data['filename'])
        if not os.path.isfile(full_filename):
            result.append(common.set_correct_path(full_filename))

    return result


# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def find_key_from_git(key, git_folder, category, domain, name):
    result = {}
    re_path = r"(?P<category>[a-zA-Z0-9-]+)[/|\\]" \
        r"(?P<domain>[a-zA-Z0-9-]+)[/|\\]" \
        r"(?P<key>[A-Z]+[0-9]+)-(?P<name>[a-zA-Z0-9-]+)"
    repo = git.Repo(git_folder)

    result['files'] = []
    result['folder'] = None
    result['path_ref'] = None

    for entrie in repo.index.entries:
        match = re.search(re_path, entrie[0])
        diff = None
        if match:
            diff = match.group('name').upper() != name.upper() or \
                match.group('domain').upper() != domain.upper() or \
                match.group('category').upper() != category.upper()
        if match and diff and match.group('key').upper() == key.upper():
            result['files'].append(entrie)
            this_folder = entrie[0][:match.end('name')]
            this_path_ref = entrie[0][:match.start('category')]

            if result['folder'] is None:
                result['folder'] = this_folder

            if result['folder'] != this_folder:
                logging.info("too many folder '%s' '%s'",
                             result['folder'], this_folder)
                raise Exception("too many folder '%s' '%s'" %
                                (result['folder'], this_folder))

            if result['path_ref'] is None:
                result['path_ref'] = this_path_ref

            if result['path_ref'] != this_path_ref:
                logging.info("too many folder '%s' '%s'",
                             result['path_ref'], this_path_ref)
                raise Exception("too many folder '%s' '%s'" %
                                (result['path_ref'], this_path_ref))

    return result

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_key_name(key, git_folder, ref_folder):
    logging.info("Check the name for %s", key)
    key_data = ref.get_info_ref(key, lang=None)
    logging.info("path=%s", key_data['path'])

    dest = {}
    dest['folder'] = common.set_correct_path(
        os.path.join(ref_folder, key_data['path']))
    common.check_create_folder(dest['folder'])

    re_path = r"(?P<category>[a-zA-Z0-9-]+)[/|\\]" \
        r"(?P<domain>[a-zA-Z0-9-]+)[/|\\]" \
        r"(?P<key>[A-Z]+[0-9]+)-(?P<name>[a-zA-Z0-9-]+)"

    dest_match = re.search(re_path, key_data['path'])

    if not dest_match:
        logging.info("    CAN NOT FIND THE DOMAIN/NAME")
        return

    dest['category'] = dest_match.group('category')
    dest['domain'] = dest_match.group('domain')
    dest['name'] = dest_match.group('name')

    git_entries = find_key_from_git(key, git_folder,
                                    dest['category'],
                                    dest['domain'],
                                    dest['name'])

    if git_entries['folder'] is None:
        logging.info("            --> End")
        return

    logging.info("From '%s' To '%s'", git_entries['folder'], key_data['path'])

    # move git files
    repo = git.Repo(git_folder)
    for entrie in git_entries['files']:
        match = re.search(re_path, entrie[0])
        from_filename = common.set_correct_path(
            os.path.join(repo.working_tree_dir, entrie[0]))
        to_filename = os.path.split(entrie[0])[1].replace(
            match.group('name'), dest['name'])
        to_filename = os.path.join(ref_folder, key_data['path'],
                                   to_filename)
        logging.info("Move from %s ---> %s", from_filename, to_filename)
        result = repo.index.move((from_filename, to_filename))
        # logging.info("Move from %s ---> %s", result[0], result[1])

    # copy other files
    common.copytree(git_entries['folder'], dest['folder'])
    shutil.rmtree(git_entries['folder'])

# -----------------------------------------------------------------------------
# check title
#
# @return the MD.
# -----------------------------------------------------------------------------
def check_all_key_name(git_folder, ref_folder):
    keys = ref.get_info_ref_keys()
    for key in keys:
        check_key_name(key, git_folder, ref_folder)

# -----------------------------------------------------------------------------
# Find the filename of this file (depend on the frozen or not)
# This function return the filename of this script.
# The function is complex for the frozen system
#
# @return the filename of THIS script.
# -----------------------------------------------------------------------------
def __get_this_filename():
    result = ""

    if getattr(sys, 'frozen', False):
        # frozen
        result = sys.executable
    else:
        # unfrozen
        result = __file__

    return result
