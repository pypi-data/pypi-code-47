from enum import Enum

from currenpy.symbols import CurrencySymbol


class Currency(Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    USS = "USS"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XFU = "XFU"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XTS = "XTS"
    XUA = "XUA"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"


class CurrencyHelper:
    _CURRENCY_DATA = {
        Currency.AED: {
            "display_name": "UAE Dirham",
            "numeric_code": 784,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AED,
        },
        Currency.AFN: {
            "display_name": "Afghani",
            "numeric_code": 971,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AFN,
        },
        Currency.ALL: {
            "display_name": "Lek",
            "numeric_code": 8,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ALL,
        },
        Currency.AMD: {
            "display_name": "Armenian Dram",
            "numeric_code": 51,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AMD,
        },
        Currency.ANG: {
            "display_name": "Netherlands Antillean Guilder",
            "numeric_code": 532,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ANG,
        },
        Currency.AOA: {
            "display_name": "Kwanza",
            "numeric_code": 973,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AOA,
        },
        Currency.ARS: {
            "display_name": "Argentine Peso",
            "numeric_code": 32,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ARS,
        },
        Currency.AUD: {
            "display_name": "Australian Dollar",
            "numeric_code": 36,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AUD,
        },
        Currency.AWG: {
            "display_name": "Aruban Florin",
            "numeric_code": 533,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AWG,
        },
        Currency.AZN: {
            "display_name": "Azerbaijanian Manat",
            "numeric_code": 944,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.AZN,
        },
        Currency.BAM: {
            "display_name": "Convertible Mark",
            "numeric_code": 977,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BAM,
        },
        Currency.BBD: {
            "display_name": "Barbados Dollar",
            "numeric_code": 52,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BBD,
        },
        Currency.BDT: {
            "display_name": "Taka",
            "numeric_code": 50,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BDT,
        },
        Currency.BGN: {
            "display_name": "Bulgarian Lev",
            "numeric_code": 975,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BGN,
        },
        Currency.BHD: {
            "display_name": "Bahraini Dinar",
            "numeric_code": 48,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.BHD,
        },
        Currency.BIF: {
            "display_name": "Burundi Franc",
            "numeric_code": 108,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BIF,
        },
        Currency.BMD: {
            "display_name": "Bermudian Dollar",
            "numeric_code": 60,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BMD,
        },
        Currency.BND: {
            "display_name": "Brunei Dollar",
            "numeric_code": 96,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BND,
        },
        Currency.BOB: {
            "display_name": "Boliviano",
            "numeric_code": 68,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BOB,
        },
        Currency.BOV: {
            "display_name": "Mvdol",
            "numeric_code": 984,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BOV,
        },
        Currency.BRL: {
            "display_name": "Brazilian Real",
            "numeric_code": 986,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BRL,
        },
        Currency.BSD: {
            "display_name": "Bahamian Dollar",
            "numeric_code": 44,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BSD,
        },
        Currency.BTN: {
            "display_name": "Ngultrum",
            "numeric_code": 64,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BTN,
        },
        Currency.BWP: {
            "display_name": "Pula",
            "numeric_code": 72,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BWP,
        },
        Currency.BYR: {
            "display_name": "Belarussian Ruble",
            "numeric_code": 974,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BYR,
        },
        Currency.BZD: {
            "display_name": "Belize Dollar",
            "numeric_code": 84,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.BZD,
        },
        Currency.CAD: {
            "display_name": "Canadian Dollar",
            "numeric_code": 124,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CAD,
        },
        Currency.CDF: {
            "display_name": "Congolese Franc",
            "numeric_code": 976,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CDF,
        },
        Currency.CHE: {
            "display_name": "WIR Euro",
            "numeric_code": 947,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CHE,
        },
        Currency.CHF: {
            "display_name": "Swiss Franc",
            "numeric_code": 756,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CHF,
        },
        Currency.CHW: {
            "display_name": "WIR Franc",
            "numeric_code": 948,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CHW,
        },
        Currency.CLF: {
            "display_name": "Unidades de fomento",
            "numeric_code": 990,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CLF,
        },
        Currency.CLP: {
            "display_name": "Chilean Peso",
            "numeric_code": 152,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CLP,
        },
        Currency.CNY: {
            "display_name": "Yuan Renminbi",
            "numeric_code": 156,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CNY,
        },
        Currency.COP: {
            "display_name": "Colombian Peso",
            "numeric_code": 170,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.COP,
        },
        Currency.COU: {
            "display_name": "Unidad de Valor Real",
            "numeric_code": 970,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.COU,
        },
        Currency.CRC: {
            "display_name": "Costa Rican Colon",
            "numeric_code": 188,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CRC,
        },
        Currency.CUC: {
            "display_name": "Peso Convertible",
            "numeric_code": 931,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CUC,
        },
        Currency.CUP: {
            "display_name": "Cuban Peso",
            "numeric_code": 192,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CUP,
        },
        Currency.CVE: {
            "display_name": "Cape Verde Escudo",
            "numeric_code": 132,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CVE,
        },
        Currency.CZK: {
            "display_name": "Czech Koruna",
            "numeric_code": 203,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.CZK,
        },
        Currency.DJF: {
            "display_name": "Djibouti Franc",
            "numeric_code": 262,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.DJF,
        },
        Currency.DKK: {
            "display_name": "Danish Krone",
            "numeric_code": 208,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.DKK,
        },
        Currency.DOP: {
            "display_name": "Dominican Peso",
            "numeric_code": 214,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.DOP,
        },
        Currency.DZD: {
            "display_name": "Algerian Dinar",
            "numeric_code": 12,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.DZD,
        },
        Currency.EGP: {
            "display_name": "Egyptian Pound",
            "numeric_code": 818,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.EGP,
        },
        Currency.ERN: {
            "display_name": "Nakfa",
            "numeric_code": 232,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ERN,
        },
        Currency.ETB: {
            "display_name": "Ethiopian Birr",
            "numeric_code": 230,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ETB,
        },
        Currency.EUR: {
            "display_name": "Euro",
            "numeric_code": 978,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.EUR,
        },
        Currency.FJD: {
            "display_name": "Fiji Dollar",
            "numeric_code": 242,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.FJD,
        },
        Currency.FKP: {
            "display_name": "Falkland Islands Pound",
            "numeric_code": 238,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.FKP,
        },
        Currency.GBP: {
            "display_name": "Pound Sterling",
            "numeric_code": 826,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GBP,
        },
        Currency.GEL: {
            "display_name": "Lari",
            "numeric_code": 981,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GEL,
        },
        Currency.GHS: {
            "display_name": "Ghana Cedi",
            "numeric_code": 936,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GHS,
        },
        Currency.GIP: {
            "display_name": "Gibraltar Pound",
            "numeric_code": 292,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GIP,
        },
        Currency.GMD: {
            "display_name": "Dalasi",
            "numeric_code": 270,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GMD,
        },
        Currency.GNF: {
            "display_name": "Guinea Franc",
            "numeric_code": 324,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GNF,
        },
        Currency.GTQ: {
            "display_name": "Quetzal",
            "numeric_code": 320,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GTQ,
        },
        Currency.GYD: {
            "display_name": "Guyana Dollar",
            "numeric_code": 328,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.GYD,
        },
        Currency.HKD: {
            "display_name": "Hong Kong Dollar",
            "numeric_code": 344,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.HKD,
        },
        Currency.HNL: {
            "display_name": "Lempira",
            "numeric_code": 340,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.HNL,
        },
        Currency.HRK: {
            "display_name": "Croatian Kuna",
            "numeric_code": 191,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.HRK,
        },
        Currency.HTG: {
            "display_name": "Gourde",
            "numeric_code": 332,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.HTG,
        },
        Currency.HUF: {
            "display_name": "Forint",
            "numeric_code": 348,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.HUF,
        },
        Currency.IDR: {
            "display_name": "Rupiah",
            "numeric_code": 360,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.IDR,
        },
        Currency.ILS: {
            "display_name": "New Israeli Sheqel",
            "numeric_code": 376,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ILS,
        },
        Currency.INR: {
            "display_name": "Indian Rupee",
            "numeric_code": 356,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.INR,
        },
        Currency.IQD: {
            "display_name": "Iraqi Dinar",
            "numeric_code": 368,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.IQD,
        },
        Currency.IRR: {
            "display_name": "Iranian Rial",
            "numeric_code": 364,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.IRR,
        },
        Currency.ISK: {
            "display_name": "Iceland Krona",
            "numeric_code": 352,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ISK,
        },
        Currency.JMD: {
            "display_name": "Jamaican Dollar",
            "numeric_code": 388,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.JMD,
        },
        Currency.JOD: {
            "display_name": "Jordanian Dinar",
            "numeric_code": 400,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.JOD,
        },
        Currency.JPY: {
            "display_name": "Yen",
            "numeric_code": 392,
            "default_fraction_digits": 0,
            "sub_unit": 1,
            "symbol": CurrencySymbol.JPY,
        },
        Currency.KES: {
            "display_name": "Kenyan Shilling",
            "numeric_code": 404,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KES,
        },
        Currency.KGS: {
            "display_name": "Som",
            "numeric_code": 417,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KGS,
        },
        Currency.KHR: {
            "display_name": "Riel",
            "numeric_code": 116,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KHR,
        },
        Currency.KMF: {
            "display_name": "Comoro Franc",
            "numeric_code": 174,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KMF,
        },
        Currency.KPW: {
            "display_name": "North Korean Won",
            "numeric_code": 408,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KPW,
        },
        Currency.KRW: {
            "display_name": "Won",
            "numeric_code": 410,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KRW,
        },
        Currency.KWD: {
            "display_name": "Kuwaiti Dinar",
            "numeric_code": 414,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.KWD,
        },
        Currency.KYD: {
            "display_name": "Cayman Islands Dollar",
            "numeric_code": 136,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KYD,
        },
        Currency.KZT: {
            "display_name": "Tenge",
            "numeric_code": 398,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.KZT,
        },
        Currency.LAK: {
            "display_name": "Kip",
            "numeric_code": 418,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LAK,
        },
        Currency.LBP: {
            "display_name": "Lebanese Pound",
            "numeric_code": 422,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LBP,
        },
        Currency.LKR: {
            "display_name": "Sri Lanka Rupee",
            "numeric_code": 144,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LKR,
        },
        Currency.LRD: {
            "display_name": "Liberian Dollar",
            "numeric_code": 430,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LRD,
        },
        Currency.LSL: {
            "display_name": "Loti",
            "numeric_code": 426,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LSL,
        },
        Currency.LTL: {
            "display_name": "Lithuanian Litas",
            "numeric_code": 440,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LTL,
        },
        Currency.LVL: {
            "display_name": "Latvian Lats",
            "numeric_code": 428,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.LVL,
        },
        Currency.LYD: {
            "display_name": "Libyan Dinar",
            "numeric_code": 434,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.LYD,
        },
        Currency.MAD: {
            "display_name": "Moroccan Dirham",
            "numeric_code": 504,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MAD,
        },
        Currency.MDL: {
            "display_name": "Moldovan Leu",
            "numeric_code": 498,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MDL,
        },
        Currency.MGA: {
            "display_name": "Malagasy Ariary",
            "numeric_code": 969,
            "default_fraction_digits": 2,
            "sub_unit": 5,
            "symbol": CurrencySymbol.MGA,
        },
        Currency.MKD: {
            "display_name": "Denar",
            "numeric_code": 807,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MKD,
        },
        Currency.MMK: {
            "display_name": "Kyat",
            "numeric_code": 104,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MMK,
        },
        Currency.MNT: {
            "display_name": "Tugrik",
            "numeric_code": 496,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MNT,
        },
        Currency.MOP: {
            "display_name": "Pataca",
            "numeric_code": 446,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MOP,
        },
        Currency.MRO: {
            "display_name": "Ouguiya",
            "numeric_code": 478,
            "default_fraction_digits": 2,
            "sub_unit": 5,
            "symbol": CurrencySymbol.MRO,
        },
        Currency.MUR: {
            "display_name": "Mauritius Rupee",
            "numeric_code": 480,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MUR,
        },
        Currency.MVR: {
            "display_name": "Rufiyaa",
            "numeric_code": 462,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MVR,
        },
        Currency.MWK: {
            "display_name": "Kwacha",
            "numeric_code": 454,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MWK,
        },
        Currency.MXN: {
            "display_name": "Mexican Peso",
            "numeric_code": 484,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MXN,
        },
        Currency.MXV: {
            "display_name": "Mexican Unidad de Inversion (UDI)",
            "numeric_code": 979,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MXV,
        },
        Currency.MYR: {
            "display_name": "Malaysian Ringgit",
            "numeric_code": 458,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MYR,
        },
        Currency.MZN: {
            "display_name": "Mozambique Metical",
            "numeric_code": 943,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.MZN,
        },
        Currency.NAD: {
            "display_name": "Namibia Dollar",
            "numeric_code": 516,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NAD,
        },
        Currency.NGN: {
            "display_name": "Naira",
            "numeric_code": 566,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NGN,
        },
        Currency.NIO: {
            "display_name": "Cordoba Oro",
            "numeric_code": 558,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NIO,
        },
        Currency.NOK: {
            "display_name": "Norwegian Krone",
            "numeric_code": 578,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NOK,
        },
        Currency.NPR: {
            "display_name": "Nepalese Rupee",
            "numeric_code": 524,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NPR,
        },
        Currency.NZD: {
            "display_name": "New Zealand Dollar",
            "numeric_code": 554,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.NZD,
        },
        Currency.OMR: {
            "display_name": "Rial Omani",
            "numeric_code": 512,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.OMR,
        },
        Currency.PAB: {
            "display_name": "Balboa",
            "numeric_code": 590,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PAB,
        },
        Currency.PEN: {
            "display_name": "Nuevo Sol",
            "numeric_code": 604,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PEN,
        },
        Currency.PGK: {
            "display_name": "Kina",
            "numeric_code": 598,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PGK,
        },
        Currency.PHP: {
            "display_name": "Philippine Peso",
            "numeric_code": 608,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PHP,
        },
        Currency.PKR: {
            "display_name": "Pakistan Rupee",
            "numeric_code": 586,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PKR,
        },
        Currency.PLN: {
            "display_name": "Zloty",
            "numeric_code": 985,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PLN,
        },
        Currency.PYG: {
            "display_name": "Guarani",
            "numeric_code": 600,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.PYG,
        },
        Currency.QAR: {
            "display_name": "Qatari Rial",
            "numeric_code": 634,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.QAR,
        },
        Currency.RON: {
            "display_name": "New Romanian Leu",
            "numeric_code": 946,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.RON,
        },
        Currency.RSD: {
            "display_name": "Serbian Dinar",
            "numeric_code": 941,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.RSD,
        },
        Currency.RUB: {
            "display_name": "Russian Ruble",
            "numeric_code": 643,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.RUB,
        },
        Currency.RWF: {
            "display_name": "Rwanda Franc",
            "numeric_code": 646,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.RWF,
        },
        Currency.SAR: {
            "display_name": "Saudi Riyal",
            "numeric_code": 682,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SAR,
        },
        Currency.SBD: {
            "display_name": "Solomon Islands Dollar",
            "numeric_code": 90,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SBD,
        },
        Currency.SCR: {
            "display_name": "Seychelles Rupee",
            "numeric_code": 690,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SCR,
        },
        Currency.SDG: {
            "display_name": "Sudanese Pound",
            "numeric_code": 938,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SDG,
        },
        Currency.SEK: {
            "display_name": "Swedish Krona",
            "numeric_code": 752,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SEK,
        },
        Currency.SGD: {
            "display_name": "Singapore Dollar",
            "numeric_code": 702,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SGD,
        },
        Currency.SHP: {
            "display_name": "Saint Helena Pound",
            "numeric_code": 654,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SHP,
        },
        Currency.SLL: {
            "display_name": "Leone",
            "numeric_code": 694,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SLL,
        },
        Currency.SOS: {
            "display_name": "Somali Shilling",
            "numeric_code": 706,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SOS,
        },
        Currency.SRD: {
            "display_name": "Surinam Dollar",
            "numeric_code": 968,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SRD,
        },
        Currency.SSP: {
            "display_name": "South Sudanese Pound",
            "numeric_code": 728,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SSP,
        },
        Currency.STD: {
            "display_name": "Dobra",
            "numeric_code": 678,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.STD,
        },
        Currency.SVC: {
            "display_name": "El Salvador Colon",
            "numeric_code": 222,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SVC,
        },
        Currency.SYP: {
            "display_name": "Syrian Pound",
            "numeric_code": 760,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SYP,
        },
        Currency.SZL: {
            "display_name": "Lilangeni",
            "numeric_code": 748,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.SZL,
        },
        Currency.THB: {
            "display_name": "Baht",
            "numeric_code": 764,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.THB,
        },
        Currency.TJS: {
            "display_name": "Somoni",
            "numeric_code": 972,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TJS,
        },
        Currency.TMT: {
            "display_name": "Turkmenistan New Manat",
            "numeric_code": 934,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TMT,
        },
        Currency.TND: {
            "display_name": "Tunisian Dinar",
            "numeric_code": 788,
            "default_fraction_digits": 3,
            "sub_unit": 1000,
            "symbol": CurrencySymbol.TND,
        },
        Currency.TOP: {
            "display_name": "Pa’anga",
            "numeric_code": 776,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TOP,
        },
        Currency.TRY: {
            "display_name": "Turkish Lira",
            "numeric_code": 949,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TRY,
        },
        Currency.TTD: {
            "display_name": "Trinidad and Tobago Dollar",
            "numeric_code": 780,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TTD,
        },
        Currency.TWD: {
            "display_name": "New Taiwan Dollar",
            "numeric_code": 901,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TWD,
        },
        Currency.TZS: {
            "display_name": "Tanzanian Shilling",
            "numeric_code": 834,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.TZS,
        },
        Currency.UAH: {
            "display_name": "Hryvnia",
            "numeric_code": 980,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.UAH,
        },
        Currency.UGX: {
            "display_name": "Uganda Shilling",
            "numeric_code": 800,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.UGX,
        },
        Currency.USD: {
            "display_name": "US Dollar",
            "numeric_code": 840,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.USD,
        },
        Currency.USN: {
            "display_name": "US Dollar (Next day)",
            "numeric_code": 997,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.USN,
        },
        Currency.USS: {
            "display_name": "US Dollar (Same day)",
            "numeric_code": 998,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.USS,
        },
        Currency.UYI: {
            "display_name": "Uruguay Peso en Unidades Indexadas (URUIURUI)",
            "numeric_code": 940,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.UYI,
        },
        Currency.UYU: {
            "display_name": "Peso Uruguayo",
            "numeric_code": 858,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.UYU,
        },
        Currency.UZS: {
            "display_name": "Uzbekistan Sum",
            "numeric_code": 860,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.UZS,
        },
        Currency.VEF: {
            "display_name": "Bolivar",
            "numeric_code": 937,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.VEF,
        },
        Currency.VND: {
            "display_name": "Dong",
            "numeric_code": 704,
            "default_fraction_digits": 0,
            "sub_unit": 10,
            "symbol": CurrencySymbol.VND,
        },
        Currency.VUV: {
            "display_name": "Vatu",
            "numeric_code": 548,
            "default_fraction_digits": 0,
            "sub_unit": 1,
            "symbol": CurrencySymbol.VUV,
        },
        Currency.WST: {
            "display_name": "Tala",
            "numeric_code": 882,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.WST,
        },
        Currency.XAF: {
            "display_name": "CFA Franc BEAC",
            "numeric_code": 950,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XAF,
        },
        Currency.XAG: {
            "display_name": "Silver",
            "numeric_code": 961,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XAG,
        },
        Currency.XAU: {
            "display_name": "Gold",
            "numeric_code": 959,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XAU,
        },
        Currency.XBA: {
            "display_name": "Bond Markets Unit European Composite Unit (EURCO)",
            "numeric_code": 955,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XBA,
        },
        Currency.XBB: {
            "display_name": "Bond Markets Unit European Monetary Unit (E.M.U.-6)",
            "numeric_code": 956,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XBB,
        },
        Currency.XBC: {
            "display_name": "Bond Markets Unit European Unit of Account 9 (E.U.A.-9)",
            "numeric_code": 957,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XBC,
        },
        Currency.XBD: {
            "display_name": "Bond Markets Unit European Unit of Account 17 (E.U.A.-17)",
            "numeric_code": 958,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XBD,
        },
        Currency.XCD: {
            "display_name": "East Caribbean Dollar",
            "numeric_code": 951,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XCD,
        },
        Currency.XDR: {
            "display_name": "SDR (Special Drawing Right)",
            "numeric_code": 960,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XDR,
        },
        Currency.XFU: {
            "display_name": "UIC-Franc",
            "numeric_code": 958,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XFU,
        },
        Currency.XOF: {
            "display_name": "CFA Franc BCEAO",
            "numeric_code": 952,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XOF,
        },
        Currency.XPD: {
            "display_name": "Palladium",
            "numeric_code": 964,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XPD,
        },
        Currency.XPF: {
            "display_name": "CFP Franc",
            "numeric_code": 953,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XPF,
        },
        Currency.XPT: {
            "display_name": "Platinum",
            "numeric_code": 962,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XPT,
        },
        Currency.XSU: {
            "display_name": "Sucre",
            "numeric_code": 994,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XSU,
        },
        Currency.XTS: {
            "display_name": "Codes specifically reserved for testing purposes",
            "numeric_code": 963,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XTS,
        },
        Currency.XUA: {
            "display_name": "ADB Unit of Account",
            "numeric_code": 965,
            "default_fraction_digits": 0,
            "sub_unit": 100,
            "symbol": CurrencySymbol.XUA,
        },
        Currency.YER: {
            "display_name": "Yemeni Rial",
            "numeric_code": 886,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.YER,
        },
        Currency.ZAR: {
            "display_name": "Rand",
            "numeric_code": 710,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ZAR,
        },
        Currency.ZMW: {
            "display_name": "Zambian Kwacha",
            "numeric_code": 967,
            "default_fraction_digits": 2,
            "sub_unit": 100,
            "symbol": CurrencySymbol.ZMW,
        },
        Currency.ZWL: {
            "display_name": "Zimbabwe Dollar",
            "numeric_code": 932,
            "default_fraction_digits": 2,
            "sub_unit": 100,
        },
    }

    @classmethod
    def decimal_precision_for_currency(cls, currency: Currency) -> int:
        """Returns the decimal precision for a currency (number of digits after the decimal)"""

        return cls._CURRENCY_DATA[currency]["default_fraction_digits"]

    @classmethod
    def sub_unit_for_currency(cls, currency: Currency) -> int:
        """Returns the sub unit for a currency.
        (eg, the subunit for USD is 100 because there are 100 cents in a dollar)

        """
        return cls._CURRENCY_DATA[currency]["sub_unit"]

    @classmethod
    def symbol_for_currency(cls, currency: Currency) -> str:
        return cls._CURRENCY_DATA[currency]["symbol"]
