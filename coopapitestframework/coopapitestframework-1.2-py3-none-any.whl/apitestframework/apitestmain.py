import sys, getopt
# from xforceCloudTest.business import robotFileUtils
# from test_case import get_cases, test_yamlapi
import os

def help():
    msg = "*" * 100 + "\n" \
          + '您在使用票易通云测本地版，有bug和有问题反馈请联系杨凯[yangkai@xforceplus.com]\n\n' \
          + "--help: 显示帮助。\n\n" \
          + "--file: 运行指定的文件或者路径。\n\n" \
          + "*" * 100
    print(msg)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:h:",["file=","help="])
    except Exception:
        help()
        sys.exit(-1)
    for opt, value in opts:
        if opt == '-h' or opt=='--help':
            help()
            sys.exit(0)
        elif opt in ("-f", "--file"):
            file_path=value
            if file_path !='*.py':
                cmd = 'pytest -s ' + file_path
            else:
                cmd = 'pytest -s'
            print('cmd=%s'%cmd)
            os.system(cmd)
            sys.exit(0)
        help()
