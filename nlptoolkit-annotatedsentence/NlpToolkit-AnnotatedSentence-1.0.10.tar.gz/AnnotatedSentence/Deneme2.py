from AnnotatedSentence.AnnotatedCorpus import AnnotatedCorpus
from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
corpus = AnnotatedCorpus("../../Etstur/Deneme")
for sentence in corpus.sentences:
    if isinstance(sentence, AnnotatedSentence):
        modified = False
        groupFound = None
        groups = sentence.getShallowParseGroups()
        for group in groups:
            word = group.getWord(0)
            if isinstance(word, AnnotatedWord) and word.getShallowParse() == "YÜKLEM" and group.wordCount() == 1:
                groupFound = group
        lastWord = sentence.getWord(sentence.wordCount() - 1)
        if lastWord.getName() == "." and groupFound is not None:
            index = sentence.getIndex(groupFound.getWord(0))
            print(sentence.toString() + "--->" + groupFound.getWord(0).getName() + "--->" + index.__str__())
            lastWord.setUniversalDependency(index + 1, "PUNCT")
            modified = True
    if modified:
        sentence.save()
