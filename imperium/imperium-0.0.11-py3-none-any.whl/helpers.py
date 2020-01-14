from datetime import datetime, timedelta
import re

def exists(key, subject):
    split = key.split('.')
    for i, value in enumerate(split):
        if i == 0 and value == '$subject' or value == 'subject':
            continue

        if not value in subject:
            return False
        
        subject = subject[value]
    
    return True

def matches(expr, subject, flag=None):
    if flag is not None:
        flag = flag.lower()
        if flag == 'i':
            result = re.match(expr, subject, re.IGNORECASE)
        elif flag == 'm':
            result = re.match(expr, subject, re.MULTILINE)
    else:
        result = re.match(expr, subject)

    if result:
        return True
    else:
        return False

def date(string=None, format='%Y-%m-%d'):
    if string is not None:
        return datetime.strptime(string, format)

    return datetime.now()

def date_modify(date, operation, valuetype, value):
    operation = operation.lower()
    if operation == 'subtract' or operation == '-':
        if valuetype == 'days' or valuetype == 'day':
            return date - timedelta(days=int(value))
        if valuetype == 'months' or valuetype == 'month':
            return date - timedelta(days=int(value) * 30)
        if valuetype == 'years' or valuetype == 'year':
            return date - timedelta(days=int(value) * 365)

    if operation == 'add' or operation == '+':
        if valuetype == 'days' or valuetype == 'day':
            return date + timedelta(days=int(value))
        if valuetype == 'months' or valuetype == 'month':
            return date + timedelta(days=int(value) * 30)
        if valuetype == 'years' or valuetype == 'year':
            return date + timedelta(days=int(value) * 365)

    return date