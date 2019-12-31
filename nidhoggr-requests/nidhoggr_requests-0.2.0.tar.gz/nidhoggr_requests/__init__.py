from pkg_resources import get_distribution, DistributionNotFound
import os.path

try:
    _dist = get_distribution('nidhogg_requests')
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'nidhogg_requests')):
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version
