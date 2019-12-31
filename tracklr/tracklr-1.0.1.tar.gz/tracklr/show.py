import jinja2
import logging

from xhtml2pdf import pisa
from cliff.command import Command
from tracklr import Tracklr
from jinja2 import Template
from jinja2.exceptions import TemplateNotFound


class Show(Command):

    log = logging.getLogger(__name__)

    tracklr = Tracklr()

    def take_action(self, parsed_args):
        """Show configuration details.
        """
        cal = self.tracklr.get_calendar_config(parsed_args.kalendar)
        self.tracklr.get_calendar(cal["name"])

        self.tracklr.get_title(cal["name"], parsed_args.title)
        self.tracklr.get_subtitle(cal["name"], parsed_args.subtitle)

        calendars = []
        for cal in self.tracklr.calendars:
            calendars.append(
                "- {} | {} | {}\n".format(
                    cal,
                    self.tracklr.get_title(cal, parsed_args.title),
                    self.tracklr.calendars[cal]["location"],
                )
            )

        self.app.stdout.write("    __                        __    __\n")
        self.app.stdout.write(
            "  _/  |_____________    ____ |  | _|  |_______\n"
        )
        self.app.stdout.write(
            "  \   __\_  __ \__  \ _/ ___\|  |/ /  |\_  __ \ \n"
        )
        self.app.stdout.write(
            "   |  |  |  | \// __ \\\  \___|    <|  |_|  | \/\n"
        )
        self.app.stdout.write("   |__|  |__|  (____  /\___  >__|_ \____/__|\n")
        self.app.stdout.write(
            "                    \/     \/     \/     v{}\n".format(
                self.tracklr.__version__
            )
        )
        self.app.stdout.write(
            "\n{} - {}\n".format(self.tracklr.title, self.tracklr.subtitle)
        )
        self.app.stdout.write(
            "\nLoaded Config File: {}\n".format(self.tracklr.loaded_config_file)
        )
        self.app.stdout.write("\nCalendars:\n\n{}".format("".join(calendars)))
        self.app.stdout.write("\n\n")

    def get_description(self):
        return "shows info about current instance"

    def get_parser(self, prog_name):
        parser = super(Show, self).get_parser(prog_name)
        parser.add_argument("-f", "--file")
        return self.tracklr.get_parser(parser)
