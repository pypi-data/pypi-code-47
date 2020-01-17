from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
corpus = AnnotatedCorpus("../../Etstur/Turkish-Phrase")
for sentence in corpus.sentences:
    modified = False
    if isinstance(sentence, AnnotatedSentence):
        phraseGroups = sentence.getShallowParseGroups()
        yuklemler = []
        for group in phraseGroups:
            if group.getTag() == "YÜKLEM":
                yuklemler.append(group)
        sonYuklem = yuklemler.pop()
        if sonYuklem.wordCount() == 1:
            sonYuklem.getWord(0).setUniversalDependency(0, "ROOT")
            print(sentence.toString() + "->" + sonYuklem.toString())
