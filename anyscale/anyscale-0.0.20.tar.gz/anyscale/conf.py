import os

AWS_PROFILE = None

if "ANYSCALE_HOST" in os.environ:
    ANYSCALE_HOST = os.environ["ANYSCALE_HOST"]
else:
    # The production server.
    # TODO(pcm): This needs to be changed to a more production like URL.
    ANYSCALE_HOST = "34.220.43.10"

APPLICATION_URL = "http://{}:5000".format(ANYSCALE_HOST)

# Global variable that contains the server session token.
CLI_TOKEN = None
