from colorama import Fore, Style, init

init()


def print_red(text):
  print(F'{Fore.RED}{text}{Style.RESET_ALL}')


def print_green(text):
  print(F'{Fore.GREEN}{text}{Style.RESET_ALL}')
