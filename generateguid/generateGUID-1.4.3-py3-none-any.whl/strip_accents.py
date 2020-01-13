#!/usr/bin/python
import unicodedata
import re
import datetime
# Function to remove special characters and convert
# them in lower case from typical french names

from itertools import compress


def format_age(age, length_year=4):

    if length_year == 4:
        format_date = r'%d%m%Y'
    elif length_year == 2:
        format_date = r'%d%m%y'

    delim_list = ['-', '/', r"\\", ' ']
    delim_age = [delim in age for delim in delim_list]
    if any(delim_age):
        list_delim = list(compress(delim_list, delim_age))
        assert len(list_delim) < 3, "More than two delim in age:{}".format(
            list_delim)

        if len(list_delim) == 1:
            list_delim = list_delim + list_delim

        if re.match(r"^[0-9]{2}\D", age):
            format_strp = r'%d{}%m{}%Y'.format(*list_delim)
        elif re.match(r"^[0-9]{4}\D", age):
            format_strp = r'%Y{}%m{}%d'.format(*list_delim)
        date_time_obj = datetime.datetime.strptime(str(age), format_strp)
        date_time_obj = date_time_obj.strftime(format_date)

    else:
        date_time_obj = age

    return date_time_obj


def strip_accents(text):
    """
    Strip accents from input String.
    :param text: The input string.
    :type text: String.
    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError):  # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def text_to_id(text):
    """
    Convert input text to id.
    :param text: The input string.
    :type text: String.
    :returns: The processed String.
    :rtype: String.
    """

    text = strip_accents(text)
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    text = re.sub('-', '', text)
    text = re.sub('_', '', text)
    text = text.replace(r'\/', '')
    text = text.replace(r'\\', ' ')
    return text.upper()
