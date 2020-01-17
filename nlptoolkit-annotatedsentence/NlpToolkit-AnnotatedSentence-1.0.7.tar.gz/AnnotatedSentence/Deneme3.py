from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag
corpus = AnnotatedCorpus("../../Etstur/Turkish-Phrase")
for sentence in corpus.sentences:
    if isinstance(sentence, AnnotatedSentence):
        modified = False
        ozneGroup = None
        yuklemGroup = None
        groups = sentence.getShallowParseGroups()
        for group in groups:
            word = group.getWord(0)
            if isinstance(word, AnnotatedWord) and word.getShallowParse() == "ÖZNE" and group.wordCount() == 1:
                ozneGroup = group
            if isinstance(word, AnnotatedWord) and word.getShallowParse() == "YÜKLEM" and group.wordCount() == 1:
                yuklemGroup = group
        if ozneGroup is not None and yuklemGroup is not None:
            yuklemWord = yuklemGroup.getWord(0)
            if isinstance(yuklemWord, AnnotatedWord) and yuklemWord.getParse() is not None and not yuklemWord.getParse().containsTag(MorphologicalTag.PASSIVE):
                ozneWord = ozneGroup.getWord(0)
                index = sentence.getIndex(yuklemGroup.getWord(0))
                print(sentence.toString() + "--->" + yuklemGroup.getWord(0).getName() + "--->" + ozneGroup.getWord(0).getName())
                ozneWord.setUniversalDependency(index + 1, "NSUBJ")
