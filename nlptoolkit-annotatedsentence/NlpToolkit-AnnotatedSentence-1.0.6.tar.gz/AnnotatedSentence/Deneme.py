from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
corpus = AnnotatedCorpus("../../Etstur/Deneme")
for i in range(corpus.sentenceCount()):
    sentence = corpus.getSentence(i)
    if isinstance(sentence, AnnotatedSentence):
        groups = sentence.getShallowParseGroups()
        for j in range(len(groups)):
            word = groups[j].getWord(0)
            if isinstance(word, AnnotatedWord):
                if word.getShallowParse() == "YÜKLEM" and groups[j].wordCount() == 1:
                    word.setUniversalDependency(0, "root")
                    print(word.getUniversalDependency())