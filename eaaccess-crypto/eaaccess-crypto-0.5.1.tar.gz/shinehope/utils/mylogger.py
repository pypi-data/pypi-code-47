import logging
import logging.config
import os
import shinehope.eaaccess.settings  as settings
from shinehope.utils.definitions import EAACCESS_DIR

# # 读取日志配置文件内容
# if settings.__logFile:
#      logFile = settings.__logFile
# else:
#      logFile = './logs/EAAccess.log'
# logging.config.fileConfig('./configs/logging.conf', defaults={'logfilename': logFile})

if settings.__logFile is not None:
    logFile = settings.__logFile
else:
    logFile = os.path.join(EAACCESS_DIR, 'logs', 'EAAccess.log')

if settings.__logEAFile is not None:
    eaLogFile = settings.__logEAFile
else:
    eaLogFile = os.path.join(EAACCESS_DIR, 'strategy', 'logs', 'EAAccess.log')

if settings.appMode == "BACKTEST":
    confFile = os.path.join(EAACCESS_DIR, 'configs', 'log_backtest.conf')
    ## appLog
    logging.config.fileConfig(confFile, defaults={'logfilename': logFile, 'ealogfile': eaLogFile})
    # # 创建一个日志器logger
    # logger = logging.getLogger('root')
# if settings.appMode == "BACKTEST":
    appLog = logging.getLogger(name="backtestLogger")
    eaLog = logging.getLogger(name="eaBackTestLogger")
    # eaLog = appLog
else:
    confFile = os.path.join(EAACCESS_DIR, 'configs', 'logging.conf')
    ## appLog
    logging.config.fileConfig(confFile, defaults={'logfilename': logFile, 'ealogfile': eaLogFile})
    appLog = logging.getLogger(name="rotatingFileLogger")
    eaLog = logging.getLogger(name="eaFileLogger")

# appLog = logging.getLogger(name="backtestFileLogger")
# appLog = logging.getLogger(name="rotatingFileLogger")

# ## eaLog
# logging.config.fileConfig(confFile, defaults={'logfilename': eaLogFile})
# # # 创建一个日志器logger
# # logger = logging.getLogger('root')
# if settings.appMode == "BACKTEST":
#      eaLog = logging.getLogger(name="backtestLogger")
# else:
#      eaLog = logging.getLogger(name="rotatingFileLogger")

