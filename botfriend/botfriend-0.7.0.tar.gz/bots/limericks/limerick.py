#!/usr/bin/python
import json
import os
import random
import sys

homedir = os.path.split(__file__)[0]

class Lines(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def sound(self):
        return random.choice(list(self.sounds.keys()))

    def all(self, exclude_sound=None):
        for sound in self.sounds:
            if sound == exclude_sound:
                continue
            for word, line in self.possibilities_for_sound(sound):
                yield sound, word, line

    def possibilities_for_sound(self, sound, exclude_words=[]):
        for word, lines in list(self.sounds[sound].items()):
            if word not in exclude_words:
                for line in lines:
                    yield word, line

    def line(self, used_words, sound=None, exclude_sound=None):
        # print "%d words for %s" % (len(self.sounds[sound]), sound)

        if sound is None:
            # Pick from the entire range at random.
            sound, word, line = random.choice(list(self.all(exclude_sound)))
        else:
            # We've been given a sound.
            possibilities = list(self.possibilities_for_sound(sound, used_words))
            if len(possibilities) == 0:
                # We're out of options. We need to reuse a word.
                return self.line([], sound)
            word, line = random.choice(possibilities)
        used_words.append(word)

        # Look for a dangling quote mark
        if line.count('"') == 1:
            if line[-1] == '"' or '" ' in line:
                line = '"' + line
            else:
                line = line + '"'

        # Same for parenthesis
        if line.count(')') == 1 and line.count('(') != 1:
            line = '(' + line
        elif line.count('(') == 1 and line.count(')') != 1:
            line = line + ')'

        return sound, word, line


lines = [Lines(json.load(open(os.path.join(homedir, "%d-partitioned.json" % i)))) for i in range(0, 5)]

class Limerick(object):

    def __init__(self):
        self.sounds = []
        self.words = []
        self.lines = []
        self.unclosed_quote = False
        self.choices = []
        for i in range(0, 5):
            self.pump(i)

    def __str__(self):
        return "\n".join(self.lines)

    def pump(self, position):
        args = [self.choices]
        if position == 0:
            pass
        elif position == 1:
            args.append(self.sounds[0])
        elif position == 2:
            args.extend([None, self.sounds[0]])
        elif position == 3:
            args.append(self.sounds[2])
        elif position == 4:
            args.append(self.sounds[0])
        sound, word, line = lines[position].line(*args)
        self.sounds.append(sound)
        self.words.append(word)
        self.lines.append(line)

    @classmethod
    def for_twitter(self, letters_or_numbers="numbers"):
        if letters_or_numbers == "numbers":
            line1 = "1.\n"
            line2 = "2.\n"
        else:
            line1 = "A.\n"
            line2 = "B.\n"
        to_post = None
        while to_post is None:
            limerick = Limerick()
            separated, joined = limerick.as_tweets()
            if len(joined[0]) < 140:
                to_post = joined
            elif len(separated[0]) < 137 and len(separated[1]) < 137:
                to_post = line1 + separated[0], line2 + separated[1]
        return to_post
    
if __name__ == '__main__':
    print(str(Limerick()))
        
