from pymongo import ASCENDING

# index_symbol is yahoo ticker symbol
indexMap = {
    "yh_symbol": [('symbol',  ASCENDING)],
    "ms_symbol": [('symbol',  ASCENDING)],
    "yh_currency": [('index_symbol',  ASCENDING)],
    "ms_currency": [('index_symbol',  ASCENDING)],
    "yh_ohlcv_3mo": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_1mo": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_1wk": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_5d": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_1d": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_1h": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_90m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_60m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_30m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_15m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_5m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_2m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_ohlcv_1m": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_assetProfile": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_assetProfile_companyOfficers": [
        ('index_symbol',  ASCENDING),
        ('name',  ASCENDING)
    ],
    "yh_balanceSheetStatementsYearly": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_balanceSheetStatementsQuarterly": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_calendarEvents": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_calendarEvents_earnings": [
        ('index_symbol',  ASCENDING),
        ('earningsDate',  ASCENDING)
    ],
    "yh_cashflowStatementsYearly": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_cashflowStatementsQuarterly": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_keyStatistics": [
        ('index_symbol',  ASCENDING),
        ("lastFiscalYearEnd",  ASCENDING)
    ],
    "yh_earnings_earningsChart_quarterly": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_earnings_earningsChart": [
        ('index_symbol',  ASCENDING),
        ('earningsDate',  ASCENDING)
    ],
    "yh_earnings_financialsChart_yearly": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_earnings_financialsChart_quarterly": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_earnings": [
        ('index_symbol',  ASCENDING)
    ],
    "yh_earningsHistory": [
        ('index_symbol',  ASCENDING),
        ('quarter',  ASCENDING)
    ],
    "yh_earningsTrend": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_esgScores_peerEsgScorePerformance": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores_peerGovernancePerformance": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores_peerSocialPerformance": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores_peerEnvironmentPerformance": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores_peerHighestControversyPerformance": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores_relatedControversy": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_esgScores": [
        ('index_symbol',  ASCENDING),
        ('ratingYear',  ASCENDING),
        ('ratingMonth',  ASCENDING)
    ],
    "yh_financial_data": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_fundOwnership_ownershipList": [
        ('index_symbol',  ASCENDING),
        ('reportDate',  ASCENDING)
    ],
    "yh_incomeStatementHistory": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_incomeStatementHistoryQuarterly": [
        ('index_symbol',  ASCENDING),
        ('endDate',  ASCENDING)
    ],
    "yh_indexTrend_estimates": [
        ('index_symbol',  ASCENDING),
        ('date', ASCENDING),
        ('period',  ASCENDING)
    ],
    # 02-01-2020 : added combination of period and date as index
    # otherwise next quarter and 0y not unique.
    "yh_indexTrend": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING),
    ],
    # 02-01-2020 : added combination of period and date as index
    # otherwise next quarter and 0y not unique.
    "yh_industryTrend_estimates": [
        ('index_symbol',  ASCENDING),
        ('date', ASCENDING),
        ('period',  ASCENDING)
    ],
    "yh_industryTrend": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_insiderHolders": [
        ('index_symbol',  ASCENDING),
        ('latestTransDate',  ASCENDING),
        ('name',  ASCENDING),
        ('transactionDescription',  ASCENDING)
    ],
    "yh_insiderTransactions": [
        ('index_symbol',  ASCENDING),
        ('filerName',  ASCENDING),
        ('startDate',  ASCENDING)
    ],
    "yh_institutionOwnership": [
        ('index_symbol',  ASCENDING),
        ('organization',  ASCENDING),
        ('reportDate',  ASCENDING)
    ],
    "yh_majorDirectHolders": [
        ('index_symbol',  ASCENDING),
        ('name',  ASCENDING),
        ('reportDate',  ASCENDING)
    ],
    "yh_majorHoldersBreakdown": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_netSharePurchaseActivity": [
        ('index_symbol',  ASCENDING),
        ('period',  ASCENDING)
    ],
    "yh_price": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING)
    ],
    "yh_quoteType": [
        ('index_symbol',  ASCENDING)
    ],
    "yh_recommendationTrend": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING),
        ('period', ASCENDING)
    ],
    "yh_secFilings": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING),
        ('type',  ASCENDING)
    ],
    "yh_sectorTrend_estimates": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING),
        ('period',  ASCENDING)
    ],
    "yh_sectorTrend": [
        ('index_symbol',  ASCENDING),
        ('date',  ASCENDING),
    ],
    "yh_summaryDetail": [
        ('index_symbol',  ASCENDING),
        ('startDate',  ASCENDING)
    ],
    "yh_upgradeDowngradeHistory": [
        ('index_symbol',  ASCENDING),
        ('firm',  ASCENDING),
        ('epochGradeDate',  ASCENDING),
        ('action',  ASCENDING)
    ],
    "ms_balancesheet": [
        ('index_symbol',  ASCENDING),
        ('year',  ASCENDING)
    ],
    "ms_profitabilityRatios": [
        ('index_symbol',  ASCENDING),
        ('year',  ASCENDING)
    ],
    "ms_cashflowsheet": [
        ('index_symbol',  ASCENDING),
        ('year',  ASCENDING)
    ],
    "ms_liquidity": [
        ('index_symbol',  ASCENDING),
        ('year',  ASCENDING)
    ],
    "ms_financials": [
        ('index_symbol',  ASCENDING),
        ('year',  ASCENDING)
    ],
}
