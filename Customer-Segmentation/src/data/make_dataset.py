# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from data_funcs import csv_to_sql


@click.command()
@click.argument('raw_path', type=click.Path(exists=True))
@click.argument('interim_path', type=click.Path())
@click.argument('processed_path', type=click.Path())
def main(raw_path, interim_path, processed_path):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


#    csv_dir = Path(root_dir + 'data/raw/')
    csv_name = 'ustwo_followers.csv'
#    db_dir = Path(root_dir + 'data/interim')
    db_name = 'customer-segmentation.sqlite'
    tab_name = 'ustwo_followers'
#    
    csv_to_sql(csv_dir=raw_path, csv_name=csv_name, db_dir=interim_path, 
               db_name=db_name, tab_name=tab_name)
    print('raw_path')
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
