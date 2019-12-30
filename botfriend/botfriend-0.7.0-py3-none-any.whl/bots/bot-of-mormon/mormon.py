# encoding: utf-8
from pdb import set_trace
import gzip
import json
import os
import random
from olipy.queneau import Assembler
import wordfilter

# Avoid blasphemy and super unpleasantness in addition to racial
# slurs (which are present in this corpus).
wordfilter.add_words([
    'jesus', 'christ', 'lord', 'god', 'heavenly father', 'holy ghost', 'savior',
    'redeemer', 'jehovah', 'rape', 'rapist', 'incest', 'molest'
])

class Speaker(object):
    """I have an important message for you."""

    DIRECTORY = os.path.split(__file__)[0]

    # Don't put two conjunctions together.
    STOPWORDS = set(["and", "but", "or", "nor", "for", "yet", "so", "although", "as", "after", "because", "before", "even", "if", "lest", "now", "once", "provided", "since", "than", "that", "til", "until", "when", "whenever", "where", "whereas", "wherever", "whether", "which", "while", "who", "whoever", "why", "both", "either", "neither", "whether", "such", "scarcely", "rather"])
    
    @classmethod
    def load_stream(cls, filename, choose_fraction=0.15):
        x = []
        path = os.path.join(cls.DIRECTORY, 'data', filename)
        for i in gzip.open(path):
            if random.random() < choose_fraction:
                x.append(json.loads(i.strip()))
        return x
    
    @classmethod
    def random(cls):
        """Create a Speaker from a randomly selected corpus."""
        d_and_c = lambda: cls.load_stream("d_and_c.queneau.json.gz")
        early_conference = lambda: cls.load_stream("early_conference.queneau.json.gz")
        conference = lambda: cls.load_stream("conference.queneau.json.gz")
        b_of_m = lambda: cls.load_stream("b_of_m.queneau.json.gz")
        pearl = lambda: cls.load_stream("p_of_g_p.queneau.json.gz")
        journal = lambda: cls.load_stream("j_of_d.queneau.json.gz")

        accept_old = False
        if random.randint(1,4) == 4:
            # Conference + Discourses.
            sample = random.sample(conference(), 300) + random.sample(early_conference(), 300) + random.sample(journal(), 300)
        elif random.randint(1, 5) == 5:
            # Scripture LDS edition.
            sample = random.sample(d_and_c(), 100) + random.sample(b_of_m(), 100) + random.sample(pearl(), 50)
            accept_old=True
        elif random.randint(1,3) == 3:
            # Pure conference gold.
            sample = random.sample(conference(), 300) + random.sample(early_conference(), 300)
        else:
            # Everything.
            sample = random.sample(conference(), 200) + random.sample(early_conference(), 200) + random.sample(d_and_c(), 150) + random.sample(b_of_m(), 150) + random.sample(pearl(), 50) + random.sample(journal(), 100)

        return Speaker(Assembler(), sample, accept_old)

    def __init__(self, assembler, sample, accept_old=False, hard_size_limit=140):
        self.assembler = assembler
        for i in sample:
            self.assembler.add(i)
        self.accept_old = accept_old
        self.hard_size_limit = hard_size_limit

    def speak(self, min_size=20, max_size=None):
        if not max_size:
            max_size = max(min_size, max(random.gauss(95, 20), self.hard_size_limit))
        f = None
        while not f:
            f = self.attempt(min_size, max_size)
        return f

    def attempt(self, min_size, max_size):
        f = ""
        last_punc = None
        parts = list(self.assembler.assemble("."))
        found_modern = False
        found_old = False
        new_parts = []
        for x in parts:
            text, first_word, last_word, contains_modern = x[0]
            if contains_modern:
                found_modern = True
            else:
                found_old = True
            new_parts.append((text, first_word, last_word))
        if not self.accept_old and not found_modern:
            return False
        if found_modern and not found_old and random.random() > 0.3:
            return False
        parts = new_parts
        if len(parts) == 2 and any(x[0].count(' ') < 2 for x in parts) and random.randint(1, 6) != 1:
            return False
        joining_onto_word = None
        for seg, first_word, last_word in parts:
            if joining_onto_word in self.STOPWORDS and first_word in self.STOPWORDS:
                return False
            joining_onto_word = last_word
            if last_punc and last_punc in ';,':
                f += ' '
            f += seg.strip()
            last_punc = f[-1]
        if f.count('"') % 2 == 1:
            if f.endswith('"'):
                f = '"' + f
            else:
                f = f + '"'
        f = f.strip()
        if f[-1] in ';—,:':
            f = f[:-1]
        if f[-1] not in '."\'?!':
            f = f + "."
        if ']' in f and not '[' in f:
            f = f.replace("]", "")
        if '[' in f and not ']' in f:
            f = f.replace("[", "")
        if len(f) > max_size:
            return None
        if len(f) < min_size:
            return None
        check = f.lower()
        if wordfilter.blacklisted(check):
            return None
        f = f.replace("\n", " ")
        return f
