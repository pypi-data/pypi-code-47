"""
Created by adam on 11/11/19
"""
__author__ = 'adam'

"""
These are classes for helping to save statistical data like tables and charts into html, image, and pdf files. They take a dataframe as an input.
"""
from pandas import DataFrame
import codecs
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date

class StatSaver:
    @staticmethod
    def save(PATH, FILENAME, dataframe_w_content, table_title=None):
        """
        This will save a dataframe as a formatted table in an html file
        @param PATH The path to the folder into which the stats will be saved. Should NOT end in '/'
        @param FILENAME The name to give the saved file. The date will automatically be appended
        @param dataframe_w_content A pandas dataframe object containing the content to save
        @param table_title Optional title to add to the table in the file
        """
        today = date.isoformat(date.today())
        head = """<html><head>
			<style type="text/css">
				table.nowrap {
					margin-right: 80px;
				}
				table.dataframe {
					margin-right: 80px;
				}
				table{
				font-size:24;
				height:300px;
				width:500px;
				}
			</style></head>
			<body>
			<h1>%s</h1>
			<h1>%s</h1>""" % (table_title, FILENAME)
        tail = """<h3>%s</h3></body></html>""" % today
        content = dataframe_w_content.to_html()
        page = head + content + tail
        path = '%s/%s_%s' % (PATH, today, FILENAME)
        outfile = codecs.open(path, mode='w', encoding='utf-8', errors='html_replace')
        outfile.write(page)
        outfile.close()

class ChartSaver:
    """
    This is used to save chart data
    """
    @staticmethod
    def pdf(PATH, CHARTNAME, chartsize=(18.5,10.5)):
        """
        This saves a chart as a pdf. It is called after a chart has been plotted
        @param PATH The path to the folder into which the stats will be saved. Should NOT end in '/'
        @param CHARTNAME The name to give the saved file. The date will automatically be appended
        """
        today = date.isoformat(date.today())
        filepath = '%s/%s_%s' % (PATH, today, CHARTNAME)
        pp = PdfPages(filepath)
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(chartsize[0], chartsize[1])
        pp.savefig(fig)
        pp.close()