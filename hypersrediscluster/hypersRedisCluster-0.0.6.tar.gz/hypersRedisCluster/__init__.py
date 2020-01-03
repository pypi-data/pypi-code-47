__version__ = "0.0.6"

# import redis
# import warnings
#
#
# def check_redis(version):
#     try:
#         redis_version = list(map(int, version.split(".")))
#     except ValueError:
#         return
#     major, minor, patch = redis_version
#     assert major == 3
#     assert minor >= 0
#     assert minor <= 4
#
#
# try:
#     redis_version = redis.__version__
#     check_redis(redis_version)
# except (AssertionError, ValueError):
#     warnings.warn(
#         f"redis({redis_version}) doesn't match a supported redis-py-cluster supports redis-py>=3.0.0,<3.4.0."
#     )
