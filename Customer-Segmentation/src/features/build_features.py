# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import sqlite3
import pandas as pd
import numpy as np
import nltk
import fasttext
from features_func import normalize_doc, lemmatize_doc

@click.command()
@click.argument('db_path', type=click.Path(exists=True))
@click.argument('interim_path', type=click.Path())
@click.argument('processed_path', type=click.Path())
def main(db_path, tab_name):
    """ Generates cleaned, lemmatized, and vectorized text to be used in 
        clustering algorithims
    """
    
    ###########################################################################
    #Grab data
    ###########################################################################    
    logger = logging.getLogger(__name__)
    logger.info('Reading from SQLite database')

    e = sa.create_engine('sqlite:///' + DB_PATH)
    query = 'SELECT * FROM ' + TAB_NAME
    users = pd.read_sql_query(query, e)

    ###########################################################################
    # Clean and lemmatize data
    ###########################################################################
    logger = logging.getLogger(__name__)
    logger.info('Cleaning and lemmatization of text')

    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend(['co', 'https', 'http', 'gmail', 'com', 'like', 'love'])

    users['clean_desc'] = users['description'].map(lambda doc: normalize_doc(doc, stop_words) 
                                                if doc == doc 
                                                else np.nan)

    # import and apply FastText model for language identification
#    idlang_path = Path('fasttext_training_data', 'lid.176.bin')
    idlang_path = Path('.data/external/fasttext_training_data/lid.176.bin')
    idlang_model = fasttext.FastText.load_model(idlang_path)
    
    users['lang_id'] = users['clean_desc'].map(lambda doc: idlang_model.predict(doc) 
                                                if doc == doc 
                                                else np.nan)
    
    # only English profiles are lemmatized; empty profiles are also ignored
    users['clean_desc_en'] = users.apply(lambda row: lemmatize_doc(row['clean_desc']) 
                                            if  row['lang_id'] == row['lang_id']
                                            and row['lang_id'][0][0] == '__label__en'
                                            and row['clean_desc'] == row['clean_desc'] 
                                            else np.nan,
                                            axis=1)
    
    ###########################################################################
    # upload cleaned data set to database
    ###########################################################################
    e = sa.create_engine('sqlite:///db_path' + '_cleaned)
    # only create the table if it doesn't already exist
    if not e.dialect.has_table(e, tab_name):
        df.to_sql(tab_name, e)
    else:
        print('Table ' + tab_name + ' already exists in ' + db_name)
    

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
