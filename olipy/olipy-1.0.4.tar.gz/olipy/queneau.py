"""Create Queneau assemblies of source texts."""
from io import StringIO
import json
import random
import re

class Assembler(object):

    def __init__(self, initial=[]):
        self.items = []
        self.tokens_by_position = {}
        self.lengths = []
        for i in initial:
            self.add(i)

    def token_bucket(self, token):
        return self.tokens_by_position

    def bucket_for_position(self, position, code, so_far):
        return self.tokens_by_position

    def add(self, item, tokens_in='tokens'):
        if isinstance(item, dict):
            if not tokens_in in item:
                raise ValueError(
                    "Dictionary added to corpus must put tokens in '%s'." % tokens_in)
            tokens = item[tokens_in]
        elif not (isinstance(item, tuple) or isinstance(item, list)):
            raise ValueError(
                "Only lists, tuples, and dicts may be added to the corpus.")
        else:
            tokens = item
        self.items.append(item)
        l = len(tokens)
        if l > 0:
            self.lengths.append(l)
            for i, token in enumerate(tokens):
                tup = (token, item)
                bucket = self.token_bucket(token)
                bucket.setdefault(i, []).append(tup)
                if bucket != self.tokens_by_position:
                    self.tokens_by_position.setdefault(i, []).append(tup)
                # Also add tokens to more general positions like "middle"
                # and "end".
                if i > 0 and i < l-1:
                    bucket.setdefault("m", []).append(tup)
                if i == l-1:
                    bucket.setdefault("l", []).append(tup)

    def _assert_possible_position(self, position, pattern, length):
        if len(self.tokens_by_position[position]) == 0:
            raise ValueError(
                'Pattern "%s" cannot generate an assembly of length %d with this corpus, because there are no possible values at position %d.' % (pattern, length, position))


    def empty_bucket(self):
        """Generate an empty token bucket."""
        return dict(f=[], m=[], l=[])

    def expand_pattern(self, pattern, length):
        """Decode a short string representing a family of Queneau assembly.

        Some common families, expanded to length 5:

        "0." -> 0, 1, 2, 3, 4
        "0.l" -> 0, 1, 2, 3, last
        "f.l" -> first, middle, middle, middle, last
        "f." -> first, middle, middle, middle, last
        "." -> first, middle, middle, middle, last

        Some less common families:

        "011." -> 0, 1, 1, 2, 3
        "011.l" -> 0, 1, 1, 2, last
        "0f1fl" -> 0, 0, 1, 0, last
        "f.f" -> first, middle, middle, middle, first
        "l.f" -> last, middle, middle, middle, first
        "m.l" -> middle, middle, middle, middle, last
        """
        if length < len(pattern):
            pattern = pattern[:length]
        expanded = []
        previous = None
        if pattern.count(".") > 1:
            raise ValueError(
                'Pattern may not contain more than one expansion characters.')
        if pattern.startswith('.'):
            pattern = "f." + pattern[1:]
        for i, code in enumerate(pattern):

            if code == 'f':
                # First item
                expanded.append(0)

            elif code == 'l':
                # Last item
                expanded.append("l")

            elif code == 'm':
                # An item that's neither first nor last.
                expanded.append("m")

            elif code in "0123456789":
                # An item from a specific place in the sequence.
                code = int(code)
                self._assert_possible_position(code, pattern, length)
                expanded.append(code)

            elif code == '.':
                # Expand the next few entries to fit a pattern
                # established by the previous code.

                # First, see how many things we have to fill in.
                to_be_generated = length-i # Number of items to be generated.
                generated_by_pattern = len(pattern)-i-i # Number of those items to be generated by remaining items in the pattern.
                expanded_size = to_be_generated-generated_by_pattern
                if isinstance(previous, int):
                    # A numeric position is expanded by incrementing
                    # the number.
                    for j in range(previous+1, previous+expanded_size+1):
                        self._assert_possible_position(j, pattern, length)
                        expanded.append(j)
                elif previous in 'flm':
                    for j in range(0, expanded_size):
                        if j == to_be_generated-1:
                            # The last item in the expansion will be
                            # taken from the set of last items.
                            expanded.append('l')
                        else:
                            # Any other item will be taken from the
                            # middle.
                            expanded.append('m')
            else:
                # Invalid code
                raise ValueError(
                    'Invalid character "%s" in pattern "%s".' % (code, pattern))
            previous = code
        return expanded

    def assemble(self, pattern="f.l", length=None, min_length=None):
        while length is None:
            length = random.choice(self.lengths)

        if min_length and length < min_length:
            length = min_length

        pattern = self.expand_pattern(pattern, length)

        so_far = []

        for position, code in enumerate(pattern):
            bucket = self.bucket_for_position(position, code, so_far)
            if bucket[code]:
                choice = random.choice(bucket[code])
                so_far.append(choice)
                yield choice

    @classmethod
    def load(cls, f, tokens_in='tokens'):
        """Load from a filehandle that defines a JSON list of objects."""
        corpus = Assembler()
        for i in json.load(f):
            if tokens_in in i:
                corpus.add(i, tokens_in)
        return corpus

    @classmethod
    def loadlines(cls, f, tokens_in='tokens'):
        """Load from a filehandle that defines a JSON object on every line."""
        corpus = cls()
        for i in f.readlines():
            o = json.loads(i)
            if tokens_in in o:
                corpus.add(o, tokens_in)
        return corpus

    @classmethod
    def loadlist(cls, l, tokens_in='tokens'):
        """Load from a list of objects.""" 
        corpus = cls()
        for o in l:
            if tokens_in in o:
                corpus.add(o, tokens_in)
        return corpus
    
    @classmethod
    def loads(cls, s):
        return cls.load(StringIO(s))

    def dumps(self, compress=False):
        return str(dump(StringIO(), compress))

    def dump(self, f, compress=False):
        for item in self.items:
            if compress:
                if isinstance(item, dict):
                    tokens = item['tokens']
                else:
                    tokens = item
                if len(tokens) == 0:
                    # Skip this one--it can't be used in assemblies.
                    continue
            f.write(json.dumps(item) + "\n")

class SentenceAssembler(Assembler):
    """Assemble sentences from words.

    Markov chains are usually better for this."""

    WHITESPACE = re.compile("\s+")

    def add(self, item):
        words = self.WHITESPACE.split(item)
        super(SentenceAssembler, self).add(words)

class WordAssembler(Assembler):

    """Assemble words from runs of vowels and consonants."""

    def __init__(self, initial=[]):
        self.vowel_runs_by_position = self.empty_bucket()
        self.consonant_runs_by_position = self.empty_bucket()
        super(WordAssembler, self).__init__(initial)

    sequence_of_vowels = re.compile("([aeiou]+)", re.I)
    vowels="aeiouAEIOU"

    def token_bucket(self, token):
        if token[0] in self.vowels:
            return self.vowel_runs_by_position
        else:
            return self.consonant_runs_by_position

    def bucket_for_position(self, position, code, so_far):
        if position == 0:
            # Choose the first token from the list of all first tokens.
            return self.tokens_by_position

        # Subsequent tokens must alternate between the vowel and
        # consonant buckets.
        if so_far[0][0] in self.vowels:
            vowels_at_mod = 0
        else:
            vowels_at_mod = 1
        if (position % 2) == vowels_at_mod:
            return self.vowel_runs_by_position
        else:
            return self.consonant_runs_by_position

    def add(self, word):
        chunks = [x.strip() for x in self.sequence_of_vowels.split(word) if x.strip()]
        super(WordAssembler, self).add(dict(tokens=chunks))

    def assemble_word(self, *args, **kwargs):
        word = None
        while not word:
            word = "".join(x[0] for x in self.assemble(*args, **kwargs))
        return word


class CompositeAssembler(Assembler):
    """Choose from a number of assemblers based on their relative sizes."""

    def __init__(self, initial):
        self.assemblers = []
        for i in initial:
            self.add(i)

    def add(self, assembler):
        self.assemblers.append(assembler)

    def assemble(self, *args):
        total = 0
        sizes = []
        for i in self.assemblers:
            size = len(i.items)
            total += size
            sizes.append(size)

        choice = random.randint(0, total)
        for i, assembler in enumerate(self.assemblers):
            choice -= sizes[i]
            if choice <= 0:
                return assembler, assembler.assemble(*args)


class DialogueAssembler(Assembler):
    """A separate corpus is established for each speaker.
    """

    def __init__(self, initial=[]):
        self.assembler_by_speaker = {} # Lines for each speaker
        self.transitions_by_speaker = {} # Which speaker tends to follow a given speaker?
        self.last_speaker = None
        self.last_section = None
        super(DialogueAssembler, self).__init__(initial)

    def add(self, o, tokens_in="tokens", speaker_in="speaker"):
        speaker = o[speaker_in]
        if speaker not in self.assembler_by_speaker:
            self.assembler_by_speaker[speaker] = Assembler()
        assembler = self.assembler_by_speaker[speaker]
        if self.last_speaker is not None:
            self.transitions_by_speaker.setdefault(self.last_speaker, []).append(speaker)
            self.transitions_by_speaker.setdefault(None, []).append(speaker)
        self.last_speaker = speaker
        assembler.add(o, tokens_in)

    def assemble(self, last_speaker=None, pattern="f.l"):
        speaker = random.choice(self.transitions_by_speaker[last_speaker])
        subassembler = self.assembler_by_speaker[speaker]
        return speaker, list(subassembler.assemble(pattern))
