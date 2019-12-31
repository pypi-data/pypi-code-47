#!/usr/bin/env python3

""" AD1459, an IRC Client

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

  A parser for IRC style tags.
"""

import logging
from urllib.parse import urlparse

class Parser:

    formatting = {
        '\x02': ['b', '*'],
        #'\u0003': 'color',
        #'\u000F': 'clear',
        '\x1D': ['i', '_'],
        '\x1F': ['u', '-']
    }

    def __init__(self):
        self.log = logging.getLogger('ad1459.formatting')
    
    def format_text(self, text):
        for i in self.formatting:
            # text = text.replace(f'/{self.formatting[i][0]}', i)
            text = text.replace(f'/{self.formatting[i][1]}', i)
        return text

    def parse_text(self, text):        
        # \u0002 bold
        # \u0003 colour
        # \u000F cancel all
        # \u001D italic
        # \u001F underline
        text = self.fix_markedup_tags(text)
        f_text = ''
        current_tags = []

        for char in text:
            if char in self.formatting:

                if not char in current_tags:
                    for tag in reversed(current_tags):
                        f_text = f'{f_text}</{self.formatting[tag][0]}>'

                    current_tags.append(char)
                    for tag in current_tags:
                        f_text = f'{f_text}<{self.formatting[tag][0]}>'

                else:
                    for tag in reversed(current_tags):
                        f_text = f'{f_text}</{self.formatting[tag][0]}>'

                    current_tags.pop()
                    for tag in current_tags:
                        f_text = f'{f_text}<{self.formatting[tag][0]}>'

            else: 
                f_text = f'{f_text}{char}'
        
        for tag in reversed(current_tags):
            f_text = f'{f_text}</{self.formatting[tag][0]}>'

        return f_text
    
    def hyperlinks(self, text):
        words = text.split()

        linked_words = []
        for word in words:
            scheme = urlparse(word).scheme
            if scheme == 'http' or scheme == 'https':
                paren = False
                if word.endswith(')'):
                    word = word.strip(')')
                    paren = True
                word = f'<a href="{word}">{word}</a>'
                if paren:
                    word = f'{word})'
            linked_words.append(word)
        return " ".join(linked_words)

    def fix_markedup_tags(self, text):
        mu_formatting = {
            '&#x2;': '\x02',
            #'\u0003': #'\u0003',
            #'\u000F': #'\u000F',
            '&#x1d;': '\x1D',
            '&#x1f;': '\x1F'
        }

        for i in mu_formatting:
            text = text.replace(i, mu_formatting[i])
        
        return text