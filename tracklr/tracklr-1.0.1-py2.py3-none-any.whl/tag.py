import logging

from cliff.lister import Lister
from tracklr import Tracklr


class Tag(Lister):

    log = logging.getLogger(__name__)

    tracklr = Tracklr()

    def take_action(self, parsed_args):
        """Generates report and logs total number of hours.
        """
        ts = self.tracklr.get_tags(
            parsed_args.kalendar,
            parsed_args.date,
            parsed_args.include,
            parsed_args.exclude,
        )

        titles = self.tracklr.get_titles(
            parsed_args.kalendar, parsed_args.title, parsed_args.subtitle
        )
        self.log.info(titles)
        self.log.info("Total hours: {}".format(self.tracklr.total_hours))

        return (("Tag", "Hours"), ts)

    def get_description(self):
        return "creates tagged report"

    def get_parser(self, prog_name):
        parser = super(Tag, self).get_parser(prog_name)
        return self.tracklr.get_parser(parser)
