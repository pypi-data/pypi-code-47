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
import shutil
import codecs
import urllib.request
import zipfile
from urllib.parse import urljoin, quote
import requests
import jinja2
import gitlab
import yaml

from pymdtools import common
from pymdtools import mdcommon
from pymdtools import mdfile
from pymdtools import mdtopdf
from pymdtools import translate
import upref

import pygereference
from . import ref


__LIST_FILENAME__ = "_list.md"
__LIST_MENU_FILENAME__ = "_list_menu.md"

# -----------------------------------------------------------------------------
def short_name(name):
    return common.slugify(common.limit_str(name, 30, ' '))

# -----------------------------------------------------------------------------
def jinja_env():
    templates_folder = os.path.join(__get_this_folder(), "templates")
    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(templates_folder),
        autoescape=jinja2.select_autoescape(['html', 'xml']))

    template_env.filters['short_name'] = short_name
    return template_env

# -----------------------------------------------------------------------------
def _build_folder(destination_folder, refs, ref_id, generate_pdf=False):
    logging.info("build folder %s", destination_folder)
    destination_folder = common.check_create_folder(destination_folder)
    context = {'links_id': 'reference-%s' % ref_id, 'links': []}

    for name in refs:
        if 'key' in refs[name] and name == refs[name]['key']:
            title_short = short_name(refs[name]['title'])
            dest_filename = os.path.join(
                destination_folder, title_short + ".md")
            shutil.copy(refs[name]['filename'], dest_filename)
            if generate_pdf:
                mdtopdf.convert_md_to_pdf(dest_filename)
            context['links'].append({
                'name': refs[name]['title'],
                'url': "./" + title_short + ".md",
                'menu_link': "./" + title_short + ".md",
                'title': refs[name]['title'],
            })
        else:
            name_short = short_name(name)
            target = os.path.join(destination_folder, name_short)
            _build_folder(target, refs[name], ref_id + "-" + name_short)
            context['links'].append({
                'name': name,
                'url': "./" + name_short + "/_index.md",
                'name_short': name_short,
                'menu_include': "./%s/%s"%(name_short,
                                           __LIST_MENU_FILENAME__),
                'title': name,
            })

    content = jinja_env().get_template(__LIST_FILENAME__ + ".j2")\
                         .render(context)
    output_filename = os.path.join(destination_folder, __LIST_FILENAME__)
    logging.debug("Write the file %s", output_filename)
    common.set_file_content(output_filename, content)

    content = jinja_env().get_template(__LIST_MENU_FILENAME__ + ".j2")\
                         .render(context)
    output_filename = os.path.join(destination_folder, __LIST_MENU_FILENAME__)
    logging.debug("Write the file %s", output_filename)
    common.set_file_content(output_filename, content)

# -----------------------------------------------------------------------------
def _build_list(destination_folder, refs, ref_id):
    logging.info("build automated list in folder %s", destination_folder)
    destination_folder = common.check_create_folder(destination_folder)
    context = {'links_id': 'reference-%s' % ref_id, 'links': []}

    for name in refs:
        if 'key' in refs[name] and name == refs[name]['key']:
            context['links'].append({'title': refs[name]['title']})
        else:
            _build_list(destination_folder,
                        refs[name], ref_id + "-" + short_name(name))
            context['links'].append({'title': name})

    content = jinja_env().get_template(__LIST_FILENAME__ + ".j2")\
                         .render(context)
    output_filename = os.path.join(destination_folder,
                                   "list-%s.md" % ref_id)
    logging.debug("Write the file %s", output_filename)
    common.set_file_content(output_filename, content)

# -----------------------------------------------------------------------------
def build_automated_list(destination_folder):
    for lang in translate.eu_lang_list():
        logging.info("Build automated list for lang=%s", lang)
        refs = ref.get_ref_organised(lang=lang,
                                     keys_order=['category', 'domain'])
        if len(refs) == 0:
            continue
        _build_list(destination_folder, refs, lang)

# -----------------------------------------------------------------------------
def write_preformat_description(destination_folder, context, ref_id,
                                filename=None, **kwargs):
    if filename is None:
        filename = "description-%s.md" % ref_id
    output_filename = os.path.join(destination_folder, filename)
    if os.path.isfile(output_filename):
        return
    content = jinja_env().get_template("description.md.j2").render(context)
    logging.debug("Write the file %s", output_filename)
    common.set_file_content(output_filename, content)

    mdown = mdfile.MarkdownContent(output_filename, backup=False, **kwargs)
    mdown.process_tags()
    mdown.write()

    return output_filename

# -----------------------------------------------------------------------------
def build_preformat_description(destination_folder):
    for lang in translate.eu_lang_list():
        logging.info("Build preformat menu for lang=%s", lang)
        refs = ref.get_ref_organised(lang=lang,
                                     keys_order=['category', 'domain'])
        if len(refs) == 0:
            continue

        for category in refs:
            ref_id = "%s-%s" % (lang, short_name(category))
            context = {
                "links_id": "reference-%s" % ref_id,
                "lang": lang,
                "category": category,
                "title": category
            }
            write_preformat_description(destination_folder, context, ref_id)
            for domain in refs[category]:
                ref_id_domain = ref_id + "-" + short_name(domain)
                context['domain'] = domain
                context['title'] = domain
                context['links_id'] = "reference-%s" % ref_id_domain
                write_preformat_description(
                    destination_folder, context, ref_id_domain)


# -----------------------------------------------------------------------------
# Get title in md text
# @param title the title of markdown text
# @param lang the language
# @return the corrected text
# -----------------------------------------------------------------------------
def context_files(destination_folder):
    licence = os.path.join(__get_this_folder(), "..", "LICENSE.md")
    shutil.copyfile(licence, os.path.join(destination_folder, "LICENSE.md"))

    files = {}
    for lang in translate.eu_lang_list():
        refs = ref.get_ref_organised(lang=lang,
                                     keys_order=['category', 'domain'])
        if len(refs) != 0:
            files[lang] = refs

    context = {
        "version": pygereference.__version_info__,
        "package_name": pygereference.__package_name__,
        "today": common.get_today(),
        "langs": translate.eu_lang_list(),
        "files": files,
    }

    for name in ["readme.md", "configuration.yml"]:
        content = jinja_env().get_template(name + ".j2").render(context)
        output_filename = os.path.join(destination_folder, name)
        logging.debug("Write the file %s", output_filename)
        common.set_file_content(output_filename, content)


# -----------------------------------------------------------------------------
# Get title in md text
# -----------------------------------------------------------------------------
def build_description(destination_folder, **kwargs):
    # existing files
    descriptions = ref.list_description_files()
    for filename in descriptions:
        mdown = mdfile.MarkdownContent(filename, **kwargs)
        mdown.filename = "list.md"
        lang = mdown['lang']
        category = mdown['category']
        domain = mdown['domain'] if 'domain' in mdown else ''
        mdown.filename = "_index.md"
        mdown.filename_path = \
            os.path.join(destination_folder, lang,
                         short_name(category), short_name(domain))
        mdown.backup=False
        mdown.process_tags()
        mdown.write()

    # Create other
    for lang in translate.eu_lang_list():
        logging.info("Build preformat index for lang=%s", lang)
        refs = ref.get_ref_organised(lang=lang,
                                     keys_order=['category', 'domain'])
        if len(refs) == 0:
            continue

        for category in refs:
            ref_id = "%s-%s" % (lang, short_name(category))
            context = {
                "links_id": "reference-%s" % ref_id,
                "lang": lang,
                "category": category,
                "title": category
            }
            dest_path = os.path.join(destination_folder, lang,
                                     short_name(category))
            write_preformat_description(dest_path, context, ref_id,
                                        filename="_index.md", **kwargs)
            for domain in refs[category]:
                ref_id_domain = ref_id + "-" + short_name(domain)
                context['domain'] = domain
                context['title'] = domain
                context['links_id'] = "reference-%s" % ref_id_domain
                dest_path = os.path.join(destination_folder, lang,
                                         short_name(category),
                                         short_name(domain))
                write_preformat_description(
                    dest_path, context, ref_id_domain,
                    filename="_index.md", **kwargs)


# -----------------------------------------------------------------------------
# Get title in md text
# @param title the title of markdown text
# @param lang the language
# @return the corrected text
# -----------------------------------------------------------------------------
def build(destination_folder, generate_pdf=False, **kwargs):
    for lang in translate.eu_lang_list():
        logging.info("Build for lang=%s", lang)
        refs = ref.get_ref_organised(lang=lang,
                                     keys_order=['category', 'domain'])
        if len(refs) == 0:
            continue
        _build_folder(os.path.join(destination_folder, lang), refs, lang,
                      generate_pdf=generate_pdf)

    build_description(destination_folder, **kwargs)
    context_files(destination_folder)

# -----------------------------------------------------------------------------
# Get title in md text
# @param title the title of markdown text
# @param lang the language
# @return the corrected text
# -----------------------------------------------------------------------------
def create(release_path, package_name="reference", build_path=None,
           version=None, generate_pdf=False):
    if build_path is None:
        build_path = release_path
    if version is None:
        version = pygereference.__version_info__

    build(os.path.join(build_path, package_name), generate_pdf=generate_pdf)

    release_filenanme = os.path.join(
        release_path, "%s-v%s.zip" % (package_name, version))

    create_zip(release_filenanme, [package_name], build_path)

    return release_filenanme

# -----------------------------------------------------------------------------
def create_zip(zipfilename, files_or_folder_list, root_path):
    """
    Create a zip file with all file and folders
    Arguments:
        zipfilename {str} -- the zip filename destination
        files_or_folder_list {list} -- all files or folders
    """
    zipfilename = common.set_correct_path(zipfilename)
    logging.info("Create the zip file %s", zipfilename)

    def add_file(filename, ziph, root_path):
        logging.debug("Add the file %s", filename)
        ziph.write(os.path.join(root_path, filename), filename)

    def add_dir(path, ziph, root_path):
        path = os.path.join(root_path, path)
        for root, unused_dirs, files in os.walk(path):
            for file in files:
                filename = os.path.join(root, file)
                rel_filename = os.path.relpath(filename, root_path)
                add_file(rel_filename, ziph, root_path)

    with zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for fname in files_or_folder_list:
            complet_fname = os.path.join(root_path, fname)
            if os.path.isdir(complet_fname):
                add_dir(fname, zipf, root_path)
            else:
                add_file(fname, zipf, root_path)

    return zipfilename

# -----------------------------------------------------------------------------
def gitlab_upload(filenames):
    if not isinstance(filenames, list):
        filenames = [filenames]

    data_conf = upref.load_conf(os.path.join(__get_this_folder(),
                                             "templates", "gitlab.conf"))
    data_conf["server"]["value"] = pygereference.__gitlab_url__
    data_conf["project_id"]["value"] = pygereference.__gitlab_project_id__
    user_data = upref.get_pref(
        data_conf, "gitlab-" + pygereference.__module_name__)

    api_url = urljoin(user_data['server'] + "/",
                      "/api/v4/projects/%s/" % user_data['project_id'])
    auth = {'PRIVATE-TOKEN': user_data['private_token']}
    uploads = []
    verify = True  # Ignore ssl certificate failures

    logging.info("Uploading %s", filenames)

    for filename in filenames:
        with codecs.open(filename, 'rb') as filehandle:
            rsp = requests.post(urljoin(api_url, 'uploads'),
                                files={'file': filehandle},
                                headers=auth, verify=verify)
            try:
                rsp.raise_for_status()
                logging.info("Upload of %s", filename)
            except BaseException as ex:
                logging.info("Upload of %s failed: %s", filename, ex)
            else:
                uploads.append(rsp.json())

    return uploads

# -----------------------------------------------------------------------------
def release_description(uploads):
    context = {
        "uploads": uploads,
        "version": pygereference.__version_info__,
        "today": common.get_today(),
    }

    template = jinja_env().get_template("release_description.md.j2")

    return template.render(context)

# -----------------------------------------------------------------------------
def gitlab_description_upload(description, release_tag):
    data_conf = upref.load_conf(os.path.join(__get_this_folder(),
                                             "templates", "gitlab.conf"))
    data_conf["server"]["value"] = pygereference.__gitlab_url__
    data_conf["project_id"]["value"] = pygereference.__gitlab_project_id__
    user_data = upref.get_pref(
        data_conf, "gitlab-" + pygereference.__module_name__)

    api_url = urljoin(user_data['server'] + "/",
                      "/api/v4/projects/%s/" % user_data['project_id'])
    auth = {'PRIVATE-TOKEN': user_data['private_token']}
    verify = True  # Ignore ssl certificate failures

    # Now we've got the uploaded file info, attach that to the tag
    url = urljoin(
        api_url, 'repository/tags/{t}'.format(t=quote(release_tag, safe='')))
    tag_details = requests.get(url, headers=auth, verify=verify).json()

    if 'name' not in tag_details:
        logging.error("The tag '%s' is not define.", release_tag)
        raise BaseException("The tag '%s' is not define." % release_tag)

    if 'release' in tag_details and tag_details['release'] is not None:
        logging.error("The release '%s' is already done.", release_tag)
        raise BaseException("The release '%s' is already done." % release_tag)

    rsp = requests.post(url + '/release',
                        data={'description': description},
                        headers=auth, verify=verify)

    try:
        rsp.raise_for_status()
        logging.info("Description uploaded to tag %s", release_tag)

    except BaseException as ex:
        logging.info("Setting tag description failed: "
                     "\"%s\" error: %s", description, ex)

    return release_tag

# -----------------------------------------------------------------------------
def gitlab_make_release(build_folder, dist_folder):
    release_tag = "v" + pygereference.__version__

    if release_tag not in gitlab_get_tags():
        logging.error("The tag %s is not define", release_tag)
        raise BaseException("The tag %s is not define" % release_tag)

    release_filename = "%s-%s.zip" % (
        pygereference.__package_name__, release_tag)

    build(os.path.join(build_folder, pygereference.__package_name__))
    zipfilename = create_zip(os.path.join(dist_folder, release_filename),
                             [pygereference.__package_name__],
                             build_folder)

    uploads = gitlab_upload(zipfilename)
    description = release_description(uploads)
    gitlab_description_upload(description, release_tag)

# -----------------------------------------------------------------------------
def gitlab_proj_anonymous():
    return gitlab.Gitlab(pygereference.__gitlab_url__)\
                 .projects.get(pygereference.__gitlab_project_id__)

# -----------------------------------------------------------------------------
def gitlab_get_tags():
    project = gitlab_proj_anonymous()
    return [tag.name for tag in project.tags.list()]

# -----------------------------------------------------------------------------
def gitlab_get_releases():
    project = gitlab_proj_anonymous()
    return [tag.tag_name for tag in project.releases.list()]

# -----------------------------------------------------------------------------
def gitlab_get_latest_release():
    releases = gitlab_get_releases().sort()
    return releases[-1] if len(releases) > 0 else None

# -----------------------------------------------------------------------------
def get(destination_folder, name, version=None):
    """ Get the template from gitlab and update template.

    @return the configuration fielname
    """
    logging.info("Get the reference release name=%s version=%s",
                 name, version or "latest")
    project_id = pygereference.__gitlab_project_id__
    server = pygereference.__gitlab_url__
    conf_filename = 'reference/configuration.yml'

    destination_folder = common.check_create_folder(destination_folder)
    conf_filename = os.path.join(destination_folder, conf_filename)

    if version is not None and version.lower() == "local":
        return conf_filename

    if version is None or version.lower() == "latest":
        project = gitlab.Gitlab(server).projects.get(project_id)
        release_tag = [release.tag_name for release in project.releases.list()]
        release_tag.sort()
        version = release_tag[-1]
        version = version.replace("v", "")
        logging.info("The latest release is %s", version)

    if os.path.isfile(conf_filename):
        with codecs.open(conf_filename, "r", "utf-8") as ymlfile:
            conf = yaml.load(ymlfile, Loader=yaml.FullLoader)
        current_version = conf['version']
        current_package = None
        if 'package_name' in conf:
            current_package = conf['package_name']
        logging.info('Current_version is %s', current_version)
        logging.info('Current_package_name is %s', current_package)
        if current_version == version and current_package == name:
            logging.info('Already have it')
            return conf_filename

    logging.info('Go for a download')
    project = gitlab.Gitlab(server).projects.get(project_id)
    description_md = project.releases.get("v" + version).description
    links = mdcommon.search_link_in_md_text(description_md)

    url = None
    for link in links:
        if link['name'].startswith(name):
            url = link['url']
    if url is None:
        logging.warning('Cannont find the version %s of %s', version, name)
        raise Exception('Cannont find the version %s of %s' % (version, name))
    url = project.web_url + url

    if os.path.isdir(destination_folder):
        logging.info('Clean folder %s', destination_folder)
        shutil.rmtree(destination_folder)
        common.check_create_folder(destination_folder)

    dest_filename = os.path.join(
        destination_folder, name + "-" + release_tag[-1] + ".zip")
    logging.info('Download %s --> %s', url, dest_filename)
    urllib.request.urlretrieve(url, dest_filename)

    logging.info('Extract %s', dest_filename)
    with zipfile.ZipFile(dest_filename, 'r') as zip_obj:
        zip_obj.extractall(destination_folder)

    return conf_filename


# -----------------------------------------------------------------------------
def create_merge_request():
    data_conf = upref.load_conf(os.path.join(__get_this_folder(),
                                             "templates", "gitlab.conf"))
    data_conf["server"]["value"] = pygereference.__gitlab_url__
    data_conf["project_id"]["value"] = pygereference.__gitlab_project_id__
    user_data = upref.get_pref(
        data_conf, "gitlab-" + pygereference.__module_name__)

    server = user_data['server']
    project_id = user_data['project_id']
    private_token = user_data['private_token']

    gitl = gitlab.Gitlab(server, private_token=private_token)
    project = gitl.projects.get(project_id)

    git_mr = project.mergerequests.create({
        'source_branch': 'develop',
        'target_branch': 'master',
        'title': 'New version to test',
    })

    git_mr.merge()


# -----------------------------------------------------------------------------
def __get_this_folder():
    """ Return the folder of this script with frozen compatibility
    @return the folder of THIS script.
    """
    return os.path.split(os.path.abspath(os.path.realpath(
        __get_this_filename())))[0]

# -----------------------------------------------------------------------------
def __get_this_filename():
    """ Return the filename of this script with frozen compatibility
    @return the filename of THIS script.
    """
    return __file__ if not getattr(sys, 'frozen', False) else sys.executable
