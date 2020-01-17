import pandas as pd
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, LancasterStemmer
"""
TODO: return most likely specific quantity to make sure that
the term with the highest number of tokens is returned.

clean speech text, so that e.g. fritz-kola -> fritz kola
"""




def clean_text(text):   
    text = str(text).lower() #lowercase
    text = re.sub('\'s', 's', text)
    text = re.sub('\’s', 's', text)
    text = re.sub('\W', ' ', text) #remove punctuation
    text = re.sub('\d+','', text) #remove digits 
    text = re.sub('\s+', ' ', text) #remove whitespace
    text = text.strip(' ')
    return text

def remove_stopwords(text):
    stop_words = stopwords.words('english')

    # add words to stopwords
    add_words = ['de', 'la', 'order', 'could']
    stop_words += add_words
    word_tokens = word_tokenize(text)
    filtered = [w for w in word_tokens if not w in stop_words]
    return ' '.join([w for w in filtered])

def lemmatize_text(text):
    # Lemmatizing
    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in text.split()])
    
    #Stemming
    #stemmer = LancasterStemmer()
    #stemmed_words = [stemmer.stem(word) for word in text]
    #text = " ".join(stemmed_words)
    
    return lemmatized_output

def get_quantities(menu):
    """
    separate items in quantity columns into a list
    """

    new_quant = []
    for q in menu['Quantities']:
        try:
            new_quant.append(q.split(', '))
        except:
            new_quant.append([])
    menu['Quantities'] = new_quant

    return menu


def main(menu_file):
    """
    menu file is a csv file containing the menu items
    """

    data = pd.read_csv(menu_file, encoding = 'utf-8')
    data.rename(columns={data.columns[1]: "Specific term"}, inplace=True)

    data["Further details"] = data["Further details"].apply(clean_text)
    data = get_quantities(data)
    data['Quantities'] = data['Quantities'].apply(clean_text)
    data["General term"] = data["General term"].apply(clean_text)
    data["Specific term"] = data["Specific term"].apply(clean_text)

    data["description_tokens"] = data["Further details"].apply(word_tokenize)
    #data["quantities_tokens"] = data["Quantities"].apply(word_tokenize)
    data["general_tokens"] = data["General term"].apply(word_tokenize)
    data["specific_tokens"] = data["Specific term"].apply(word_tokenize)

    data["all_tokens"] = data["specific_tokens"] + data["general_tokens"] + data["description_tokens"]

    data.to_csv('menu_data.csv')
    return data

if __name__ == "__main__":
    menu_file = ('../menus/menu.csv')
    tokenized_data = main(menu_file)
    print(tokenized_data.head())