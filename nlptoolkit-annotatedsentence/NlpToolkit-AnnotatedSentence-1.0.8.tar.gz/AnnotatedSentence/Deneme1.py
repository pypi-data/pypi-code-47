from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
corpus = AnnotatedCorpus("../../Etstur/Deneme")
for sentence in corpus.sentences:
    modified = False
    if isinstance(sentence, AnnotatedSentence):
        groups = sentence.getShallowParseGroups()
        for group in groups:
            word = group.getWord(0)
            if isinstance(word, AnnotatedWord) and word.getUniversalDependency() is None:
                if word.getShallowParse() == "YÜKLEM" and group.wordCount() == 1:
                    word.setUniversalDependency(0, "ROOT")
                    modified = True
    if modified:
        sentence.save()


