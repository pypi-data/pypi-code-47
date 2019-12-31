import jinja2
import logging

from xhtml2pdf import pisa
from cliff.command import Command
from tracklr import Tracklr
from jinja2 import Template
from jinja2.exceptions import TemplateNotFound


class Pdf(Command):

    log = logging.getLogger(__name__)

    tracklr = Tracklr()

    __template__ = """
<html>
  <header>
    <title>{{ tracklr.title }} {{ tracklr.subtitle }}</title>
    <style>
    table {
        font: 12px Verdana, Arial, Helvetica, sans-serif;
        width: 1200px;
    }

    th {
        padding: 0.5em 0.5em 0;
        border-bottom: 3px solid #555;
    }
    th.date {
        text-align: left;
        width: 100px;
    }
    th.summary {
        text-align: left;
        width: 1000px;
    }
    th.hours {
        text-align: right;
        width: 100px;
    }

    td {
        border-bottom: 1px solid #CCC;
        padding: 0.25em 0.5em 0;
        vertical-align: top;
    }
    td.tag {
        text-align: left;
        width: 100px;
    }
    td.date {
        text-align: left;
        width: 100px;
    }
    td.summary {
        text-align: left;
        width: 1000px;
    }
    td.hours {
        text-align: right;
        width: 100px;
    }
    tr.total {
        border-top: 2px solid #555;
        font-weight: bold;
    }
    </style>
  </header>
  <body>
    <h1>{{ tracklr.title }} - {{ tracklr.subtitle }}</h1>
    <table>
      {% if tracklr.tags %}
      <tr>
        <th class="date">Tag</th>
        <th class="hours">Hours</th>
      </tr>
        {% for item in tracklr.report_html %}
      <tr>
        <td class="tag">{{ item.0 }}</td>
        <td class="hours">{{ item.1 }}</td>
      </tr>
        {% endfor %}
      <tr class="total">
        <td>Total</td>
        <td class="hours">{{ tracklr.total_hours }}</td>
      </tr>
      {% else %}
      <tr>
        <th class="date">Date</th>
        <th class="summary">Summary</th>
        <th class="hours">Hours</th>
      </tr>
        {% for item in tracklr.report_html %}
      <tr>
        <td class="date">{{ item.0 }}</td>
        <td class="summary">
        {% if item.2 != "" %}
          {{ item.2 }}
        {% endif %}
        {% if item.4 not in item.2 %}
          {% if item.2 != "" %}
          <br />
          {% endif %}
          {{ item.4 }}
        {% endif %}
        </td>
        <td class="hours">{{ item.3 }}</td>
      </tr>
        {% endfor %}
      <tr class="total">
        <td colspan="2">Total</td>
        <td class="hours">{{ tracklr.total_hours }}</td>
      </tr>
      {% endif %}
    </table>
  </body>
</html>
        """

    def take_action(self, parsed_args):
        """Generates report as a PDF file.
        """
        cal = self.tracklr.get_calendar_config(parsed_args.kalendar)
        self.tracklr.get_calendar(cal["name"])

        if parsed_args.report == "tag":
            self.tracklr.get_tags(
                parsed_args.kalendar,
                parsed_args.date,
                parsed_args.include,
                parsed_args.exclude,
            )
        else:
            self.tracklr.get_report(
                parsed_args.kalendar,
                parsed_args.date,
                parsed_args.include,
                parsed_args.exclude,
            )

        self.tracklr.get_title(cal["name"], parsed_args.title)
        self.tracklr.get_subtitle(cal["name"], parsed_args.subtitle)

        in_html = self.generate_html()

        out_pdf = self.tracklr.get_pdf_output_file(parsed_args.file)

        titles = self.tracklr.get_titles(
            parsed_args.kalendar, parsed_args.title, parsed_args.subtitle
        )
        self.log.info(
            "Generating...\n{}\nOutput file: {}".format(titles, out_pdf)
        )

        self.generate_pdf(in_html, out_pdf)

    def get_description(self):
        """creates PDF report"""
        return "creates PDF report"

    def get_parser(self, prog_name):
        """Defines the following input arguments for ``pdf`` command:

        * ``-f`` ``--file`` destination of the pdf file
        * ``-r`` ``--report`` {ls, tag} pdf of ``ls`` (default) or ``tag``
        """
        parser = super(Pdf, self).get_parser(prog_name)
        parser.add_argument("-f", "--file")
        parser.add_argument("-r", "--report", type=str, choices=["ls", "tag"])
        return self.tracklr.get_parser(parser)

    def generate_html(self):
        """Generates HTML version"""
        try:
            loader = jinja2.FileSystemLoader(
                searchpath=self.tracklr.template_path
            )
            env = jinja2.Environment(loader=loader)
            template = env.get_template(self.tracklr.pdf_template_file)
            self.log.info("Template: {}".format(self.tracklr.pdf_template_file))
            return template.render(tracklr=self.tracklr)
        except TemplateNotFound:
            template = Template(self.__template__)
            self.log.info("Template: internal")
            return template.render(tracklr=self.tracklr)

    def generate_pdf(self, in_html, out_pdf):
        """Generates PDF from HTML version"""
        report_file = open(out_pdf, "w+b")
        status = pisa.CreatePDF(in_html, dest=report_file)
        report_file.close()
