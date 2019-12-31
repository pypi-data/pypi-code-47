from shinehope.utils.definitions import EAACCESS_DIR
import shinehope.eaaccess.settings as settings
import  time
import  sys, os, getopt
import multiprocessing as mp


def getCommandArgs(accID) -> {}:
    # global  initForce, confFile, accID

    argv = sys.argv[1:]
    initForce = False
    confFile = os.path.join(EAACCESS_DIR, 'configs', 'config.toml')

    try:
        opts, args = getopt.getopt(argv,"hc:",["init","conf=", "id="])
    except getopt.GetoptError:
        print("")
        print("Use -h option go get help !")
        print("eacrypto.py -h")
        sys.exit(2)
        # retStatus = 2
    for opt, arg in opts:
        if opt == "-h":
            print("")
            print("eacrypto.py -h --init -c <conf.toml> --id <id>")
            print("")
            print("-h                 : this help text")
            print("--init             : will re-init local Candles (remove local cache, and re-fetch candles; be careful)")
            print("-c <conf.toml>")
            print("--conf <conf.toml> : use self-defined config file, <conf.toml> is toml format")
            print("--id <id>          : specify account id <id>")
            print("")
            sys.exit(0)
            # retStatus = 0
        elif opt == "--init":
            initForce = True
        elif opt in {"-c", "--conf"}:
            confFile = f"./{arg}"
        elif opt == "--id":
            accID = f"{arg}"
        else:
            print("eacrypto.py -h")
            sys.exit(2)   
            # retStatus = 2

    commands = {}
    commands['account'] = accID
    commands['init'] = initForce
    commands['confFile'] = confFile

    return commands     

def eatrade(accID):
    name = mp.current_process().name

    settings.__logFile = os.path.join(EAACCESS_DIR, 'logs', f"{name}.log")
    settings.__logEAFile = os.path.join(EAACCESS_DIR, 'strategy', 'logs', f"{name}.log")

    startMsg = f"{name} Starting"
    print(startMsg)
    # print('\n'.join(sys.path))

    runConfs = getCommandArgs(accID)

    initForce = runConfs['init']
    accID = runConfs['account']
    confFile = runConfs['confFile']

    import toml
    # configs = toml.load('./configs/backtest.toml')
    if not os.path.exists(confFile):
        print("")
        print(f"File not existed...({confFile})")
        sys.exit(1)
    print(f"--- using config file: {confFile} id: {accID}\n")
    configs = toml.load(confFile)

    minerFile = os.path.join(EAACCESS_DIR, 'configs', 'MinerConfig.toml')
    minerConf = toml.load(minerFile)

    if accID not in minerConf['ExpertAdvisor']:
        print("")
        print(f"[ExpertAdvisor.{accID}] not found in {minerFile} !!!")
        sys.exit(1)


    settings.appMode = "TRADE"
    settings.exchangeName = minerConf['Worker']['exchangeName'].strip()
    settings.wssEndPoint = minerConf['Worker']['apiWSSPoint']
    apiKey =  minerConf['Worker']['apiKey']
    apiSecret =  minerConf['Worker']['apiSecret']
    settings.apiKey = apiKey
    settings.apiSecret = apiSecret

    from shinehope.eaminer.EAInfo import EAInfo
    from shinehope.eaminer.MinerTalk import MinerTalk
    # from shinehope.eaaccess.dataaccess.sqlite import DBAccess
    from shinehope.utils.mylogger import appLog
    appLog.warning(startMsg)

    expertName = "strategy_client"
    if configs['tradingAdvisor']['expert']:
        expertName = configs['tradingAdvisor']['expert']
        tomlFileName = f"{expertName}.toml"
        tomlFilePath = os.path.join(EAACCESS_DIR, 'strategy', 'configs', tomlFileName)
        if os.path.isfile(tomlFilePath):
            strategyConfs = toml.load(tomlFilePath)
            settings.settings = strategyConfs
        else:
            appLog.warning(f"Expert config file {tomlFilePath} not existed !")

    # if __name__ == '__main__':
    print("Enter...", __name__)

    # if not settings.appMode not in {'LIVE', 'DEMO'}:
    if minerConf['ExpertAdvisor'][accID]['tradeMode'] not in {'LIVE', 'DEMO'}:
        appLog.warning("only support tradeMode('LIVE', 'DEMO')...")
        sys.exit(0)

    if settings.appMode == "TRADE":     # including Paper Trading and Live Trading
        settings._configs = configs
        settings._initForce = initForce

    # import strategy.experts.strategy_client as EAAccessStrategy
    import importlib.util
    # if os.path.isdir('./eacrypto/strategy/'):
    strategyDir = os.path.join(EAACCESS_DIR, 'strategy', 'experts')
    if os.path.isdir(strategyDir):
        # strategyFilePath = os.path.join(strategyDir, 'strategy_client.py')
        strategyName = expertName + ".py"
        strategyFilePath = os.path.join(strategyDir, strategyName)
        if os.path.isfile(strategyFilePath):
            MODULE_PATH = strategyFilePath
        else:
            # strategyFilePath = os.path.join(strategyDir, 'strategy_client.pyc')
            strategyName = expertName + ".pyc"
            strategyFilePath = os.path.join(strategyDir, strategyName)
            if os.path.isfile(strategyFilePath):
                MODULE_PATH = strategyFilePath
            else:
                print("Strategy File not existed !!!")
                exit(1)

        print(f'Importing external ({MODULE_PATH}) as EAAccessStrategy')
        MODULE_NAME = "EAAccessStrategy"

        spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
        print("spec.name is " + str(spec.name))
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module 
        # print(sys.modules)
        spec.loader.exec_module(module)
        # print(sys.modules)


        # strategy_client = module
        EAAccessStrategy = module
        # print(strategy_client.__version__)
    else:
        # print('Importing internal(eacrypto.strategy.strategy_client) as EAAccessStrategy')
        print('Importing internal(strategy.experts.strategy_client) as EAAccessStrategy')
        import shinehope.strategy.experts.strategy_client as EAAccessStrategy

    ea = EAAccessStrategy.StrategyClient('V00.05.01')
    ea.aiboxConnect(settings.exchangeName, apiKey, apiSecret, accID)

    while True:
        try:
            time.sleep(5)
            eaInfo = MinerTalk.get(accID)
            if eaInfo is None:
                appLog.info(f"App Running....initializing")
            else:
                appLog.info(f"App Running...{eaInfo.account}#  {eaInfo.lots_opentrade}  {eaInfo.lots_today}  {eaInfo.timestamp}")
        except KeyboardInterrupt:
            print()
            print('Got Ctrl+C(Interrupt)...')
            print('disposing ...')
            ea.dispose()
            break

    sys.exit(0)

