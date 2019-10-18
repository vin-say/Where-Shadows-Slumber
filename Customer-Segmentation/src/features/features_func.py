# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:41:30 2019

@author: Vincent
"""

import nltk
import re
import numpy as np
import spacy



def normalize_doc(doc, stop_words):
    ''' Cleans text to prepare for vectorization
    
    param doc (list): raw text
    param stop_words (list): stopwords to filter out

    return doc (list): cleaned text
    '''
    # remove special characters, single characters and white space. This filters out non-arabic languages!!
    doc = re.sub(r'[^a-zA-Z\s]', ' ', doc, re.IGNORECASE|re.ASCII) #r'[^a-zA-Z0-9\s]'
    doc = re.sub(r'\b[a-zA-Z]\b', '', doc, re.IGNORECASE|re.ASCII)
    # remove whitespace at beginning and end of string
    doc = doc.strip()
    # convert all characters to lowercase
    doc = doc.lower()
    # tokenize document
    tokens = nltk.word_tokenize(doc)
    # remove stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # recreate doc from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

nlp = spacy.load('en') #download 'small' version of english model

def lemmatize_doc(nlp_model, doc):
    ''' Lemmatizes text to prepare for vectorization. Pronouns cannot be lemmatized.
    
    param doc: raw text
    param nlp_model(spaCy model):
    
    return doc: lemmatized text    
    '''
    doc = nlp(doc)
    doc = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in doc])
    return doc