
def print_error(text):
    text = str(text)
    if not text.startswith('[!] '):
        text = '[!] ' + text
    text = '\033[1;31m' + text + '\033[0;0m'
    print(text)

def print_warning(text):
    text = str(text)
    if not text.startswith('[#]'):
        text = '[#] ' + text
    text = '\033[1;33m' + text + '\033[0;0m'
    print(text)