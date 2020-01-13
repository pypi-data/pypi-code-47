from sys import argv
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, exists
from builtins import input
from protect_rm.config import Config


c = Config()

# print the 
def pprint(msg):
    global c
    print(c.protect_prefix + msg)

def ask_in(q, a):
    return bool(input(q) in a)

def protect(protect_args=None):
    global c
    flags = ''
    multi_flags = False
    option_end = False
    if not protect_args:
        protect_args = argv[1:]
    if (protect_args[0].startswith("-")):
        if (len(protect_args[1:]) > 1):
            pprint("Looks you have multiple files or directories")
            if ask_in(q="Set all file protection with same profile? (y/n) ", a="Yesyes"):
                multi_flags = True
                global_question = input("Global question for all files/directories: ")
                global_answer = input("Global answer: ")
            else:
                pprint("Profiles will be customized for each file or directory.")
    elif (len(protect_args) > 1):
        pprint("Looks you have multiple files or directories")
        if ask_in(q="Set all file protection with same profile? (y/n) ", a="Yesyes"):
            multi_flags = True
            global_question = input("Global question for all files/directories: ")
            global_answer = input("Global answer: ")
        else:
            pprint("Profiles will be customized for each file or directory.")
    for arg in protect_args:
        if arg == '--':
            option_end = True
        elif (arg.startswith("-") and not option_end):
            flags = flags + arg[arg.rfind('-') + 1:]
        elif arg in c.invalid:
            pprint('"." and ".." may not be protected')
        else:
            path = abspath(expv(expu(arg)))
            evalpath = dirname(path) + "/." + basename(path) + c.suffix
            if not exists(path):
                pprint("Warning: " + path + " does not exist")
            with open(evalpath, "w") as f:
                if multi_flags:
                    f.write(global_question + "\n" + global_answer + "\n" + flags.upper())
                else:
                    question = input("Question for " + path + ": ")
                    answer = input("Answer: ")
                    f.write(question + "\n" + answer + "\n" + flags.upper())


if __name__ == "__main__":
    protect()
