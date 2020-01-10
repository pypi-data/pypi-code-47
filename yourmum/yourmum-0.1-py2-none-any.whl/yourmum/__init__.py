#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

class Jokes():
    def __init__(self,pronoun='your', noun='mum'):
        assert isinstance(pronoun, str), 'The pronoun parameter must be a string.'
        assert isinstance(noun, str), 'The noun parameter must be a string.'
        self.folder='yourmum/jokes/'
        self.pronoun=pronoun.title()
        self.noun=noun

    def dumb(self):
        return self.generator('dumb')

    def fat(self):
        return self.generator('fat')

    def old(self):
        return self.generator('old')

    def ugly(self):
        return self.generator('ugly')

    def generator(self, category):
        return (self._format(joke) for joke in open(os.path.join(self.folder, '{}.txt'.format(category)), 'r'))

    def random(self):
        category = random.choice(['dumb', 'fat', 'old', 'ugly'])
        generator = self.generator(category)
        jokes = list(generator)
        return random.choice(jokes)

    def _format(self, joke):
        return joke.strip().format(pronoun=self.pronoun, noun=self.noun)