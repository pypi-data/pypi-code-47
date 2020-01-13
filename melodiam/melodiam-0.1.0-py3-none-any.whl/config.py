from starlette.config import Config
from starlette.datastructures import URL, Secret

CONFIG = Config(env_file=".env.api")

TESTING = CONFIG("TESTING", cast=bool)
