# encoding: utf-8
import os
import re
from textblob import TextBlob
from pdb import set_trace
import json
import random
from collections import Counter

base_dir = os.path.split(__file__)[0]

MAX_YEAR = 2014

class CounterWithRandomChoice(Counter):

    def choice(self):
        keys = sorted(self.keys())
        total = sum(self.values())
        target = random.uniform(0, total)
        total_so_far = 0
        for key in keys:
            value = self[key]
            total_so_far += value
            if target <= total_so_far:
                return key

class GhostbusterCastingOffice(object):

    DIRECTORY = os.path.split(__file__)[0]
    DATA_DIRECTORY = os.path.join(DIRECTORY, 'data')

    def load(self, filename):
        return json.load(open(os.path.join(self.DATA_DIRECTORY, filename)))
    
    def __init__(
            self, recently_used=[],
            recently_used_cutoff=800
    ):
        recently_used = recently_used or []
        if isinstance(recently_used, str):
            recently_used = json.loads(recently_used)
        self.by_year = self.load("comedic_actors.json")
        self.directors_by_year = self.load("comedic_directors.json")
        self.recently_used = recently_used
        self.recently_used_set = set(self.recently_used)
        self.recently_used_cutoff=recently_used_cutoff

    def save_recently_used(self):
        self.recently_used = self.recently_used[:self.recently_used_cutoff]
        out = open(self.recently_used_file, "w")
        for i in self.recently_used:
            out.write(i.encode("utf8"))
            out.write("\n")

    def random_year(self, gender=None):
        year_counter = CounterWithRandomChoice()
        for year, data in list(self.by_year.items()):
            if int(year) > MAX_YEAR:
                continue

            multiplier = 1
            if year > 2000:
                multiplier * 0.75
            elif year > 1995:
                multiplier =  0.80
            elif year > 1990:
                multiplier = 0.85

            if not gender or 'm':
                year_counter[year] += len(data['men']) * multiplier
            if not gender or 'f':
                year_counter[year] += len(data['women']) * multiplier

        # Choose a year proportional to how many actors are available
        # for that year.
        return year_counter.choice()

    def gender_makeup(self, gender=None):
        """How many men and how many women make up this ghostbusting team?"""
        if not gender:
            if random.randint(1, 10) == 1:
                gender = None # Co-ed Ghostbuster team
            elif random.randint(1,2) == 1:
                gender = 'm'
            else:
                gender = 'f'

        if gender == 'm':
            return 4, 0
        if gender == 'f':
            return 0, 4
        men = random.randint(1,3)
        women = 4 - men
        return men, women

    def choose(self, choices, mean):
        if not choices:
            return None
        if mean is None:
            return random.choice(choices)
        else:
            mean = len(choices) * mean
            v = None
            while v is None or v >= len(choices):
                v = int(random.expovariate(1.0/mean))
            choice = choices[v]
            choices.remove(choice)
            return choice

    def default_title(self, year):
        year = int(year)
        if year < 1950:
            choices = ['Ghost Busters', 'Ghost Busters',
                       'The Ghost Busters',
                       'Ghost-Busters', 'The Ghost-Busters']
        else:
            choices = ['Ghostbusters', 'Ghostbusters', 'Ghostbusters',
                       'Ghost Busters', 'The Ghostbusters']
        if year < 1935:
            choices.extend(['The Ghost Bursters', 'Ghost-Bursters'])
        return random.choice(choices)

    def title(self, year):
        default = self.default_title(year)
        title = None
        if random.random() < 0.25:
            title = self.custom_title(year)
        if not title:
            title = default
        return title

    def custom_title(self, year, attempts=100):
        year_obj = self.by_year[year]
        titles = list(year_obj['titles'].keys())
        for i in range(attempts):
            choice = random.choice(titles)
            new_title = self.ghostbust_title(choice)
            if new_title:
                return new_title
        return None

    def ghostbust_title(self, title):
        if ':' in title or '(' in title or ')' in title:
            return None
        if title.count(' ') > 3:
            return None
        if 'Gold Diggers' in title:
            return title.replace("Gold Diggers", "Ghostbusters")
        if 'Gold-Diggers' in title:
            return title.replace("Gold-Diggers", "Ghostbusters")
        if 'Golddiggers' in title:
            return title.replace("Golddiggers", "Ghostbusters")

        words = [x[0] for x in TextBlob(title).tags]
        tags = TextBlob(title.lower()).tags
        if len(tags) != len(words):
            return None
        new_title = []
        replacement_index = None
        nouns = []
        plural_nouns = []
        for i, word in enumerate(words):
            tag = tags[i][1]
            if tag in 'NN':
                word = words[i]
                if not word in ['L']:
                    nouns.append(word)
            elif tag == 'NNS':
                word = words[i]
                if not word in ['L']:
                    plural_nouns.append(word)
        if not nouns and not plural_nouns:
            # No use using this title.
            return None
        if plural_nouns:
            to_replace = random.choice(plural_nouns)
            replacement_string = random.choice(
                ["Ghostbusters", "Ghostbusters", "Ghosts"])
        else:
            to_replace = random.choice(nouns)
            replacement_string = random.choice(
                ["Ghostbuster", "Ghostbuster", "Ghost"])

        tr = to_replace
        tr = tr.replace("*", "\*")
        try:
            with_apostrophe = re.compile("(^%s'| %s')" % (tr, tr))
        except Exception as e:
            set_trace()
        without_apostrophe = re.compile("(^%s | %s | %s$)" % (tr, tr, tr))
        new_title = with_apostrophe.sub(" " + replacement_string + "'", title)
        if new_title == title:
            new_title = without_apostrophe.sub(" " + replacement_string + " ", title)
        new_title = new_title.strip()
        if new_title in ('The Ghost','Ghosts', 'Ghost', 'The Ghostbuster',
                         'Ghostbuster'):
            # Boring.
            return None
        if new_title == title:
            return None
        # print "%s => %s" % (title, new_title)
        return new_title

    def director(self, year):
        counter = CounterWithRandomChoice()
        if len(self.directors_by_year.get(year, [])) < 3:
            return None # Otherwise Chaplin directs everything pre-1923.

        for director in self.directors_by_year[year]:
            if director['name'] in self.recently_used_set:
                continue
            power = director['star_power']
            # Affirmative action for women directors, who make up
            # less than 10% of the total.
            if director['gender'] != 'm':
                power *= 3

            # Handicap the superstar directors a little.
            if power > 800000:
                power = int(power * (0.5 + random.random()/2))

            # Chaplin is not a superstar director in terms of modern
            # attention, but he completely blows away all his
            # contemporaries. Handicap him to give the others a
            # chance.
            if director['name'] == 'Charles Chaplin':
                power *= 0.2

            # Woody Allen also deserves a special penalty.
            if director['name'] == 'Woody Allen':
                power *= 0.2

            counter[director['name']] += power
        return counter.choice()

    def cast(self, year=None, gender=None):

        candidates = []

        if not year:
            year = self.random_year(gender)
        target_men, target_women = self.gender_makeup(gender)

        year_obj = self.by_year[year]
        candidates = []

        men = [(x['name'], x['star_power']) for x in year_obj['men']
               if x['name'] not in self.recently_used_set
        ]
        women = [(x['name'], x['star_power']) for x in year_obj['women']
                 if x['name'] not in self.recently_used_set
        ]

        by_star_power = lambda x: x[1]
        men = sorted(men, key=by_star_power)
        women = sorted(women, key=by_star_power)

        # We want to pick two well-known actors and two lesser-known
        # actors.
        #
        # Actual positions of the 1984 Ghostbusters are:
        # 0.84 (Harold Ramis)
        # 0.85 (Ernie Hudson)
        # 0.98 (Dan Aykroyd)
        # 0.99 (Bill Murray)
        #
        # But if we pick from that high up it won't be much fun, and
        # also those numbers are distorted by the success of
        # "Ghostbusters" itself.
        selected = []
        if random.randint(1,2) == 1:
            means = [0.85, 0.8, 0.75, 0.7]
        else:
            means = [0.85, 0.8, 0.8, 0.75]
        random.shuffle(means)

        # If there aren't enough actors for this year who haven't been used recently,
        # relax the 'not used recently' restriction.
        if len(men) < target_men:
            men = [(x['name'], x['star_power']) for x in year_obj['men']]
        if len(women) < target_women:
            women = [(x['name'], x['star_power']) for x in year_obj['women']]

        if len(women) < target_women or len(men) < target_men:
            # It still won't work. Give up.
            return None, None
        
        # Pick the men.
        for i in range(target_men):
            choice = None
            while choice is None:
                choice = self.choose(men, means[-1])
            means.pop()
            selected.append(choice)

        # Pick the women.
        for i in range(target_women):
            choice = None
            while choice is None:
                choice = self.choose(women, means[-1])
                if choice is None:
                    set_trace()
            means.pop()
            selected.append(choice)

        # Sort the cast roughly by star power but allowing for a significant
        # random element.
        cast = sorted(selected, key=lambda x: -x[1]*(random.random()/2))
        cast = [x[0] for x in cast]
        return year, cast

    def tweet(self):
        tweet = None
        while not tweet:
            tweet = self._tweet()
        return tweet

    def _tweet(self):

        year, cast = self.cast()
        if not year:
            return None
        
        default_title = "Ghostbusters"
        director = self.director(year)
        default_tweet = self.make_tweet(default_title, year, cast, director)
        if len(default_tweet) > 140:
            # The names are just too long.
            return None

        # Okay, we've got something in our back pocket. Let's try to
        # get a better title.
        tweet = None
        for i in range(10):
            title = self.title(year)
            tweet = self.make_tweet(title, year, cast, director)
            if len(tweet) > 140:
                tweet = None
            else:
                break

        return tweet

    def make_tweet(self, title, year, cast, director):
        if director:
            if director not in self.recently_used_set:
                self.recently_used.append(director)
            director = "dir. %s" % director
        else:
            director = ''
        for i in cast:
            if i not in self.recently_used_set:
                self.recently_used.append(i)
        self.recently_used = self.recently_used[-self.recently_used_cutoff:]
        self.recently_used_set = set(self.recently_used)
        cast_with_and = ", ".join(cast[:3]) + " and %s" % cast[-1]
        cast_without_and = ", ".join(cast)
        if director:
            long_director = " (%s)" % director
        else:
            long_director = ''
        long_version = "%s (%s) starring %s%s" % (title, year, cast_with_and, long_director)
        if random.random() < 0.10:
            separator = ":"
            if director:
                director = " (%s)" % director
        else:
            separator = " —"
            if director:
                director = " — %s" % director
        short_version = "%s (%s)%s %s%s" % (title, year, separator, cast_without_and, director)
        even_shorter_version = "%s (%s)%s %s" % (title, year, separator, cast_without_and)
        if len(long_version) > 140 or random.random() < 0.15:
            if len(short_version) > 140:
                return even_shorter_version
            return short_version
        return long_version
