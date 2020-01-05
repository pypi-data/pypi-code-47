from . import docopt_parser, explainshell_parser, naive_parser

_name_to_parser = {
    "docopt": docopt_parser.DocoptParser,
    "explainshell": explainshell_parser.ExplainShellParser,
    "naive": naive_parser.NaiveParser
}

class ParametersExtractor():

    def __init__(self, cmd, parsers_to_use):
        self.parsers = []
        self.options = []
        self.arguments = []
        self.commands = []
        self._init_parser(cmd, parsers_to_use)
        self._extract_parameters()

    def _init_parser(self, cmd, parsers_to_use):
        """
        Create the parsers according the option passed in the command line
        """
        for parser in parsers_to_use.strip('\"').strip('\'').split(','):
            parser_constructor = _name_to_parser[parser.strip()]
            self.parsers.append(parser_constructor(cmd))

    def _extract_parameters(self):
        """
        Extract the options, arguments and subcommands from each parser
        """
        for parser in self.parsers:
            self._extract_info(self.options, parser.options, self._are_same_options)
            self._extract_info(self.arguments, parser.arguments, self._are_same_arguments)
            self._extract_info(self.commands, parser.commands, self._are_same_commands)

    def _extract_info(self, current_info_list, new_info_list, are_same_info):
        """
        Update the current options, arguments and subcommands info with a
         parser info
        """
        info_to_add = []
        for new_info in new_info_list:
            is_update = False
            for current_info in current_info_list:
                if are_same_info(current_info, new_info):
                    current_info.update(new_info)
                    is_update = True
                    break
            if not is_update:
                info_to_add.append(new_info)
        current_info_list.extend(info_to_add)

    def _are_same_options(self, option1, option2):
        """
        Return True iif the 2 options represents the same option
        """
        if len(option1['names']) == len(option2['names']):
            for name in option1['names']:
                if not name in option2['names']:
                    return False
            return True
        else:
            return False

    def _are_same_arguments(self, arg1, arg2):
        """
        Return True iif the 2 arguments represents the same argument
        """
        return arg1['name'] == arg2['name']

    def _are_same_commands(self, subcmd1, subcmd2):
        """
        Return True iif the 2 subcommands represents the same subcommand
        """
        return subcmd1['name'] == subcmd2['name']
