#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'bee'
import unicodecsv as csv
from django.http import StreamingHttpResponse

# 导出csv
def export_csv(filename, headers, rows):
    response = StreamingHttpResponse((row for row in csv_itertor(headers, rows)), content_type="text/csv;charset=utf-8")
    response['Content-Disposition'] = 'attachment;filename="' + filename + '.csv"'
    return response


def csv_itertor(headers, rows):
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    yield writer.writerow(headers)
    for column in rows:
        yield writer.writerow(column)


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


# 完