import os
import json
import random
from olipy.markov import MarkovGenerator
import re
from pdb import set_trace


class Fusion(object):

    base = os.path.split(__file__)[0]
    
    fusions = {
        "Smoky Quartz": ["Steven", "Amethyst"],
        "Rainbow Quartz": ["Rose", "Pearl"],
        "Opal": ["Amethyst", "Pearl"],
        "Sugilite": ["Amethyst", "Garnet"],
        "Alexandrite": ["Amethyst", "Garnet", "Pearl"],
        "Sardonyx": ["Garnet", "Pearl"],
        "Stevonnie": ["Steven", "Connie"],
#        "Malachite": ["Jasper", "Lapis"],
    }

    @classmethod
    def random(cls):
        return Fusion(random.choice(list(cls.fusions.keys())))
    
    def __init__(self, name):
        if name not in self.fusions:
            raise ValueError("Unknown fusion: %s")
        self.name = name
        self.dialogue = MarkovGenerator(order=1, max=200)
        self.directions = MarkovGenerator(order=1, max=7)
        
        members = list(self.fusions[name]) + [name]
        if 'Garnet' in members:
            members.append('Sapphire')
        for member in members:
            filename = member + ".json"
            data = json.load(open(self.path(filename)))
            for line in data.get('lines', []):
                self.dialogue.add(line)
            for line in data.get('actions', []):
                self.directions.add(line)
        
    def path(self, filename):
        return os.path.join(self.base, "data", filename)

    def assemble(self):
        data = self.dialogue.assemble()
        template = " ".join(data)
        while "%(direction)s" in template:
            d = " ".join(self.directions.assemble())
            template = template.replace("%(direction)s", d, 1)
        return self.cleanup(template)

    def cleanup(self, s):
        if s.count('*') % 2 == 1:
            s = re.compile("\*([^*]+)$").sub("\g<1>", s)
        if s.count('"') % 2 == 1:
            s = re.compile('"([^"]+)$').sub("\g<1>", s)

        for start, end in ('[]', '()', '{}'):
            if start in s and not end in s:
                s = s.replace(start, "")
            if end in s and not start in s:
                s = s.replace(end, "")
        for punc in '.!?])},;"':
            s = s.replace(" " + punc, punc)
        for punc in '({["':
            s = s.replace(punc + " ", punc)
        s = re.sub(" +", " ", s)
        return s
    

if __name__ == '__main__':
    for fusion in Fusion.fusions:
        avatar = os.path.join(Fusion.base, 'data', 'avatars', '%s.png' % fusion)
        if not os.path.exists(avatar):
            print("MISSING: %s" % avatar)
            break
    else:
        print("Avatars look good!")
    fusion = Fusion.random()
    print("%s says:" % fusion.name)
    for i in range(10):
        x = fusion.assemble()
        print(x)
