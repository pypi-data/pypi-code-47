from shinehope.utils.definitions import EAACCESS_DIR
import shinehope.eaaccess.settings as settings
import  time
import  sys, os, getopt
from datetime import datetime, timedelta
import multiprocessing as mp


def getCommandArgs(accID) -> {}:
    # global  initForce, confFile, accID

    argv = sys.argv[1:]
    initForce = False
    confFile = os.path.join(EAACCESS_DIR, 'configs', 'backtest.toml')

    try:
        opts, args = getopt.getopt(argv,"hc:",["init","conf=", "id="])
    except getopt.GetoptError:
        print("")
        print("Use -h option go get help !")
        print("eabacktest.py -h")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("")
            print("eabacktest.py -h --init -c <conf.toml>")
            print("")
            print("-h                 : this help text")
            print("--init             : will re-init local Candles (remove local cache, and re-fetch candles; be careful)")
            print("-c <conf.toml>")
            print("--conf <conf.toml> : use self-defined config file, <conf.toml> is toml format")
            print("--id <id>          : specify account id <id>")
            print("")
            sys.exit(0)
        elif opt == "--init":
            initForce = True
        elif opt in {"-c", "--conf"}:
            confFile = f"./{arg}"
        elif opt == "--id":
            accID = f"{arg}"
        else:
            print("eabacktest.py -h")
            sys.exit(2)

    commands = {}
    commands['account'] = accID
    commands['init'] = initForce
    commands['confFile'] = confFile

    return commands       

def eabacktest(accID):
    name = "BackTest"
    settings.__logFile = os.path.join(EAACCESS_DIR, 'logs', f"{name}.log")
    settings.__logEAFile = os.path.join(EAACCESS_DIR, 'strategy', 'logs', f"{name}.log")
    # from utils.mylogger import appLog

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

    settings._ConfFile = confFile
    # settings.candleSize = configs['market']['candleSize'].strip()
    minerConf = configs['MinerConfig']
    if accID not in minerConf['ExpertAdvisor']:
        print("")
        print(f"[MinerConfig.ExpertAdvisor.{accID}] not found in {confFile} !!!")
        sys.exit(1)    
    accConf = minerConf['ExpertAdvisor'][accID]
    tradeSymbol = accConf['CurrAVL']
    pos = tradeSymbol.find("/")
    currAsset = tradeSymbol[:pos]
    currQuote = tradeSymbol[pos + 1:]
    settings.symbol = f"{currAsset}/{currQuote}"
    # settings.appMode = accConf['tradeMode']
    settings.appMode = "BACKTEST"
    # settings.accountID = accID
    settings.exchangeName = minerConf['Worker']['exchangeName'].strip()
    settings.wssEndPoint = minerConf['Worker']['apiWSSPoint']
    apiKey =  minerConf['Worker']['apiKey']
    apiSecret =  minerConf['Worker']['apiSecret']
    settings.apiKey = apiKey
    settings.apiSecret = apiSecret
    settings._axhline = configs['backtest']['cursorAxHLine']

    expertName = "strategy_client"
    if configs['tradingAdvisor']['expert']:
        expertName = configs['tradingAdvisor']['expert']
        settings.settings = configs['tradingAdvisor'][expertName]

    from shinehope.eaminer.EAInfo import EAInfo
    from shinehope.eaminer.MinerTalk import MinerTalk
    from shinehope.eaaccess.dataaccess.sqlite import DBAccess
    import shinehope.eaaccess.importers.klineimport as importer
    from shinehope.eaaccess.dataaccess.klinestream import KlineStream
    from shinehope.eaaccess.marketdata import BarData   
    from shinehope.utils.mylogger import appLog
    appLog.warning(startMsg)

    # if __name__ == '__main__':
    print("Enter...", __name__)

    if not settings.appMode == 'BACKTEST':
        appLog.warning("only support tradeMode('BACKTEST')...")
        sys.exit(0)

    ## init trading DB 
    dbaccess = DBAccess()
    dbaccess.initTradeDB(accID, True)
    bal = configs['balances']
    # dbaccess.loadBalance(tradeDB, bal)
    dbaccess.loadBalance(bal)

    """ init history DB """
    # init history DB
    tblSymbol = f"{currQuote}_{currAsset}"
    # histDB = dbaccess.initHistDB(settings.exchangeName, tblSymbol, False)
    initFlag = configs['backtest']['daterange']['initFlag']
    if initFlag or initForce:
        initFlag = True
    histDB = dbaccess.initHistDB(settings.exchangeName, tblSymbol, initFlag)

    # import history Candles
    rangeFrom = configs['backtest']['daterange']['from']
    rangeTo = configs['backtest']['daterange']['to']
    batchSize = configs['backtest']['daterange']['batchSize']
    dtFrom = datetime.strptime(rangeFrom, "%Y-%m-%d")
    dtTo =  datetime.strptime(rangeTo, "%Y-%m-%d")
    dtTo += timedelta(days=1)
    sstampFrom = int(dtFrom.timestamp())
    sstampTo = int(dtTo.timestamp())
    importer.syncCandlesticks(histDB, tblSymbol, sstampFrom, sstampTo, batchSize)    

    """ 2019.10.31
        # 允許 strategy_client 於 onInit(...) 中使用 set_market 改變 Market & Period
        # 移至 ea.broker.strategy_instance.onInit() 之後
    """
    # kstream = KlineStream(histDB, tblSymbol, settings.candleSize)
    # kstream.set_range(sstampFrom, sstampTo)

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

    ea = EAAccessStrategy.StrategyClient('V01.00.01')
    ea.aiboxConnect(settings.exchangeName, apiKey, apiSecret, accID)
    startCandle = configs['tradingAdvisor']['startCandle']
    ea.broker.kline.set_backtest_start_candle(startCandle)

    # ea.broker.set_backtest_db(tradeDB)
    ea.broker.set_dbaccess(dbaccess)
    ea.broker.strategy_instance.onInit()        ## 允許 strategy_client 於 onInit(...) 中使用 set_market 改變 Market & Period
    marketFee = configs['paper']['fee']
    ea.broker.set_fee_rate(marketFee)

    kstream = KlineStream(histDB, settings.symbol, tblSymbol, settings.candleSize)
    kstream.set_range(sstampFrom, sstampTo)
    ea.broker.set_backtest_stream(kstream)

    from shinehope.eaaccess.backtest import UIReport
    uiKline = UIReport()

    # print("before...backtest while")
    tickContinue = True
    bBreak = False
    # vSpread = configs['market']['askbidSpread']
    vSpread = configs['tradingAdvisor'][expertName]['market']['askbidSpread']
    while tickContinue:
        try:
            bar = kstream.nextBar()
            if bar:
                if bar.timestamp >= sstampTo * 1000:
                    tickContinue = False

                ea.broker.run_strategy(bar, uiKline)                    # 增加 UIReport optional para

                tick = kstream.bar_tickinfo(bar, vSpread)
                ea.broker.run_strategy(tick)
                # time.sleep(0.1)
            else:
                appLog.debug(bar)
                tickContinue = False
        except KeyboardInterrupt:
            bBreak = True
            print()
            print('Got Ctrl+C(Interrupt)...')
            print('disposing ...')
            ea.dispose()
            break

    if not bBreak:
        ea.broker.calculate(sstampFrom, sstampTo)   
        uiKline.report_profit(dbaccess, sstampTo)     
        
    ea.broker.strategy_instance.onDeinit()
    sys.exit(0)

