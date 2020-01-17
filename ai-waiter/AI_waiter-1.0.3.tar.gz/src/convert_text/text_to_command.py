
from nltk import word_tokenize
from statistics import mode

import sys
sys.path.append('../../')
from src.convert_text.get_menu_items import lemmatize_text, clean_text, remove_stopwords
from src.configs.config import filenames

import textwrap
import json
import ast
from collections import Counter
import pandas as pd
import random
import nltk
import sqlalchemy
import random
from datetime import datetime
import urllib3, time
import requests
import json
from random import randint
#from word2number import w2n

import sqlalchemy


def clean_speech(text):
    """
    Cleans the speech to text conversione

    Args:
        text : string of text converted from speech
    
    Returns:
        new_text : list of strings
    """

    new_text = clean_text(text)
    return lemmatize_text(new_text)

def search_for_general_item(text, menu):
    """
    search the cleaned text for an item on the menu

    Args:
        text : speech converted into text
        menu : menu data from csv file

    Return:
        item_idx (int): possible indices of menu item
        x : corresponding menu item
    """

    # is the general term in the order?
    general_terms = menu['General term'].unique()
    
    possible_items = []
    for w in text:
       possible_items = possible_items + [x for x in general_terms if w in x]

    # count most frequently occuring item
    if possible_items != []:
        try:
            item = mode(possible_items)
        except:
            print("more than one possible item")
    else:
        item = []

    return item

def search_for_specific_item(text, menu):
    """
    matches the indices for the general item to a specific item

    Args:
        text : speech converted to text
        menu : menu dataframe
        idx : list of possible general items

    TODO: need to improve so it matches up exact word for word

    """


    specific_items = menu['Specific term'].apply(lambda x: remove_stopwords(x))

    print(specific_items)
    possible_items = []
    print('text = ',text)
    for w in text:
        possible_items += [x for x in specific_items if w in x]
    
    if possible_items == []:
        print('no match to specific item found')
        return []
    else:
        try:
            return mode(possible_items)
        except:
            print("More than one possible item")
            print(possible_items)
            return []

def match_item_to_order(text, menu):
    """
    instead of seraching for an item in the text, search through all the items
    to see if they appear in the text
    """

    # clean specific items
    menu['Specific term'] = menu['Specific term'].apply(lambda x: remove_stopwords(x))
    text = word_tokenize(remove_stopwords(' '.join(text)))
    possible_items = []
    count_terms = []
    for term in menu['Specific term']:
        count = 0
        for token in word_tokenize(term):
            if any(token == w for w in text):
                count +=1
        if count != 0:
            possible_items.append(term)
            count_terms.append(count)

    if possible_items == []:
        return []
    else:
        try:
            return mode(possible_items)
        except:
            print('count_terms = ',count_terms)
            print('possible_items = ', possible_items)
            idx = count_terms.index(max(count_terms))
            for i in range(len(count_terms)):
                if i != idx:
                    if count_terms[i] == max(count_terms):
                        return 'not sure'
            return possible_items[idx]
            

def search_for_quantity(text,menu, item_index):

    # TODO : find numeric values
    quantity_list = menu['Quantities'].loc[item_index]
    quantity = ([w for w in text if w in quantity_list])

    return quantity

def search_for_number(text):

    pos = nltk.pos_tag(text)
    for i in range(len(pos)):
        word, pos_tag = pos[i]
        if pos_tag == 'CD':
            return word    
    else:
        return 'one'

def get_alternative_text(audio, recognizer):

    alt_dict = recognizer.recognize_google(audio, show_all = True)
    alternatives = alt_dict['alternative']
    transcript = []
    for i in alternatives:
        transcript.append(i['transcript'])
    return transcript

def final_order(order_data, timestamp):
    """
    determine final order, as most likely translation
    """
    max_items = max(order_data['sentence_id'])
    order_itemid = []
    order_table = []
    order_items = []
    order_quantity = []
    order_timestamp = []
    order_number = []

    # iterate through item orders
    for i in range(max_items + 1):

        # find item
        item_list = order_data[order_data['sentence_id'] == i]['item'].values
        # if all items are the same, choice is obvious
        if all(x == item_list[0] for x in item_list):
            item = item_list[0]
        else:
            # TODO : find most commonly occuring item
            try:
                item = mode(item_list)
                if item == 'not sure':
                        item = mode(item_list[item_list != 'not sure'])
            except:
                item = item_list[0]
                
        
        # find quantity
        quantity_list = order_data[order_data['sentence_id'] == i]['quantity'].values
        try:
            quantity_list = [q[0] for q in quantity_list]
            if all(x == quantity_list[0] for x in quantity_list):
                quantity = quantity_list[0]     
            else:
                try:
                    quantity = mode(quantity_list)
                except:
                    quantity = quantity_list[0]
        except:
            quantity = 'missing quantity'


        # find number
        number_list = order_data[order_data['sentence_id'] == i]['number'].values
        try:
            if all(x == number_list[0] for x in number_list):
                number = number_list[0]
            else:
                number = float('NaN')
        except:
            number = float('NaN')

        order_itemid.append(random.randint(1000,2000))
        order_items.append(item)
        order_quantity.append(quantity)
        order_timestamp.append(timestamp)
        order_table.append(0)
        order_number.append(number)

        # TODO : what if not all items/quantites are the same? How to pick most likely order

    #Counts how many times the script has ran to give a unique item ID
    def get_var_value(filename="varstore.dat"):
        with open(filename, "a+") as f:
            f.seek(0)
            val = int(f.read() or 0) + 1
            f.seek(0)
            f.truncate()
            f.write(str(val))
            return val

    your_counter = get_var_value()
    
    final_order_dict = {'OrderID': your_counter
                        ,'TableNo': random.randint(1,25)
                        ,'ItemID': order_itemid
                        ,'Item': order_items
                        ,'Quantity': order_quantity
                        ,'Number': order_number
                        ,'Time': order_timestamp}
    final_order_data = pd.DataFrame(final_order_dict)
    print(final_order_data)
    return final_order_data

def main(audio, timestamp, recognizer, menu):
    """
    Args:
        audio : output from SpeechConvert()
        recognizer : speech recognition class
        menu : dataframe containing menu information

    returns
        command
    """

    # get text and clean - look for alternatives
    speech_list = get_alternative_text(audio, recognizer)
    #speech_text = 'could i get a large glass of pinot grigio and a small glass of sauvignon blanc'

    

    order_list = []
    sentence_list = []
    item_list = []
    order_id = []
    sentence_id = []
    quantity_list = []
    number_list = []
    for i, speech_text in enumerate(speech_list):
    # split order into sentences with the word 'and'
        print('whole order = ',speech_text)
        print("")
        order = []
        speech = speech_text.split('and')
        
        for j, sentence in enumerate(speech):

            print('sentence =', sentence)
            new_text = clean_speech(sentence)
            new_text = remove_stopwords(new_text)
            if len(new_text) == 1:
                print("only one word found")
                sys.exit()
            
            new_text = word_tokenize(new_text)

            # try and find specific item
            item_name = match_item_to_order(new_text, menu)
            

            # if specific item found, search for quantity
            if item_name != []:
                try:
                    item_index = menu.loc[menu['Specific term'] == item_name].index[0] # if multiple items
                    quantity = search_for_quantity(new_text, menu, item_index)
                except:
                    quantity = 'item not clear'
            else:
            # if specific item not found perhaps ordering a general item?
                general_item = search_for_general_item(new_text, menu)

            number = search_for_number(new_text)
            
            

            print('Item: ', item_name, '. Quantity: ', quantity)
            print("")
            order.append([item_name, quantity])

            order_list.append(speech_text)
            sentence_list.append(sentence)
            item_list.append(item_name)
            sentence_id.append(j)
            order_id.append(i)
            quantity_list.append(quantity)
            number_list.append(number)


        print("--------------------")
        if order != []:
            exit

    # save order to file

    save_dir = filenames.order_dir
    filename = 'full_order.csv'
    dct = {'translation_id' : order_id
            ,'sentence_id' : sentence_id
            ,'order' : order_list
            ,'sentence' : sentence_list
            ,'item' : item_list
            ,'quantity': quantity_list
            ,'number' : number_list}
    full_order_data = pd.DataFrame(dct)
    full_order_data.to_csv(save_dir + filename)
    order = final_order(full_order_data, timestamp)
    order.to_csv(save_dir + 'final_order.csv', index = False)

    ###########################
    #Save order to SQL table
    engine = sqlalchemy.create_engine(
        "mssql+pyodbc://altius:alt.ius01@demodatasets.database.windows.net/DemoDatasets?driver=SQL+Server")
    order.to_sql(name='orders', con=engine, if_exists='append', index=False)
    print('order saved')

    return None
