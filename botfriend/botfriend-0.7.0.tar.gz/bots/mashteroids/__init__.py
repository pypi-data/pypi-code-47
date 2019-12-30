from botfriend.bot import TextGeneratorBot
from olipy.queneau import Assembler, WordAssembler
from olipy import corpora


class AsteroidBot(TextGeneratorBot):

    def __init__(self, *args, **kwargs):
        super(AsteroidBot, self).__init__(*args, **kwargs)
        asteroids = corpora.science.minor_planet_details['minor_planets']
        self.corpus = Assembler.loadlist(asteroids, tokens_in='citation')

    def generate_text(self):
        citation = ''
        while not citation or len(citation) > 490:
            citation = self.citation()
        return citation

    def citation(self):
        sentences = []
        names = []

        for sentence, source in self.corpus.assemble("f.l", min_length=3):
            sentences.append((sentence, source))
            names.append(source['name'])
        name_assembler = WordAssembler(names)
        sentences = sentences
        name = name_assembler.assemble_word()
        citation = " ".join([x[0] for x in sentences])
        return "%s: %s" % (name, citation)
Bot = AsteroidBot
