#!/usr/bin/env python

"""command line cloudwatch client"""

import argparse
from argparse import RawTextHelpFormatter as rawtxt
import subprocess
import json
import os
import re
import datetime
import time
import pkg_resources
from stringcolor import cs, bold, underline

def load_dirty_json(dirty_json):
    """do some crazy shit to the message"""
    regex_replace = [(r"([ \{,:\[])(u)?'([^']+)'", r'\1"\3"'), (r" False([, \}\]])", r' false\1'), (r" True([, \}\]])", r' true\1')]
    for r, s in regex_replace:
        dirty_json = re.sub(r, s, dirty_json)
    clean_json = json.loads(dirty_json)
    return clean_json

def mapFunc(x):
    """reformatting list of timestamps and messages"""
    x['timestamp'] = datetime.datetime.fromtimestamp(x['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S')
    x['ingestionTime'] = datetime.datetime.fromtimestamp(x['ingestionTime']/1000).strftime('%Y-%m-%d %H:%M:%S')
    try:
        x['message'] = load_dirty_json(x['message'])
        #x['message'] = json.dumps(x['message'], indent=4, sort_keys=True)
    except:
        x['message'] = x['message']
    try:
        x['message'] = x['message'].replace("\n", "")
    except:
        pass
# report, start, end, else
    if "START" in x['message']:
        xarr = x['message'].split("START")
        x['message'] = xarr[0]+str(cs("START", "green"))+xarr[1]
    elif "END" in x['message']:
        xarr = x['message'].split("END")
        x['message'] = xarr[0]+str(cs("END", "red"))+xarr[1]
    elif "REPORT" in x['message']:
        xarr = x['message'].split("REPORT")
        x['message'] = xarr[0]+str(cs("REPORT", "orange"))+xarr[1]
    else:
        x['message'] = str(cs(x['message'], "SteelBlue"))
    return x

def time_to_epoch(str_time):
    """convert yyyy-mm-dd hh:mm:ss to unix epoch"""
    # check for time and seconds parts
    first_split = str_time.split(" ")
    if len(first_split) < 2:
        # there is no time part
        str_time = str_time+" 00:00:00"
        first_split = str_time.split(" ")
    second_split = first_split[1].split(":")
    if len(second_split) < 3:
        # there are no seconds
        str_time = str_time+":00"

    time_tuple = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    time_epoch = time.mktime(time_tuple)
    return str(int(time_epoch) * 1000)

def columnify(iterable):
    """convert iterable to columns"""
    # First convert everything to its repr
    strings = [str(x) for x in iterable]
    # Now pad all the strings to match the widest
    widest = max(len(x) for x in strings)
    padded = [x.ljust(widest) for x in strings]
    return padded

def colprint(iterable, width=72):
    """print iterable in columns"""
    columns = columnify(iterable)
    colwidth = len(columns[0])+2
    perline = (width-4) // colwidth
    for i, column in enumerate(columns):
        print(column, end=' ')
        if i % perline == perline-1:
            print('\n', end='')

def main():
    """cli cloudwatch client"""
    version = pkg_resources.require("nef")[0].version
    parser = argparse.ArgumentParser(
        description='command line cloudwatch client',
        prog='nef',
        formatter_class=rawtxt
    )
    yesterday = datetime.datetime.now() - datetime.timedelta(hours=24)
    parser.add_argument('log', nargs="?", help='Which log group to view')
    parser.add_argument("--start", help="""optional. give a start date and time.
"""+str(cs("format: YYYY-MM-DD HH:MM:SS", "lightgrey13"))+"""
"""+str(cs("example: ", "pink"))+"""nef /path/to/log-group --start 2019-11-25
"""+str(cs("example 2: ", "pink"))+"""nef /path/to/log-group --start \"2019-11-25 10:24\"
"""+str(cs("example 3: ", "pink"))+"""nef /path/to/log-group --start \"2019-11-25 10:24:32\"
"""+str(cs("default (if arg not given): "+yesterday.strftime("%Y-%m-%d %H:%M:%S"), "lightgrey13")), default=yesterday.strftime("%Y-%m-%d %H:%M:%S"))
    parser.add_argument("--end", help="optional. define an end date/time.\nsee --start for formatting info", default=None)
    parser.add_argument('-c', '--columns', action='store_true', help='show log groups in columns')
    parser.add_argument("-j", "--json", action="store_true", help="display output as json")
    parser.add_argument("-r", "--recent", action="store_true", help="show messages for log group created in the last 5 minutes.")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)
    args = parser.parse_args()
    log_group = args.log
    start_time = args.start
    end_time = args.end
    columnar = args.columns
    dojson = args.json
    only_recent = args.recent
    if log_group is None:
        # NO LOG GROUP PROVIDED, LIST ALL LOG GROUPS
        column_extra = ""
        if columnar:
            column_extra = " in column format"
        print(cs("no log group given", "gold"))
        print(cs(f"printing a list of log groups{column_extra}:", "DarkSlateGray3"))
        print()
        try:
            describe = "aws logs describe-log-groups --output json"
            log_groups = subprocess.check_output(describe, shell=True).decode("utf-8").strip()
            log_groups = json.loads(log_groups)
            log_groups = log_groups["logGroups"]
        except:
            print(cs("sorry,", "red"), cs("could not get a list of log groups", "yellow"))
            exit()
        cleansed = []
        if log_groups:
            for lg in log_groups:
                if columnar:
                    cleansed.append(lg["logGroupName"])
                else:
                    print(lg["logGroupName"])
        if cleansed:
            rows, columns = os.popen('stty size', 'r').read().split()
            colprint(cleansed, int(columns))
            print()
        exit()
    else:
        # LOG GROUP PROVIDED. HERE WE GO.
        end_string = ""
        if end_time is not None:
            end_string = f" --end-time {time_to_epoch(end_time)}"
        if only_recent:
            print(cs("showing messages from the last 5 minutes...", "DarkGreen"))
            now = datetime.datetime.now()
            recent = now - datetime.timedelta(minutes = 5) 
            recent_string = recent.strftime("%Y-%m-%d %H:%M:%S")
            end_string = f" --end-time {time_to_epoch(recent_string)}"
        cmd = f"aws logs filter-log-events --log-group-name {log_group} --start-time {time_to_epoch(start_time)}{end_string} --output json"
        out = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        out = json.loads(out)
        out = list(map(mapFunc, out['events']))
        if not out:
            print(cs("unable to find any cloudwatch logs since:", "yellow"), start_time)
            print(cs("you might try an earlier start time using the --start flag", "khaki"))
            print()
            print("try: nef -h for more info")
        if dojson:
            print(json.dumps(out, indent=4, sort_keys=True))
        else:
            last_time = None
            for log in out:
                last_time = log["timestamp"]
                print(cs("log stream:", "Khaki"), log["logStreamName"].split("]")[1])
                print(cs("time:", "Khaki"), log["timestamp"])
                print(cs("message:", "Khaki"), log["message"])
                print(cs("ingestion time:", "Khaki"), log["ingestionTime"])
                print(cs("event id", "Khaki"), log["eventId"])
                print(cs("-------", "grey"))
            try:
                d = datetime.datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S")
                one_second_later = d + datetime.timedelta(0,1)
                print(cs("run the following command for new messages (not including this message):", "grey2"))
                print(cs(f"nef {log_group} --start \"{one_second_later}\"", "indianred2"))
            except Exception:
                pass

if __name__ == "__main__":
    main()
