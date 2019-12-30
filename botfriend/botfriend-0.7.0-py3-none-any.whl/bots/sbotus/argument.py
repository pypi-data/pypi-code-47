import bz2
import json
import random
import os
from pdb import set_trace
from olipy.markov import MarkovGenerator

class LineProvider(object):

    base_dir = os.path.split(__file__)[0]

    MAX_SIZE = 200000

    def __init__(self, speakers):
        self.by_state = {}
        self.speakers = speakers

    @classmethod
    def data(cls, path):
        return os.path.join(cls.base_dir, "data", path)
        
    def path(self, path):
        return self.data(os.path.join(self.data_dir, path))
    
    def line(self, state, last_speaker):
        state = self.state(state, last_speaker)
        if not state in self.by_state:
            self.load_state(state)
        return self.make_line(state, last_speaker)

    def state(self, state, last_speaker):
        if state in ('interruption', 'response'):
            if 'scotus_justice' in last_speaker['roles']:
                state = state + '-' + 'justice'
            else:
                state = state + '-' + 'nonjustice'
        return state
    
    def make_line(self, state, last_speaker):
        raise NotImplementedError()
    
    def load_state(self, state):
        raise NotImplementedError()
    
class VerbatimLineProvider(LineProvider):

    data_dir = "verbatim"

    def __init__(self, speakers):
        super(VerbatimLineProvider, self).__init__(speakers)
        self.markov_by_state = {}
    
    def load_state(self, state):
        if state in self.by_state:
            return
        path = self.path("%s.ndjson.bz2" % state)
        data = []
        for i in bz2.BZ2File(path, 'r'):
            i = json.loads(i)
            data.append(i)
            if self.MAX_SIZE and len(data) > self.MAX_SIZE:
                break
        self.by_state[state] = data

    def make_line(self, state, last_speaker):
        speaker_ok = False
        while not speaker_ok:
            utterance = random.choice(self.by_state[state])
            if not last_speaker or utterance['who'] != last_speaker['id']:
                speaker_ok = True
        return self.speakers[utterance['who']], utterance

class Assembler(object):

    LENGTHS = {
    
        "start" : { 1: 1588, 2: 3722, 3: 843, 4: 876, 5: 359, 6: 153, 7: 76, 8: 35, 9: 19, 10: 17, 11: 6, 12: 3, 13: 6, 14: 2, 16: 2 },
    
        "final": { 1: 6544, 2: 865, 3: 194, 4: 60, 5: 25, 6: 12, 7: 4, 8: 2, 10: 1 },

        "question": { 1: 213302, 2: 100581, 3: 42150, 4: 17436, 5: 7722, 6: 3410, 7: 1601, 8: 827, 9: 382, 10: 206, 11: 110, 12: 70, 13: 41, 14: 18, 15: 9, 16: 10, 17: 2, 18: 4, 19: 2 },

        "statement": { 1: 1140458, 2: 657853, 3: 332615, 4: 162337, 5: 79926, 6: 40107, 7: 20256, 8: 10503, 9: 5616, 10: 2989, 11: 1554, 12: 852, 13: 494, 14: 266, 15: 153, 16: 87, 17: 48, 18: 37, 19: 15, 20: 11, 21: 6, 22: 4, 23: 4, 24: 1, 25: 3, 26: 2},

        "interruption": {1: 299432, 2: 139738, 3: 55062, 4: 23072, 5: 11028, 6: 5419, 7: 2774, 8: 1475, 9: 793, 10: 453, 11: 244, 12: 120, 13: 71, 14: 52, 15: 19, 16: 14, 17: 11, 18: 4, 19: 4},
    
        "response-justice": { 1: 137416, 2: 107065, 3: 42128, 4: 16676, 5: 7481, 6: 3584, 7: 1768, 8: 887, 9: 477, 10: 234, 11: 148, 12: 69, 13: 33, 14: 21, 15: 20, 16: 9, 17: 5, 18: 2, 19: 2,
        },

        "response-nonjustice":  { 1: 33113, 2: 20012, 3: 8237, 4: 3403, 5: 1591, 6: 784, 7: 379, 8: 178, 9: 101, 10: 54, 11: 29, 12: 12, 13: 12, 14: 4, 15: 2, 17: 1},

        "interruption-justice": { 1: 112718, 2: 58014, 3: 24170, 4: 10786, 5: 5350, 6: 2713, 7: 1477, 8: 778, 9: 440, 10: 259, 11: 125, 12: 66, 13: 38, 14: 28, 15: 9, 16: 9, 17: 6, 18: 2, 19: 2},

        "interruption-nonjustice": { 1: 186714, 2: 81724, 3: 30892, 4: 12286, 5: 5678, 6: 2706, 7: 1297, 8: 697, 9: 353, 10: 194, 11: 119, 12: 54, 13: 33, 14: 24, 15: 10, 16: 5, 17: 5, 18: 2, 19: 2 },
    }
    
    def __init__(self, state, base_path):
        self.state = state
        self.lengths = self.LENGTHS[state]
        self.max_length = sum(self.lengths.values())
        self.single = []
        self.first = []
        self.middle = []
        self.last = []
        for name, bucket in (
                ('single', self.single),
                ('first', self.first),
                ('middle', self.middle),
                ('last', self.last)
        ):
            path = os.path.join(base_path, "%s.%s.txt.bz2" % (self.state, name))
            inp = bz2.BZ2File(path, 'r')
            for num, line in enumerate(inp):
                bucket.append(line[:-1].decode("utf8"))
                if LineProvider.MAX_SIZE and num > LineProvider.MAX_SIZE:
                    break

    @property
    def random_length(self):
        num = random.randint(0, self.max_length-1)
        counter = 0 
        for k, v in sorted(self.lengths.items()):
            counter += v
            if counter > num:
                return k
            
    def assemble(self):
        length = self.random_length
        if length == 1:
            return None
        parts = [random.choice(self.first)]
        num_middle = length-2
        if num_middle:
            parts.extend(random.sample(self.middle, num_middle))
        parts.append(random.choice(self.last))
        return "".join(parts)

class RandomSpeaker(LineProvider):

    def __init__(self, speakers):
        super(RandomSpeaker, self).__init__(speakers)
        self.justices = []
        self.nonjustices = []
        for id, speaker in list(speakers.items()):
            if 'scotus_justice' in speaker['roles']:
                self.justices.append(speaker)
            else:
                self.nonjustices.append(speaker)

    def random_speaker(self, last_speaker):
        if random.random() < 0.5:
            bucket = self.justices
        else:
            bucket = self.nonjustices
        speaker_ok = False
        while not speaker_ok:
            speaker = random.choice(bucket)
            if speaker != last_speaker:
                speaker_ok = True
        return speaker

class MarkovLineProvider(RandomSpeaker):

    def __init__(self, verbatim, speakers):
        super(MarkovLineProvider, self).__init__(speakers)
        self.verbatim = verbatim
        self.by_state = {}

    def load_state(self, state):
        markov = MarkovGenerator(order=2)
        if not state in self.verbatim.by_state:
            self.verbatim.load_state(state)
        for x in self.verbatim.by_state[state]:
            markov.add(x['text'])
        self.by_state[state] = markov

    def make_line(self, state, last_speaker):
        speaker = self.random_speaker(last_speaker)
        utterance = " ".join(self.by_state[state].assemble())
        return speaker, dict(
            text=utterance,
            interrupted=utterance.endswith('--')
        )

class QueneauLineProvider(RandomSpeaker):

    data_dir = "queneau"

    def __init__(self, verbatim, speakers):
        super(QueneauLineProvider, self).__init__(speakers)
        self.verbatim = verbatim
        self.by_state = {}

    def load_state(self, state):
        self.by_state[state] = Assembler(state, self.path(""))

    def make_line(self, state, last_speaker):
        speaker = self.random_speaker(last_speaker)
        utterance = self.by_state[state].assemble()
        if not utterance:
            self.verbatim.load_state(state)
            return self.verbatim.make_line(state, last_speaker)
        return speaker, dict(
            text=utterance,
            interrupted=utterance.endswith('--')
        )


class Argument(object):

    # start -> statetement: 7321
    # start -> question: 224
    # statement -> statement: 1967848
    # statement -> question -> 221881
    # interruption -> statement: 225456
    # interruption -> question: 50516
    # response -> statement: 262977
    # response -> question: 66788
    
    INTERRUPTED = "interrupted"
    INTERRUPTION = "interruption"
    QUESTION = "question"
    RESPONSE = "response"
    STATEMENT = "statement"
    STARTING_STATE = "start"
    ENDING_STATE = "final"
    transitions = {
        STARTING_STATE : [STATEMENT, QUESTION, 0.97],
        QUESTION : RESPONSE,
        INTERRUPTED : INTERRUPTION,
        STATEMENT : [STATEMENT, QUESTION, 0.90],
        INTERRUPTION : [STATEMENT, QUESTION, 0.82],
        RESPONSE: [STATEMENT, QUESTION, 0.583],
        ENDING_STATE: None
    }
    
    QUENEAU_CHANCE = 0.33
    MARKOV_CHANCE = 0.66

    def __init__(self, state=None, last_speaker=None):
        self.speakers = {}
        for i in open(LineProvider.data("speakers.ndjson")):
            data = json.loads(i)
            self.speakers[data['id']] = data

        self.verbatim = VerbatimLineProvider(self.speakers)
        self.queneau = QueneauLineProvider(self.verbatim, self.speakers)
        self.markov = MarkovLineProvider(self.verbatim, self.speakers)
        self.state = state or self.STARTING_STATE
        self.finished = False
        self.last_speaker = last_speaker

    def random_line(self):
        a = random.random()
        if a < self.QUENEAU_CHANCE:
            generator = self.queneau
        elif a < self.MARKOV_CHANCE:
            generator = self.markov
        else:
            generator = self.verbatim
        return generator.line(
            self.state, self.last_speaker
        )

    def pump(self):
        speaker, utterance = self.random_line()
        self.transition(speaker, utterance)
        return speaker, utterance        
    
    def transition(self, speaker, utterance):
        if self.state == self.ENDING_STATE:
            self.finished = True
            return

        if utterance['interrupted']:
            # Sometimes the speech act itself can put us into a different
            # state.
            self.state = self.INTERRUPTION
        else:
            # Most of the time the _type_ of speech act determines the
            # next state.
            possibilities = self.transitions[self.state]
            if isinstance(possibilities, str):
                self.state = possibilities
            else:
                ch1, ch2, prob = possibilities
                if random.random() < prob:
                    self.state = ch1
                else:
                    self.state = ch2
            if self.state == self.STATEMENT and random.randint(1,20) == 20:
                self.state = self.ENDING_STATE
        self.last_speaker = speaker

if __name__ == '__main__':
    argument = Argument()
    while not argument.finished:
        speaker, statement = argument.pump()
        name = speaker['last_name']
        if not name:
            name = "Unknown"
        if name.endswith(','):
            name = name[:-1]
        output = "%s: %s" % (name, statement['text'])
        print(output.encode("utf8"))
