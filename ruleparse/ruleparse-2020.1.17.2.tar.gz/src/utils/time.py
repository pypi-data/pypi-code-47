#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 10:01
# @Author  : Niyoufa
import re
import datetime
from ruleadmin.utils.number import is_number, IntegerParse

def time_convert(x):
    times = []
    units = []
    for i in x:
        time=""
        unit=""
        convert_times = []
        convert_units = []
        for j in i:
            if is_number(j):
                time+=j
            else:
                if time:
                    convert_times.append(time)
                time=""
            if not is_number(j):
                unit += j
            else:
                if unit:
                    convert_units.append(unit)
                unit=""
        else:
            if unit:
                convert_units.append(unit)
        times.append(convert_times)
        units.append(convert_units)
    return times,units

def num_convert(times,units):
    convert_dates=[]
    integerparse = IntegerParse()
    for time, unit in zip(times, units):
        convert_time = integerparse.testdig(time)
        convert_date = ""
        for i,j in zip(convert_time,unit):
            convert_date+=(str(i)+j)
        convert_dates.append(convert_date)
    return convert_dates

def formates_duration(formate_time):
    year_regex = r"(\d+)年.*"
    year_compile_regex = re.compile(year_regex)

    quarter_regex  = r"(\d+)季.*"
    quarter_compile_regex = re.compile(quarter_regex)

    month_regex = r"(\d+)[个]?月.*"
    month_compile_regex = re.compile(month_regex)

    ten_days_regex = r"(\d+)旬.*"
    ten_days_compile_regex = re.compile(ten_days_regex)

    week_regex =  r"(\d+)[个]?(?:周|礼拜).*"
    week_compile_regex = re.compile(week_regex)

    fif_days_regix=  r"(\d+)候.*"
    fif_days_compile_regex = re.compile(fif_days_regix)

    day_regex = r"(\d+)[天日].*"
    day_compile_regex = re.compile(day_regex)

    hour_regex = r"(\d+)[个]?[小]?时.*"
    hour_compile_regex = re.compile(hour_regex)

    quarter_hour_regex=r"(\d+)刻[钟]?.*"
    quarter_hour_compile_regex = re.compile(quarter_hour_regex)

    minute_regex = r"(\d+)分[钟]?.*"
    minute_compile_regex = re.compile(minute_regex)

    second_regex = r"(\d+)秒.*"
    second_compile_regex = re.compile(second_regex)

    times,units = time_convert(formate_time)
    convert_dates = num_convert(times,units)
    datetime_formates = []
    for i,unit_origin in enumerate(convert_dates):

        try:
            year = year_compile_regex.search(unit_origin).group(1)
        except:
            year = 0
        try:
            quarter = quarter_compile_regex.search(unit_origin).group(1)
        except:
            quarter = 0
        try:
            month = month_compile_regex.search(unit_origin).group(1)
        except:
            month = 0
        try:
            ten_days = ten_days_compile_regex.search(unit_origin).group(1)
        except:
            ten_days = 0
        try:
            week = week_compile_regex.search(unit_origin).group(1)
        except:
            week = 0
        try:
            fif_days = fif_days_compile_regex.search(unit_origin).group(1)
        except:
            fif_days = 0
        try:
            day = day_compile_regex.search(unit_origin).group(1)
        except:
            day =0
        try:
            hour = hour_compile_regex.search(unit_origin).group(1)
        except:
            hour = 0
        try:
            quarter_hour = quarter_hour_compile_regex.search(unit_origin).group(1)
        except:
            quarter_hour = 0
        try:
            minute = minute_compile_regex.search(unit_origin).group(1)
        except:
            minute=0
        try:
            second = second_compile_regex.search(unit_origin).group(1)
        except:
            second = 0
        days = int(year) * 365 + int(quarter) * 30 * 4 + int(month) * 30 + int(fif_days) * 15 + int(ten_days) * 10 + int(day)
        minutes = int(quarter_hour) * 15 + int(minute)
        try:
            datetime_formate = datetime.timedelta(days=days, seconds=int(second), minutes=minutes,hours=int(hour), weeks=int(week)).total_seconds()
            datetime_formates.append(datetime_formate)
        except Exception as err:
            print("%s %s"%(err.args, unit_origin))

    return datetime_formates

def formates_timepoint(formate_time):
    year_regex = r"(\d+)年.*[前后]"
    year_compile_regex = re.compile(year_regex)

    quarter_regex  = r"(\d+)季.*[前后]"
    quarter_compile_regex = re.compile(quarter_regex)

    month_regex = r"(\d+)[个]?月.*[前后]"
    month_compile_regex = re.compile(month_regex)

    ten_days_regex = r"(\d+)旬.*[前后]"
    ten_days_compile_regex = re.compile(ten_days_regex)

    week_regex =  r"(\d+)(?:周|礼拜).*[前后]"
    week_compile_regex = re.compile(week_regex)

    fif_days_regix=  r"(\d+)候.*[前后]"
    fif_days_compile_regex = re.compile(fif_days_regix)

    day_regex = r"(\d+)[天日].*[前后]"
    day_compile_regex = re.compile(day_regex)

    hour_regex = r"(\d+)[个]?[小]时.*[前后]"
    hour_compile_regex = re.compile(hour_regex)

    quarter_hour_regex=r"(\d+)刻[钟]?.*[前后]"
    quarter_hour_compile_regex = re.compile(quarter_hour_regex)

    minute_regex = r"(\d+)分[钟]?.*[前后]"
    minute_compile_regex = re.compile(minute_regex)

    second_regex = r"(\d+)秒.*[前后]"
    second_compile_regex = re.compile(second_regex)

    times,units = time_convert(formate_time)
    convert_dates = num_convert(times,units)
    datetime_formates = []
    for i,unit_origin in enumerate(convert_dates):

        try:
            year = year_compile_regex.search(unit_origin).group(1)
        except:
            year = 0
        try:
            quarter = quarter_compile_regex.search(unit_origin).group(1)
        except:
            quarter = 0
        try:
            month = month_compile_regex.search(unit_origin).group(1)
        except:
            month = 0
        try:
            ten_days = ten_days_compile_regex.search(unit_origin).group(1)
        except:
            ten_days = 0
        try:
            week = week_compile_regex.search(unit_origin).group(1)
        except:
            week = 0
        try:
            fif_days = fif_days_compile_regex.search(unit_origin).group(1)
        except:
            fif_days = 0
        try:
            day = day_compile_regex.search(unit_origin).group(1)
        except:
            day =0
        try:
            hour = hour_compile_regex.search(unit_origin).group(1)
        except:
            hour = 0

        try:
            quarter_hour = quarter_hour_compile_regex.search(unit_origin).group(1)
        except:
            quarter_hour = 0
        try:
            minute = minute_compile_regex.search(unit_origin).group(1)
        except:
            minute=0
        try:
            second = second_compile_regex.search(unit_origin).group(1)
        except:
            second = 0
        days = int(year) * 365 + int(quarter) * 30 * 4 + int(month) * 30 + int(fif_days) * 15 + int(ten_days) * 10 + int(day)
        minutes=int(quarter_hour)*15+int(minute)

        if '前'in unit_origin:
            try:
                datetime_formate = (datetime.datetime.now() - datetime.timedelta(days=days, seconds = int(second), minutes = int(minutes), hours = int(hour), weeks = int(week))).strftime("%Y-%m-%d %H:%M:%S")
                datetime_formates.append(datetime_formate)
            except Exception as err:
                print("%s %s"%(err.args, unit_origin))
        elif '后'in unit_origin:
            try:
                datetime_formate = (datetime.datetime.now() + datetime.timedelta(days=days, seconds = int(second), minutes = int(minutes), hours = int(hour), weeks = int(week))).strftime("%Y-%m-%d %H:%M:%S")
                datetime_formates.append(datetime_formate)
            except Exception as err:
                print("%s %s"%(err.args, unit_origin))
        else:
            y = IntegerParse()
            test_dig = times[i]
            a =y.testdig(test_dig)
            try:
                datetime_formate=str(datetime.datetime(*map(int,a)))
                datetime_formates.append(datetime_formate)
            except Exception as err:
                print("%s %s"%(err.args, a))

    return datetime_formates

if __name__ == "__main__":
    formate_time = ["三天","三周","30分钟","三个礼拜","一小时1分钟2秒","1刻钟", "一刻钟","15分钟","十五分钟","拾伍分钟"]
    x = formates_duration(formate_time)
    print(x)

    formate_time = ["一九九九年八月十八日八点", "三天前", "三周前", "一刻钟之前", "一刻钟之后", "2018年9月18日", "二〇一四年八月十七日"]
    x = formates_timepoint(formate_time)
    print(x)
