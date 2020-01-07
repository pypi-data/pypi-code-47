Hitam = '\033[30m'
Merah = '\033[31m'
Hijau = '\033[32m'
Kuning = '\033[33m'
Biru = '\033[34m'
Ungu = '\033[35m'
Cyann = '\033[36m'
Putih = '\033[37m'
B = '\033[1m'

def Black(string):
    return Hitam + string + '\033[m'

def Red(string):
    return Merah + string + '\033[m'

def Green(string):
    return Hijau + string + '\033[m'

def Yellow(string):
    return Kuning + string + '\033[m'

def Blue(string):
    return Biru + string + '\033[m'

def Purple(string):
    return Ungu + string + '\033[m'

def Cyan(string):
    return Cyann + string + '\033[m'

def White(string):
    return Putih + string + '\033[m'

def Bold(string):
    return B + string + '\033[m'

# set the background 

def bgBlack(string):
    return '\033[40m' + string + '\033[m'

def bgRed(string):
    return '\033[41m' + string + '\033[m'

def bgGreen(string):
    return '\033[42m' + string + '\033[m'

def bgYellow(string):
    return '\033[43m' + string + '\033[m'

def bgBlue(string):
    return '\033[44m' + string + '\033[m'

def bgPurple(string):
    return '\033[45m' + string + '\033[m'

def bgCyan(string):
    return '\033[46m' + string + '\033[m'

def bgWhite(string):
    return '\033[47m' + string + '\033[m'