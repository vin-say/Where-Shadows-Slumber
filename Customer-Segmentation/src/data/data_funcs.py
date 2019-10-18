# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:01:30 2019

@author: Vincent
"""

import os
from contextlib import contextmanager
import sqlalchemy as sa
import pandas as pd


@contextmanager
def cd(newdir):
    '''Safely move to a new directory, with guaranteed return to home
    
    https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
    '''
    
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def csv_to_sql(csv_dir, csv_name, db_dir, db_name, tab_name):
    '''Stores data from a .csv to a SQLite database.
    
    param csv_dir (Path object): directory containing .csv file
    param csv_name (str): name of .csv file
    param db_dir (Path object): directory containing SQLite database
    param db_name (str): name of SQLite database
    param tab_name (str): name of table into which .csv data is to be imported
    '''
    
    with cd(csv_dir):
        try:
            df = pd.read_csv(csv_name)
        except:
            raise Exception(csv_name + ' could not be found in the directory ' \
                            + os.getcwd())
    
    with cd(db_dir):
        e = sa.create_engine('sqlite:///' + db_name)
        # only create the table if it doesn't already exist
        if not e.dialect.has_table(e, tab_name):
            df.to_sql(tab_name, e)
        else:
            print('Table ' + tab_name + ' already exists in ' + db_name)