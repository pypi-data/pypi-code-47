import pkg_resources

__version__ = (
  pkg_resources
  .get_distribution('utensor_cgen')
  .version
)
