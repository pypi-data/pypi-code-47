# coding=utf-8
from __future__ import print_function, unicode_literals

from abc import ABCMeta
from subprocess import PIPE, Popen

import six
from termcolor import colored

CONSUELA = """
                                    ,▄▄▄▄▄▄,                                     
                        ,▄▄▄▄▄▄▄▄▄▓▓▓▓▓▓▓▓▓▓▓▄▄▄▄▄▄▄▄▄╓                         
                    ╓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄                     
                  ,▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄                   
                 ╔▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄                  
                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⌐                 
                ╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
          ▒,▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀░░░╨▀▀░░░░▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄ ╔             
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▄⌐           
          ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▀░░░░░░░░░░░░░░░░░░▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀            
           '▓▓▓▓▓▓▓▓▓▓▓▀░░░░░░░░░░░░░░░░░░░░░░░▀▀▓▓▓▓█╬▀▀▓▓▓▓▓▓▓▓▓▓,            
     @▄╥▄▄▓▓▓▓▓▓▓▓▓▓▓▓▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▄▄╥▄▄⌐    
     ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▀▀▀▓▓▓▓▓▓▌▀▀▀▀▄░░░½▒▀▀▀▀▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░╫▓▀▀▀▀▀▓▌Q░░▓░░░╫╬░░Q▓▓▀▀▀▀▓▓▄░░░▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀     
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀░░▓▀░░░░░░░░▀▌░▓░░░╫╬░▒▀░░░░░░░░▀▌░░▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌      
        ▀▓▓▓▓▓▓▓▓▓▓▓▌φ▓▓▓▄▄▄▄▄▄▄▄▄▄▓Ö▓╬░Å▓╬▐▓▄▄▄▄▄▄▄▄▄▄▓▓▀▐▓▓▓▓▓▓▓▓▓▓▓▓▓╨       
          ▀▓▓▓▓▓▓▌▄▐▌░░╫▌    █▀    ▓▐▓░░░▐▌╙▓    ▀▀    ▓░░ü▓░▒╬▓▓▓▓▓▓▀╙         
             ▓▓▓▓▒▓▒▌░░░▀▌,      ╓▓▒▓░░░░░▀▄╫▓╓      ,▓▀░░▐▓▐▌▄▓▓▓▌             
             ╟▓▓▓╠╬▓▓░░░░░▀▀▀▒▒▀▀╬▓░░░░░░░░░╬▌Å▀▒▒▒▒▀░░░░░╫▌▓░░▓▓▓▓             
              ▓▓▓▓▓▌░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌▀▄░░░░▒▀▓▀▀▀▀▀▀▀▀▀▀▀▀▀░░▓▓▓▓▓▓█             
               ▓▓▓▓▓░░░░░░░░░░░░░░▒░░╨▀▄▒▀░░▀▒░░░░░░░░░░░░░▄▓▓▓▓▓¬              
               ]▓▓▓▓▓░░░░░░░░░░░▄▀░░░░░░░░░░░▐▀Q░░░░░░░░░░▓▓▓▓▓▓▓               
              ,▓▓▓▓▓▓▓▄░░░░░░░▄╬░▄▄▒█▒▄▄▄▄▒▒▄▄░▀▒░░░░░░░▐▓▓▓▓▓▓▓▓               
             ╙▀╙,▓▓▓▓▀▀▌░░░░½▒▄▄▓▓▌▌▒▒╬▒▒╬▒▌▌▓▓▓▄▀▌░░░░░▓▀▓▓▓▓▄ └               
                ╙` ▓╬░░▓▄░░░▓▀░Å▀▓▒▒╬▀▀▀▀▀▒╬╬▒▓▀▀▀▀▌░░░½▌░▐▓                    
                   ▐▌░░░▓░░░▀░░░░░░Å▀▀▀▀▀▀▀▀▀░░░░░░▀░░░▓░░╫▌                    
                    ▀▄░░╫▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░╠▓                     
                     ▀▌░░░▀▀▒▄▄▄░▀▀██▄▄▄▄▄▄▄██▀░░▒▒▒▒▀░░▄▓                      
                      ^▓▄░░░░░░▀▀▄▄░░░░░░░░░Q▄▄▒▀░░░░░░▒▀                       
                        ╙▓▄░░░░░░░╬▀▌Q░░░░▄▀░░░░░░░░░░▓╨                        
                          ╙▓▄░░░░░▄▀▀▀▓░½▓▓▄▄░░░░░░░▄▀                          
                            ╙█▄░▐▓    ^▓▌   ^▀█▄░░░▓▀                           
                               ▀▓Γ     ╙       ▀▒▒▀  
    """


@six.add_metaclass(ABCMeta)
class BaseCommand:
    name = None
    error = None
    message = None
    status = None

    def __init__(self):
        pass

    @staticmethod
    def get_command():
        raise NotImplementedError

    def run(self):
        proc = Popen(self.get_command(), stdout=PIPE, stderr=PIPE)
        self.status = proc.wait()

        if self.status != 0:
            self.error = proc.stderr.read()

        self.message = proc.stdout.read()
        return proc


class BaseChecker(BaseCommand):
    def check(self):
        print('- {} \t ... '.format(self.name), end='')
        self.run()


class BaseFormatter(BaseCommand):
    def format(self):
        print('- {} \t ... '.format(self.name), end='')
        self.run()


class BlackBaseChecker(BaseChecker):
    name = 'Black'

    def get_command(self):
        return ["black", '.']


class Flake8BaseChecker(BaseChecker):
    name = 'Flake8'

    def get_command(self):
        return ["flake8", '.']


class ISortBaseChecker(BaseChecker):
    name = 'ISort'

    def get_command(self):
        return ["isort", '--check', '--diff']


class RadonBaseChecker(BaseChecker):
    name = 'Radon'

    @staticmethod
    def get_command():
        return ["radon", "cc", ".", "-a", "-ncc"]


class VultureBaseChecker(BaseChecker):
    name = 'Vulture'

    @staticmethod
    def get_command():
        return ["vulture", ".", "--min-confidence 100"]


class ISortFormatter(BaseFormatter):
    name = 'ISort'

    @staticmethod
    def get_command():
        return ['isort', '-y']


class BlackFormatter(BaseFormatter):
    name = 'Black'

    @staticmethod
    def get_command():
        return ['black', '.']


class Consuela:
    check_errors = None
    format_errors = None
    checkers = [
        Flake8BaseChecker,
        BlackBaseChecker,
        ISortBaseChecker,
        RadonBaseChecker,
        VultureBaseChecker,
    ]

    formatters = [ISortFormatter, BlackFormatter]

    def __init__(self):
        self.check_errors = {}

    def get_checkers(self):
        return [ch() for ch in self.checkers]

    def get_formatters(self):
        return [ch() for ch in self.formatters]

    def check(self, single=True):
        if single:
            print("\nConsuela started check ...\n")
        for checker in self.get_checkers():
            checker.check()
            if checker.error:
                self.add_error(checker.name, checker.error)
                print(colored('Fail!', 'red'))
            else:
                print(colored('Success!', 'green'))

        if single:
            self.exit()

    def format(self, single=True):
        if single:
            print("\nConsuela started format ...\n")
        for formatter in self.get_formatters():
            formatter.format()
            if formatter.error:
                self.add_error(formatter.name, formatter.error)
                print(colored('Fail!', 'red'))
            else:
                print(colored('Success!', 'green'))

        if single:
            self.exit()

    def format_and_check(self):
        print(CONSUELA)
        print("\nConsuela started working ...")
        print("Format:\n")
        self.format(single=False)
        print("\nCheck:\n")
        self.check(single=False)

        self.exit()

    def exit(self):
        check_error = self.get_check_error()
        format_error = self.get_format_error()
        if check_error or format_error:
            print(colored("\nNo, no, no ...\nSee also:\n", 'red'))
            print(colored(str(check_error or ''), 'red'))
            print(colored(str(format_error or ''), 'red'))

            raise SystemExit(1)

    def get_check_error(self):
        error = ""
        for util_name, util_error in (self.check_errors or {}).items():
            error = error + "------------------ Start {} ---------------------".format(
                util_name
            )
            error = "{}\n{}: {}".format(error, util_name, util_error)

        if error:
            error = (
                "CHECKS ERRORS: \n"
                + error
                + "-------------------------------------------------"
            )

        return error or None

    def get_format_error(self):
        error = ""
        for util_name, util_error in (self.format_errors or {}).items():
            error = error + "------------------ Start {} ---------------------".format(
                util_name
            )
            error = "{}\n{}: {}".format(error, util_name, util_error)

        if error:
            error = (
                "FORMAT ERRORS: \n"
                + error
                + "-------------------------------------------------"
            )

        return error or None

    def add_error(self, util, error):
        self.check_errors[util] = error


if __name__ == '__main__':
    Consuela().format_and_check()
