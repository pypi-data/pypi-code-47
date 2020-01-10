import nltk
import re
import string
ps=nltk.PorterStemmer()

def clean(text,all=False, extra_spaces=False, stemming=False, stopwords=False,lowercase=False, numbers=False, punct=False, stp_lang='english'):
	
	stop_words = nltk.corpus.stopwords.words(stp_lang)
	
	if text==None:
		text=''
	text=str(text)
	
	if all:
		text=re.sub('\s+', ' ', text).strip()
		text = "".join([word.lower() for word in text if word not in string.punctuation])
		text =re.sub("\d+", "", text)
		tokens = re.split('\s+', text)
		text = " ".join([ps.stem(word) for word in tokens if word not in stop_words])
		return text

	else:
		if extra_spaces:
			text=re.sub('\s+', ' ', text).strip()
		if lowercase:
			text = text.lower()
		if numbers:
			text =re.sub("\d+", "", text)
		if punct:
			text = "".join([word for word in text if word not in string.punctuation])

		if stopwords:
			text=re.split(" ",text)
			text=" ".join([word for word in text if word not in stop_words])
		if stemming:
			text=re.split(" ",text)
			text=" ".join([ps.stem(word) for word in text])

		return text
		
def clean_words(text,all=False, extra_spaces=False, stemming=False, stopwords=False,lowercase=False, numbers=False, punct=False, stp_lang='english'):
	
	stop_words = nltk.corpus.stopwords.words(stp_lang)
	
	if text==None:
		text=''
	text=str(text)
	
	if all:
		text=re.sub('\s+', ' ', text).strip()
		text = "".join([word.lower() for word in text if word not in string.punctuation])
		text =re.sub("\d+", "", text)       
		tokens = re.split('\s+', text)
		text = [ps.stem(word) for word in tokens if word not in stop_words]
		return text

	else:
		if extra_spaces:
			text=re.sub('\s+', ' ', text).strip()
		if lowercase:
			text = text.lower()
		if numbers:
			text =re.sub("\d+", "", text)
		if punct:
			text = "".join([word for word in text if word not in string.punctuation])

		if stopwords:
			text=re.split(" ",text)
			text=" ".join([word for word in text if word not in stop_words])
		if stemming:
			text=re.split(" ",text)
			text=" ".join([ps.stem(word) for word in text])

		return re.split('\s+', text)
		