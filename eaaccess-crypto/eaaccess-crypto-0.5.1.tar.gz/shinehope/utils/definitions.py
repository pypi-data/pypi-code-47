import os
import platform
#sys.path.insert(0, os.path.abspath("."))
_runsystem = platform.system()
print("system : ", _runsystem)
#if runsystem == "Windows":
#    ROOT_DIR = os.path.abspath(".")
#else:
#    ROOT_DIR = os.path.abspath("..")
ROOT_DIR = os.path.abspath(".")
print("ROOT_DIR ==>", ROOT_DIR)
# EAACCESS_DIR = os.path.join(ROOT_DIR, 'shinehope')
EAACCESS_DIR = os.path.join(ROOT_DIR, 'shinehope')
if os.path.isdir(EAACCESS_DIR):
    pass
else:
    EAACCESS_DIR = os.path.join(ROOT_DIR, 'crypto')
    if os.path.isdir(EAACCESS_DIR):
        pass
    else:
        for entry in os.scandir(ROOT_DIR):
            if not entry.name.startswith('.') and entry.is_dir():
                if entry.name == "build":
                    pass
                elif entry.name == "dist":
                    pass
                else:
                    EAACCESS_DIR = entry.path
print("EAACCESS_DIR ==>", EAACCESS_DIR)

# import sys
# # sys.path.insert(0, ROOT_DIR + "/utils")

# import gettext
# import locale

# locale.setlocale(locale.LC_ALL, "")
# loc = locale.getdefaultlocale()
# # print(loc, ":definitions.py")

# domain = "EAAccessUIText"
# # domainfolder = ROOT_DIR + "/locale"
# domainfolder = os.path.join(EAACCESS_DIR, "locale")
# #gettext.bindtextdomain(domain, domainfolder)
# #gettext.textdomain(domain)
# #locale.setlocale(locale.LC_ALL, loc)
# #lblcontent = gettext.gettext("这是测试文字")
# # print("domainfolder : ", domainfolder)

# ##LANG = "zh_TW"
# #LANG=loc[0]
# PYCODEC = loc[1]
# tmpLang = loc[0].lower()
# if tmpLang in {"zh_tw", "zh_hk", "zh_mo", "zh_cht"}:
#     LANG = "zh_TW"
#     PYCODEC = "cp950"
# elif tmpLang in {"zh_cn", "zh_sg", "zh_chs"}:
#     LANG = "zh_CN"
#     PYCODEC = "gb2312"
# else:
#     LANG = "zh_CN"
#     PYCODEC = "gb2312"
#     if sys.platform.startswith('win'):
#         if os.getenv('LANG') == "zh_cht":
#             LANG = "zh_TW"
#             PYCODEC = "cp950"

# #### debug
# #LANG = "zh_CN"
# #PYCODEC = "gb2312"

    
# lang = gettext.translation(domain, domainfolder, languages=[LANG], fallback = False)
# _myLang = lang.gettext