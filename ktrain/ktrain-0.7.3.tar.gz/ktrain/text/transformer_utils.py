from transformers import BertConfig, TFBertForSequenceClassification, BertTokenizer
from transformers import XLNetConfig, TFXLNetForSequenceClassification, XLNetTokenizer
from transformers import XLMConfig, TFXLMForSequenceClassification, XLMTokenizer
from transformers import RobertaConfig, TFRobertaForSequenceClassification, RobertaTokenizer
from transformers import DistilBertConfig, TFDistilBertForSequenceClassification, DistilBertTokenizer
from transformers import AlbertConfig, TFAlbertForSequenceClassification, AlbertTokenizer
from transformers import CamembertConfig, TFCamembertForSequenceClassification, CamembertTokenizer

TRANSFORMER_MODELS = {
    'bert':       (BertConfig, TFBertForSequenceClassification, BertTokenizer),
    'xlnet':      (XLNetConfig, TFXLNetForSequenceClassification, XLNetTokenizer),
    'xlm':        (XLMConfig, TFXLMForSequenceClassification, XLMTokenizer),
    'roberta':    (RobertaConfig, TFRobertaForSequenceClassification, RobertaTokenizer),
    'distilbert': (DistilBertConfig, TFDistilBertForSequenceClassification, DistilBertTokenizer),
    'albert':     (AlbertConfig, TFAlbertForSequenceClassification, AlbertTokenizer),
    'camembert':  (CamembertConfig, TFCamembertForSequenceClassification, CamembertTokenizer)
}

