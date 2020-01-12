from logging import config
from swy.config.logging_config import get_log_config
from swy.core.tools.init_tools import create_tmp_dir


TEMPDIR = create_tmp_dir()

# Log level: one of ['DEBUG', 'INFO', 'WARNING', 'ERROR','CRITICAL']
LOGCONFIG = get_log_config(TEMPDIR, all_levels_to='DEBUG')

# Load configuration
config.dictConfig(LOGCONFIG)
