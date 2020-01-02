import re
from nltk import sent_tokenize
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
import spacy
import math


class Validator:
    
    html_pattern = re.compile("<.*?>")
    non_letter_pattern = re.compile("[^a-zA-Z'\-]")

    def __init__(
        self,
        nlp_obj,
        sentence_token_limit=1024,
        ignore_html=True,
    ):
        self.sentence_token_limit = sentence_token_limit
        self.ignore_html = ignore_html
        self.IGNORE_TOKENS = []
        self.nlp_obj = self.confirm_nlp(nlp_obj)
        self.tokenizer=Tokenizer(self.nlp_obj.vocab)

    def confirm_nlp(self,nlp_obj):
        return nlp_obj if nlp_obj else English()


    def has_html(self, segment:str):
        return self.html_pattern.match(segment)!=None
    
    def has_non_letter(self, segment:str):
        return self.non_letter_pattern.match(segment)!=None

    def is_empty(self, segment:str):
        return len(segment.strip())==0

    def too_long(self, segment:str):
        if len(sent_tokenize(segment))==1:     
            if len(segment.strip().split())>self.sentence_token_limit:
                return True
        return False


    # test here if there are any GRBAGE tokens or IGNORE tokens
    def test_garbage(self,segment:str):    

        if self.ignore_html and self.has_html(segment) is True:
            return True 

        # filter out whitespaces, empty segments
        if self.is_empty(segment):
            return True

        # filter out too long of a segment
        if self.too_long(segment):
            return True
        
        return False

    def test_ignore(self, segment:str):

        for token in self.tokenizer(segment):            
            # check is URL 
            if token.like_url:
                self.IGNORE_TOKENS.append(token.text)

            # check if has "="sign
            elif "=" in token.text:
                self.IGNORE_TOKENS.append(token.text)

            # check if has non-letter character
            elif self.has_non_letter(token.text):
                self.IGNORE_TOKENS.append(token.text)
        
        return self.IGNORE_TOKENS


    def __call__(self, segment:str):
        self.IGNORE_TOKENS = []

        # filter out if GARBAGE_TOKENS has members
        if self.test_garbage(segment):
            return False 

        self.IGNORE_TOKENS=self.test_ignore(segment)

        # filter too many IGNORE tokens
        if len(self.IGNORE_TOKENS) >= math.floor(0.5*len(segment.strip().split())):
            return False
        
        return True

