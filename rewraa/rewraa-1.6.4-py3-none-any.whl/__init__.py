# Copyright (c) 2017 Javad Shafique All rigths reserved

import random
import threading
import socket
import string
import os
import time
import platform
import json
import operator
from difflib import SequenceMatcher
import base64
import binascii
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import re, sys
from functools import partial
import json

sys = os.sys
_exit = os._exit
environ = os.environ


# ../src/lib/aes.py START #


"""
Here is a bunch of decoding/encoding functions for diffrent things
"""
# encode unicode to hex
def hex_encode(string):
    # and return ascii string
    return binascii.hexlify(str(string).encode("unicode_escape")).decode("ascii")

# decode ascii encoded hex string to unicode
def hex_decode(string):
    # convert to bytes
    string = string.encode()
    # decode hex and unicode
    return binascii.unhexlify(string).decode("unicode_escape")

# base64 encoding and decoding with unicode
def b64_encode(string):
    return base64.b64encode(str(string).encode("unicode_escape")).decode("ascii")

def b64_decode(string):
    # convert to bytes
    string = string.encode()
    return base64.b64decode(string).decode("unicode_escape")


# and the ones we a using
encode = b64_encode
decode = b64_decode

# aes encryption class. 
# used for encrypting data 
# have a encrypt and decrypt
# function.

"""
Aes encryption class
"""

class aes:
    # define error
    class InvalidBlockSizeError(Exception):
        """Raised for invalid block sizes"""
        pass

    # constuctor takes key
    def __init__(self, key):
        # pad key
        key = key.zfill(32)
        # convert key to bytes
        self.key = key[0:32].encode()
   
    # padding
    def __pad(self, text):
        amount_to_pad = AES.block_size - (len(text) % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    # remove padding
    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    # encrypt data
    def encrypt(self, data):
        # pad and convert to bytes
        raw = self.__pad(data).encode()
        # init cipher
        # but first create iv
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # return base64 encrypted bytes
        return base64.b64encode(iv + cipher.encrypt(raw))

    # decrypt
    def decrypt(self, enc):
        # decode encrypted string
        enc = base64.b64decode(enc)
        # init cipher
        # first extract iv
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # unpad the decrypted bytes that we convert to utf-8
        return self.__unpad((cipher.decrypt(enc[AES.block_size:]).decode("utf8")))

"""
e = encode("Javad NANE IS LOL")
print(e, decode(e))

||||||||||||||||||||||

msg = input("Message: ")
pwd = input("Password: ")
a = aes(pwd)
e = a.encrypt(msg)
d = a.decrypt(e)

print("Encrypted:", e)
print("Decrypted:", d)
"""

# ../src/lib/aes.py END #



# ../src/lib/rsa.py START #


class rsa:
    def __init__(self, bits = 4096, keys = None):
        if keys == None:
            self.keys = RSA.generate(bits, Random.new().read)
            self.pub = self.keys.publickey().exportKey()
            self.pem = self.keys.exportKey()
        else:
            self.keys = RSA.importKey(keys)
            self.pub = self.keys.publickey().exportKey()
            self.pem = self.keys.exportKey()

    def encrypt(self, data):
        return PKCS1_OAEP.new(self.keys.publickey()).encrypt(data.encode())

    def decrypt(self, encrypted):
        return PKCS1_OAEP.new(self.keys).decrypt(encrypted)

    #for encrypting with the public key only
    @staticmethod
    def _encrypt(data, public):
        return PKCS1_OAEP.new(RSA.importKey(public)).encrypt(data.encode())


# ../src/lib/rsa.py END #



# ../src/lib/colors.py START #

# Copyright (c) 2012 Giorgos Verigakis <verigak@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.



_PY2 = sys.version_info[0] == 2
string_types = basestring if _PY2 else str


"""
Main module
"""

# ANSI color names. There is also a "default"
COLORS = ('black', 'red', 'green', 'yellow', 'blue',
          'magenta', 'cyan', 'white')

# ANSI style names
STYLES = ('none', 'bold', 'faint', 'italic', 'underline', 'blink',
          'blink2', 'negative', 'concealed', 'crossed')


def is_string(obj):
    """
    Is the given object a string?
    """
    return isinstance(obj, string_types)


def _join(*values):
    """
    Join a series of values with semicolons. The values
    are either integers or strings, so stringify each for
    good measure. Worth breaking out as its own function
    because semicolon-joined lists are core to ANSI coding.
    """
    return ';'.join(str(v) for v in values)


def _color_code(spec, base):
    """
    Workhorse of encoding a color. Give preference to named colors from
    ANSI, then to specific numeric or tuple specs. If those don't work,
    try looking up CSS color names or parsing CSS color specifications
    (hex or rgb).

    :param str|int|tuple|list spec: Unparsed color specification
    :param int base: Either 30 or 40, signifying the base value
        for color encoding (foreground and background respectively).
        Low values are added directly to the base. Higher values use `
        base + 8` (i.e. 38 or 48) then extended codes.
    :returns: Discovered ANSI color encoding.
    :rtype: str
    :raises: ValueError if cannot parse the color spec.
    """
    if is_string(spec):
        spec = spec.strip().lower()

    if spec == 'default':
        return _join(base + 9)
    elif spec in COLORS:
        return _join(base + COLORS.index(spec))
    elif isinstance(spec, int) and 0 <= spec <= 255:
        return _join(base + 8, 5, spec)
    elif isinstance(spec, (tuple, list)):
        return _join(base + 8, 2, _join(*spec))
    else:
        rgb = parse_rgb(spec)
        # parse_rgb raises ValueError if cannot parse spec
        # or returns an rgb tuple if it can
        return _join(base + 8, 2, _join(*rgb))


def color(s, fg=None, bg=None, style=None):
    """
    Add ANSI colors and styles to a string.

    :param str s: String to format.
    :param str|int|tuple fg: Foreground color specification.
    :param str|int|tuple bg: Background color specification.
    :param str: Style names, separated by '+'
    :returns: Formatted string.
    :rtype: str (or unicode in Python 2, if s is unicode)
    """
    codes = []

    if fg:
        codes.append(_color_code(fg, 30))
    if bg:
        codes.append(_color_code(bg, 40))
    if style:
        for style_part in style.split('+'):
            if style_part in STYLES:
                codes.append(STYLES.index(style_part))
            else:
                raise ValueError('Invalid style "%s"' % style_part)

    if codes:
        template = '\x1b[{0}m{1}\x1b[0m'
        if _PY2 and isinstance(s, unicode):
            # Take care in PY2 to return str if str is given, or unicode if
            # unicode given. A pain, but PY2's fragility with Unicode makes it
            # important to avoid disruptions (including gratuitous up-casting
            # of str to unicode) that might trigger downstream errors.
            template = unicode(template)
        return template.format(_join(*codes), s)
    else:
        return s


def strip_color(s):
    """
    Remove ANSI color/style sequences from a string. The set of all possible
    ANSI sequences is large, so does not try to strip every possible one. But
    does strip some outliers seen not just in text generated by this module, but
    by other ANSI colorizers in the wild. Those include `\x1b[K` (aka EL or
    erase to end of line) and `\x1b[m`, a terse version of the more common
    `\x1b[0m`.
    """
    return re.sub('\x1b\\[(K|.*?m)', '', s)


def ansilen(s):
    """
    Given a string with embedded ANSI codes, what would its
    length be without those codes?
    """
    return len(strip_color(s))


# Foreground color shortcuts
black = partial(color, fg='black')
red = partial(color, fg='red')
green = partial(color, fg='green')
yellow = partial(color, fg='yellow')
blue = partial(color, fg='blue')
magenta = partial(color, fg='magenta')
cyan = partial(color, fg='cyan')
white = partial(color, fg='white')

# Style shortcuts
bold = partial(color, style='bold')
none = partial(color, style='none')
faint = partial(color, style='faint')
italic = partial(color, style='italic')
underline = partial(color, style='underline')
blink = partial(color, style='blink')
blink2 = partial(color, style='blink2')
negative = partial(color, style='negative')
concealed = partial(color, style='concealed')
crossed = partial(color, style='crossed')

"""
Css colors map
"""


css_colors = {
    'aliceblue':      (240, 248, 255),
    'antiquewhite':   (250, 235, 215),
    'aqua':           (0, 255, 255),
    'aquamarine':     (127, 255, 212),
    'azure':          (240, 255, 255),
    'beige':          (245, 245, 220),
    'bisque':         (255, 228, 196),
    'black':          (0, 0, 0),
    'blanchedalmond': (255, 235, 205),
    'blue':           (0, 0, 255),
    'blueviolet':     (138, 43, 226),
    'brown':          (165, 42, 42),
    'burlywood':      (222, 184, 135),
    'cadetblue':      (95, 158, 160),
    'chartreuse':     (127, 255, 0),
    'chocolate':      (210, 105, 30),
    'coral':          (255, 127, 80),
    'cornflowerblue': (100, 149, 237),
    'cornsilk':       (255, 248, 220),
    'crimson':        (220, 20, 60),
    'cyan':           (0, 255, 255),
    'darkblue':       (0, 0, 139),
    'darkcyan':       (0, 139, 139),
    'darkgoldenrod':  (184, 134, 11),
    'darkgray':       (169, 169, 169),
    'darkgreen':      (0, 100, 0),
    'darkgrey':       (169, 169, 169),
    'darkkhaki':      (189, 183, 107),
    'darkmagenta':    (139, 0, 139),
    'darkolivegreen': (85, 107, 47),
    'darkorange':     (255, 140, 0),
    'darkorchid':     (153, 50, 204),
    'darkred':        (139, 0, 0),
    'darksalmon':     (233, 150, 122),
    'darkseagreen':   (143, 188, 143),
    'darkslateblue':  (72, 61, 139),
    'darkslategray':  (47, 79, 79),
    'darkslategrey':  (47, 79, 79),
    'darkturquoise':  (0, 206, 209),
    'darkviolet':     (148, 0, 211),
    'deeppink':       (255, 20, 147),
    'deepskyblue':    (0, 191, 255),
    'dimgray':        (105, 105, 105),
    'dimgrey':        (105, 105, 105),
    'dodgerblue':     (30, 144, 255),
    'firebrick':      (178, 34, 34),
    'floralwhite':    (255, 250, 240),
    'forestgreen':    (34, 139, 34),
    'fuchsia':        (255, 0, 255),
    'gainsboro':      (220, 220, 220),
    'ghostwhite':     (248, 248, 255),
    'gold':           (255, 215, 0),
    'goldenrod':      (218, 165, 32),
    'gray':           (128, 128, 128),
    'green':          (0, 128, 0),
    'greenyellow':    (173, 255, 47),
    'grey':           (128, 128, 128),
    'honeydew':       (240, 255, 240),
    'hotpink':        (255, 105, 180),
    'indianred':      (205, 92, 92),
    'indigo':         (75, 0, 130),
    'ivory':          (255, 255, 240),
    'khaki':          (240, 230, 140),
    'lavender':       (230, 230, 250),
    'lavenderblush':  (255, 240, 245),
    'lawngreen':      (124, 252, 0),
    'lemonchiffon':   (255, 250, 205),
    'lightblue':      (173, 216, 230),
    'lightcoral':     (240, 128, 128),
    'lightcyan':      (224, 255, 255),
    'lightgoldenrodyellow': (250, 250, 210),
    'lightgray':      (211, 211, 211),
    'lightgreen':     (144, 238, 144),
    'lightgrey':      (211, 211, 211),
    'lightpink':      (255, 182, 193),
    'lightsalmon':    (255, 160, 122),
    'lightseagreen':  (32, 178, 170),
    'lightskyblue':   (135, 206, 250),
    'lightslategray': (119, 136, 153),
    'lightslategrey': (119, 136, 153),
    'lightsteelblue': (176, 196, 222),
    'lightyellow':    (255, 255, 224),
    'lime':           (0, 255, 0),
    'limegreen':      (50, 205, 50),
    'linen':          (250, 240, 230),
    'magenta':        (255, 0, 255),
    'maroon':         (128, 0, 0),
    'mediumaquamarine': (102, 205, 170),
    'mediumblue':     (0, 0, 205),
    'mediumorchid':   (186, 85, 211),
    'mediumpurple':   (147, 112, 219),
    'mediumseagreen': (60, 179, 113),
    'mediumslateblue': (123, 104, 238),
    'mediumspringgreen': (0, 250, 154),
    'mediumturquoise': (72, 209, 204),
    'mediumvioletred': (199, 21, 133),
    'midnightblue':   (25, 25, 112),
    'mintcream':      (245, 255, 250),
    'mistyrose':      (255, 228, 225),
    'moccasin':       (255, 228, 181),
    'navajowhite':    (255, 222, 173),
    'navy':           (0, 0, 128),
    'oldlace':        (253, 245, 230),
    'olive':          (128, 128, 0),
    'olivedrab':      (107, 142, 35),
    'orange':         (255, 165, 0),
    'orangered':      (255, 69, 0),
    'orchid':         (218, 112, 214),
    'palegoldenrod':  (238, 232, 170),
    'palegreen':      (152, 251, 152),
    'paleturquoise':  (175, 238, 238),
    'palevioletred':  (219, 112, 147),
    'papayawhip':     (255, 239, 213),
    'peachpuff':      (255, 218, 185),
    'peru':           (205, 133, 63),
    'pink':           (255, 192, 203),
    'plum':           (221, 160, 221),
    'powderblue':     (176, 224, 230),
    'purple':         (128, 0, 128),
    'rebeccapurple':  (102, 51, 153),
    'red':            (255, 0, 0),
    'rosybrown':      (188, 143, 143),
    'royalblue':      (65, 105, 225),
    'saddlebrown':    (139, 69, 19),
    'salmon':         (250, 128, 114),
    'sandybrown':     (244, 164, 96),
    'seagreen':       (46, 139, 87),
    'seashell':       (255, 245, 238),
    'sienna':         (160, 82, 45),
    'silver':         (192, 192, 192),
    'skyblue':        (135, 206, 235),
    'slateblue':      (106, 90, 205),
    'slategray':      (112, 128, 144),
    'slategrey':      (112, 128, 144),
    'snow':           (255, 250, 250),
    'springgreen':    (0, 255, 127),
    'steelblue':      (70, 130, 180),
    'tan':            (210, 180, 140),
    'teal':           (0, 128, 128),
    'thistle':        (216, 191, 216),
    'tomato':         (255, 99, 71),
    'turquoise':      (64, 224, 208),
    'violet':         (238, 130, 238),
    'wheat':          (245, 222, 179),
    'white':          (255, 255, 255),
    'whitesmoke':     (245, 245, 245),
    'yellow':         (255, 255, 0),
    'yellowgreen':    (154, 205, 50)
}


def parse_rgb(s):
    if not isinstance(s, string_types):
        raise ValueError("Could not parse color '{0}'".format(s))
    s = s.strip().replace(' ', '').lower()
    # simple lookup
    rgb = css_colors.get(s)
    if rgb is not None:
        return rgb

    # 6-digit hex
    match = re.match('#([a-f0-9]{6})$', s)
    if match:
        core = match.group(1)
        return tuple(int(core[i:i+2], 16) for i in range(0, 6, 2))

    # 3-digit hex
    match = re.match('#([a-f0-9]{3})$', s)
    if match:
        return tuple(int(c*2, 16) for c in match.group(1))

    # rgb(x,y,z)
    match = re.match(r'rgb\((\d+,\d+,\d+)\)', s)
    if match:
        return tuple(int(v) for v in match.group(1).split(','))

    raise ValueError("Could not parse color '{0}'".format(s))

"""
END
"""

# ../src/lib/colors.py END #



# ../src/lib/tools.py START #


"""
Socket tools. here is some functions that makes sending
and reciving data via sockets easier.
"""

# write that can select correct data type and send it
def write(data, sock):
    # takes data and socket as args
    if type(data) == bytes:
        # if it's just binary send it as it is
        sock.sendall(data)

    elif type(data) == str:
        # if it's a string send it ad utf8
        sock.sendall(data.encode())

    elif type(data) == dict:
        # if it's a dict convert it to a json 
        # string an send as utf8
        sock.sendall(json.dumps(data).encode())
    else:
        # else just convert to a string
        # and send it as utf8
        sock.sendall(str(data).encode())

# read for sock
def read(sock):
    # read the first 1024 bytes
    data = sock.recv(1024)
    # and add them to out
    out = data
    # if there is more data
    while not data:
        # keep reading
        data = sock.recv(1024)
        # and adding
        out += data
    # when you're done
    # return out
    return out


# ../src/lib/tools.py END #



# ../src/client.py START #

"""
Importing one by one so our create.py can
use it without added namespaces ( classes )
"""

# Seprator for printing messages
# it's blank when you're using colors
# but when there is no colors it becomes
# a colon ":".

COLOR_SEP = ""

""" client class
Takes 3 (4) arguments:
 - str [name]; The username you want to use
 - str [host]; Ipaddress or host name of server
 - dict [options]; Dict with to arguments
    * int [port] The port to listen on default 7777
    * bool [colors] To use colors in terminal only use if your shell/terminal supports it
"""

class Client:
    # constuctor (initilizer) takes 3 (4) Arguments
    def __init__(self, name, host, options = {"port":7777, "bits": 2048,  "colors":False}):
        # check colors
        if not options["colors"]:
            # if colors is off, override function
            # and set COLOR_SEP to colon
            global color, COLOR_SEP
            COLOR_SEP = ":"
            color = lambda msg, col: msg

        # generate rsa keypair
        self.keys = rsa(options["bits"])
        # set key varible to None
        self.key = None
        # set name to name
        self.name = name
        # create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # and connect to address
        self.sock.connect((host, options["port"]))

    """
    ClientGetMsg (client) takes some input, checks
    if it's a command and either executes the command 
    or returns the message 
    """

    def GetMsg(self):
        i =  input("")

        if i == "/exit":
            # exit with os._exit
            _exit(0)
        else:   
            return i
    """
    ClientSendMsg (client, msg) takes a single argument, the message
    which it formats and encrypt, so it can send it to
    the server
    """

    def SendMsg(self, msg):
        # check if message includes anything
        if len(msg) == 0:
            # Do nothing
            pass
        else:
            # Create message
            msg = self.name + ": " + msg
            # Encrypt message
            msg = aes(self.key).encrypt(encode(msg))
            # and write it to server
            write(msg, self.sock)
    """
    Client__thread (client) is a function that is 
    made to be runned in a seprate thread so it can
    read data from server in the background
    """

    def __thread(self):
        while True:
            # While true read incomming messages
            msg = read(self.sock)
            try:
                # and try to decode it as a normal
                # message.

                # By Decrypting it
                msg = decode(aes(self.key).decrypt(msg))
                # And formating it with colors
                if msg.split(" ").pop() == "Disconnected":
                    print(color(msg, "yellow"))
                else:
                    # And charecters
                    print(color(msg.split(":")[0] + COLOR_SEP, "blue") + " " + color(':'.join(msg.split(":")[1:]), "green"))
            # if and exception occurs
            except Exception as e:
                # decode message
                msg = msg.decode("utf8")
                # and print it
                print(color(msg, "red"))
    """
    Clientmain (client) is the main process that starts
    the Client__thread and waits for input to be send with
    ClientGetMsg and ClientSendMsg.
    """
    def main(self):
        try:
            # key exhange
            write(self.keys.pub, self.sock)
            self.key = self.keys.decrypt(read(self.sock)).decode("utf8")
            write(aes(self.key).encrypt(encode(self.name)), self.sock)
            # start thread
            threading.Thread(target=self.__thread).start()
            # and while True
            while True:
                # send messages
                self.SendMsg(self.GetMsg())
        
        except Exception as e:
            # if any error occurs
            # print it. it's probaly from
            # the self.__thread
            print(color(e, "red"))


# ../src/client.py END #



# ../src/server.py START #


"""
Generates and random string of charecters [a-Z] and numbers [0-9]
that is Cryptograficly secure using SystemRandom()
"""

def generate(n = 32):
    return ''.join([random.SystemRandom().choice(string.ascii_letters + string.digits) for x in range(n)])

"""server class
Takes 2 (3) Arguments:
 - int [port] the port to listen on
 - dict [options] dict with options
  * str [host] if you want to listen to an alternative host default "0.0.0.0"
"""
class Server:
    def __init__(self, port, options={"host":"0.0.0.0"}):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((options["host"], port))
        self.aeskey = generate()
        self.clients = set()
        self.clients_lock = threading.Lock()
    """
    Server.broadcast (server, data, _from) takes two arguments
    data the data to broadcast and _from which is the sender who
    not to send the message to. Uses a set and threading.Lock to 
    manage connected users.
    """
    def broadcast(self, data, _from):
        # broadcast to all users
        # with threading.Lock
        with self.clients_lock:
            # run over clients
            for client in self.clients:
                # if it's the sender
                if client == _from:
                    # if the client in the list is the
                    # broadcaster of the message, skip it.
                    pass
                # else
                else:
                    # send data over socket
                    write(data, client)
    """
    Server.__read (server, client) where client is
    the socket object to read from. it basicly broadcasts
    all data from the Client
    """
    def __read(self, client):
        # try to
        try:
            # while true to:
            while True:
                # read all messages
                msg = read(client)
                # and broadcast them
                self.broadcast(msg, client)
        # except for when a exception occurs
        except BrokenPipeError:
            # then end it
            # User disconnected
            return
    """
    Server.__thread (server, client) is the function
    which handles the Client it's meant to be runned
    in a seprate thread.
    """
    def __thread(self, client):
        # add client to client list 
        # with threading.Lock
        with self.clients_lock:
            self.clients.add(client)

        # exhange keys here
        # first read the public rsa key
        pub = read(client)
        # then encrypt the aes key with the public key
        key = rsa._encrypt(self.aeskey, pub)
        # then write the encrypted key
        write(key, client)
        # and read the aes encrypted username of the client
        name = decode(aes(self.aeskey).decrypt(read(client)))
        # main procress
        try:
            # send callback message
             # write ready message and start listening
             # this one is doing to be red
            write("READY...\nType /exit to exit \n\n", client)
            # start reading function
            self.__read(client)

        except BrokenPipeError:
            # then the user disconnected
            pass

        finally:
            # broadcast that the user is disconnecting
            # but encrypt it so no one can see the username
            encrypted_return = aes(self.aeskey).encrypt(encode(name + " Disconnected"))
            # broadcast and then
            self.broadcast(encrypted_return, client)
            # finally end the connection
            with self.clients_lock:
                # remove from senders set
                self.clients.remove(client)
            # and close the connection
            client.close()
    """
    Server.main (server) is the servers main process
    which listens and accepts connctions that it handles
    with Server.__thread which it starts in a new thread
    """
    def main(self):
        # while true
        while True:
            try:
                # start listening listen again each time
                self.sock.listen(1)
                # wait for connection
                client, conn = self.sock.accept()
                # when a client has connected start in a new thread
                threading.Thread(target=self.__thread, args=(client,)).start()
            except Exception as error:
                # print error probaly from thread
                print(error)


# ../src/server.py END #


# THIS FILE WILL BE INJECTED INTO THE REWRAA.PYX

# VARIABLES

# info variables
__version__ = "1.6.4"
__module__ = "RewRaa " + __version__
__author__ = " Javad Shafique "
# Fancy license
__license__ = "Copyrigth (c) 2017-present" + __author__ + "All rigths reserved"

# a dict with command line arguments
COMMAND_ARGS = {
    "--help": [
        str(__module__ + " " + __license__),
        "\nUsage: ",
        "For server: ",
        "   rewraa server port (host, port)",
        "For client: ",
        "   rewraa host, port, useColors? username\n",  
        "This program can run in five modes: ",
        "Mode 1: Setup, here it's all interactive. No arguments",
        "Mode 2: Quick, if you pass one argument either 'server' or the hostname of the computer you want to connect to",
        "Mode 3: Custom, The first argument is the same as in Quick but now you can pass a port as the second argument",
        "Mode 4: Full, Same as custom but the arguments for server is passed like this ('server', host, port) and the client (host, port, useColors?)",
        "Mode 5: Quiet, This mode is the same as full but takes one last argument the username for the client so as this (host, port, useColors?, name)",
        "",
        "Some other modes comming up:\n ",
        "rewraa hosting: starts a server with the PORT environ variable",
        "rewraa filename.rewraa: reads file as json and tries to get port, host, and username from it\n",
        "Use --help (/help, /?) to get this message\nUse --version (-v) to get the version of this program\nUse --license (/license) to get the license\nUse --author for the note left by the author\n\n",
        "NOTE: All modes using client that isn't Quiet ask for a username. Mode 2 with server listens on port 7777, the server does not take input\n"
    ],
    "--version": [
        # print module name (which includes version)
        # __version__ should only contain the version
        str(__module__)
    ],
    "--author": [
        str(__author__)
    ],
    "--license":[
        str(__license__)
    ]
}

COMMAND_ALIASES = {
    # with support for aliases
    "/help": COMMAND_ARGS["--help"],
    "/?": COMMAND_ARGS["--help"],
    "-v": COMMAND_ARGS["--version"],
    "/license":COMMAND_ARGS["--license"]
}

# ascii banner from http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=RewRaa
BANNER = """
██████╗ ███████╗██╗    ██╗██████╗  █████╗  █████╗ 
██╔══██╗██╔════╝██║    ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗  ██║ █╗ ██║██████╔╝███████║███████║
██╔══██╗██╔══╝  ██║███╗██║██╔══██╗██╔══██║██╔══██║
██║  ██║███████╗╚███╔███╔╝██║  ██║██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                               
"""

COLOR_WARNING = "WARNING: this system does not seem to support colors"


# from django.core.management.color.supports_color at https://github.com/django/django/blob/master/django/core/management/color.py
# checks if terminal supports colors. so all color support is now automatic
def supports_color():
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    """
    plat = os.sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(os.sys.stdout, 'isatty') and os.sys.stdout.isatty()
    if not supported_platform or not is_a_tty:
        return False
    return True

"""
Find match for wrong arguments (so cool)
"""
def find_match(string):
    stats = dict()
    strings = dict()
    keys = dict(COMMAND_ARGS, **COMMAND_ALIASES).keys()
    for c,i in enumerate(keys):
        s = SequenceMatcher(None, string, i).ratio()
        stats[str(c)] = s
        strings[str(c)] = i
    
    e = max(stats.items(), key=operator.itemgetter(1))[0]
    return strings[e]

"""
Setup if no arguments is specified
and you want to use it interativly
"""

def setup():
    # print banner
    print(BANNER)
    t = input("Start server or client? [S/c]: ")

    if t.lower() in ("s", "server"):
        # launch server
        port = int(input("Which port to listen on (7777): ") or 7777)
        host = "0.0.0.0"
        Server(port, dict(host=host or "localhost")).main()

    elif t.lower() in ("c", "client"):
        # launch client
        host = input("Ip adress of server: ")
        port = int(input("Which port to listen to (7777): ") or 7777)
        bits = int(input("Bitsize of RSA keypair (2048): ") or 2048)
        # check if system/terminal supports color
        colors = supports_color()

        # IF/ELSE it all day
        if colors:
            # take input yes is bigger
            c = input("Use colors [Y/n]:")
            # set varible accordingly
            if c.lower()[:1] == "n":
                colors = False
            else:
                colors = True

        else:
            # if support_color() returns false print warning
            print(COLOR_WARNING)
            # take input no is bigger
            c = input("Use colors [y/N]:")
            # set varible accordingly
            if c.lower()[:1] == "y":
                colors = True 
            else:
                colors = False
        # get username
        name = input("Type Username: ")
        # start client
        Client(name, host, dict(port=port, bits=bits, colors=colors)).main()
    
    # if the input did not choose either of
    # them count down to 0 and start again.
    else:
        # throw error
        print("Wrong choice")
        i = 10
        while i > 0:
            print(i)
            time.sleep(1)
            i = i - 1
        
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() in ("Linux", "Darwin") or os.name == "posix":
            os.system("clear")
        setup()

"""
Main function that checks amount of arguments and exectutes acordingly
"""

def main(args = None):
    if args != None:
        args = args
    else:
        args = os.sys.argv[1:]
    
    if len(args) == 0:
        setup()


    # If there only is one argument it can either be a command or one
    # of the following arguments: 
    #
    # server: starts a server on port 7777
    # $hostname: connects to the host on port 7777
    # ${filename}.rewraa: reads file as json (client only)
    # hosting: takes envionment variable PORT and listens on 0.0.0.0


    if len(args) == 1:
        # first check if it's a command
        if args[0] in COMMAND_ARGS or args[0] in COMMAND_ALIASES:
            if args[0] in COMMAND_ARGS:
                C = COMMAND_ARGS
            else:
                C = COMMAND_ALIASES
            
            for item in C[args[0]]:
                print(item)
            exit()
        if args[0][0] in ("-", "/"):
            print("Command line argument \"" + args[0] + "\" does not exist. Did you maybe mean " + find_match(args[0]))
            exit()

        # check if it's a file
        if args[0].split(".").pop() == "rewraa" and os.path.exists(args[0]):
            # load data from file
            data = json.loads(open(args[0], "r", encoding="utf-8").read())
            # read data
            port = data["port"]
            host = data["host"]
            name = data["name"]
            bits = data["bits"]
            colors = data["colors"]
            # and start client
            Client(name, host, dict(port=int(port), bits=int(bits), colors=bool(colors))).main()

        elif args[0] == "hosting":
            # if you're using a provider
            # get port from envirment varibles
            port = int(os.environ.get("PORT") or 7777)
            # set host to 0.0.0.0 (all)
            host = "0.0.0.0"
            # print port you're using
            print(port)
            # and start server
            Server(port, dict(host=host)).main()

        # only one argument (run default settings)
        elif args[0] == "server":
            Server(7777).main()
        else:
            name = input("Type Username: ")
            Client(name, args[0]).main()

    # if you have two arguments you can specify a port for the server
    # and a port for the client as such:
    #
    # rewraa server $port
    # rewraa $hostname $port

    elif len(args) == 2:
        # check for server
        if args[0] == "server":
            Server(int(args[1])).main()
        else:
            name = input("Type Username: ")
            Client(name, args[0], dict(port=int(args[1]), colors=supports_color())).main()

    # with three arguments we have the option to specify the use of colors
    elif len(args) == 3:
        # full on stuff
        if args[0] == "server":
            Server(int(args[2]), dict(host=args[1])).main()
        else:
            name = input("Type Username: ")
            Client(name, args[0], dict(port=int(args[1]), colors=bool(args[2]))).main()
    elif len(args) == 4:
        # if the last one is the username
        Client(args[3], args[0], dict(port=int(args[1]), colors=bool(args[2]))).main()
    else:
        print("Not enough arguments (or to many. max 3)")
        exit()

# main stament for runnning
# as a command
if __name__ == "__main__":
    try:
        main()
    except Exception as Error:
        print(Error)
        pass
