from watched_schema import validators

from flask import Blueprint

from .cache import get_cache


def hard_copy(obj):
    if isinstance(obj, (set, list, tuple)):
        return list(map(hard_copy, obj))
    if isinstance(obj, dict):
        return {key: hard_copy(value) for key, value in obj.items()}
    return obj


class BasicAddon(object):
    # Some items which can be used for automatic tests (see test.py)
    test_items = None

    addon_type = None
    addon_actions = ['addon']

    props = None

    def __init__(self, props=None):
        if props is not None:
            if self.props is not None:
                raise ValueError(
                    'Define either props in constructor, ' +
                    'or on class. Please check our documentation ' +
                    'for more infos.')
        else:
            props = self.props
        if not props:
            raise ValueError(
                'You forgot to define addon props. Please check ' +
                'our documentation for more infos.')

        props['type'] = self.addon_type
        self.props = validators['models']['addon'](props)

    def __getitem__(self, key):
        return self.props[key]

    @property
    def id(self):
        return self.props["id"]

    @property
    def type(self):
        return self.props["type"]

    def get_cache(self, key):
        return get_cache().get([self.id, key])

    def set_cache(self, key, value, ttl=24 * 3600):
        return get_cache().set([self.id, key], value, ttl)

    def delete_cache(self, key):
        return get_cache().delete([self.id, key])

    def addon(self, ctx, **kwargs):
        """This function returns the addon specification.
        Normally this function doesn't need any modifications,
        but it can be overwritten to handle for example
        translations or resource infos which will be loaded
        on demand.
        """
        return hard_copy(self.props)


class RepositoryAddon(BasicAddon):
    """A repository addon is basically a colleciton of
    local as well as remote addons.
    See the `add_addon` and `add_url` functions for more
    infos.
    For more infos, see `RepositoryAddon`.
    """
    addon_type = "repository"
    addon_actions = ['addon', 'repository']

    def __init__(self, props=None):
        super(RepositoryAddon, self).__init__(props)
        self.addons = []
        self.urls = []

    def add_addon(self, addon):
        """Add a addon object to this repository.
        """
        self.addons.append(addon)

    def add_url(self, url):
        """Add a URL of a remote addon to this repository.
        The properties of the addons will be loaded in
        intervals to keep the informations updated.
        """
        self.urls.append(url)

    def repository(self, ctx, **kwargs):
        """Returns all addons this repository knows.
        """
        result = []
        kwargs['index'] = True
        for addon in self.addons:
            url = './' if addon.addon_is_root_addon else f'./{addon.id}'
            props = addon.addon(ctx, **kwargs)
            props['metadata'] = {'url': url}
            result.append(props)
        for url in self.urls:
            # TODO: Load props from remote repo via a POST /addon call
            raise NotImplementedError()
        return result


class WorkerAddon(BasicAddon):
    """A worker addon is there to get some work done ;)
    It can:
    - List directories (return a list of items)
    - Get detailed infos about an item
    - Get sources and subtitles
    - Resolve URL's
    For more infos, see `WorkerAddon`.
    """
    addon_type = "worker"
    addon_actions = ['addon', 'directory',
                     'item', 'source', 'subtitle', 'resolve']

    def directory(self, ctx, **kwargs):
        """This function returns a "directory" of items.
        See `ApiDirectoryRequest` and `ApiDirectoryResponse`.
        """
        raise NotImplementedError()

    def item(self, ctx, **kwargs):
        """This function returns a detailed infos about an `item`.
        See `ApiItemRequest` and `ApiItemResponse`.
        """
        raise NotImplementedError()

    def source(self, ctx, **kwargs):
        """This function returns sources for an item. A source
        is something where this item can be obtained, for example
        an external URL, or a link to a direct stream.
        See `ApiSourceRequest` and `ApiSourceResponse`.
        """
        raise NotImplementedError()

    def subtitle(self, ctx, **kwargs):
        """This function returns subtitles for an item.
        See `ApiSubtitleRequest` and `ApiSubtitleResponse`.
        """
        raise NotImplementedError()

    def resolve(self, ctx, **kwargs):
        """This function resolved an URL, so it can be
        played inside the app.
        See `ApiSourceRequest` and `ApiSourceResponse`.
        """
        raise NotImplementedError()


class IptvAddon(BasicAddon):
    """An IPTV addon doesn't have much functionality
    except telling it's name and an URL to the playlist.
    For more infos, see `IptvAddon`.
    """
    addon_type = "iptv"


class BundleAddon(BasicAddon):
    """A bundle addon is like a "installation script" for
    our app. On the field `requirements` you can define
    addons which should be installed.
    For more features and infos, see `BundleAddon`.
    """
    addon_type = "bundle"
