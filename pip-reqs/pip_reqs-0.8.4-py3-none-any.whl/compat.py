from distutils.version import StrictVersion as V

from pip import __version__
from pip._internal.index import PackageFinder


PIP_VERSION = V(__version__)


if PIP_VERSION >= V("19.3"):

    def is_dir_url(link):
        return link.is_existing_dir()

    def is_file_url(link):
        return link.is_file

    def is_vcs_url(link):
        return link.is_vcs


else:
    from pip._internal.download import (  # NOQA
        is_dir_url,
        is_file_url,
        is_vcs_url,
    )


def get_dist_from_abstract_dist(abstract_dist, finder):
    if PIP_VERSION >= V("19.2"):
        return abstract_dist.get_pkg_resources_distribution()
    elif PIP_VERSION >= V("19.0"):
        return abstract_dist.dist()
    else:
        return abstract_dist.dist(finder)


def get_package_finder(session):
    if PIP_VERSION >= V("19.2"):
        from pip._internal.models.search_scope import SearchScope
        from pip._internal.models.selection_prefs import SelectionPreferences

        search_scope = SearchScope.create(find_links=[], index_urls=[])

        if PIP_VERSION >= V("19.3"):
            from pip._internal.collector import LinkCollector

            kwargs = {
                "link_collector": LinkCollector(
                    session=session, search_scope=search_scope
                )
            }
        else:
            kwargs = {
                "search_scope": search_scope,
                "session": session,
            }

        return PackageFinder.create(
            selection_prefs=SelectionPreferences(allow_yanked=False), **kwargs
        )
    else:
        return PackageFinder(find_links=[], index_urls=[], session=session)
