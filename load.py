import pandas as pd
from sqlalchemy import create_engine
import json
import logging

logging.basicConfig(filename='load.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s' )
logging.info('Starting...')

cred = "credentials.json"
data = "dados_prova.txt"


# loading credentials

with open(cred) as f:
    cred = json.load(f)


def load_data_dataframe(data):
    ''' loads data from local directory to the dataframe.
        insert those rows to a postgres database according to the
        credentials file'''
    df = pd.read_csv("../subfolder/20221231-195033_mcgratr01.csv", header=0, sep=',', engine='python')
    filtered_df = df[0].str.startswith(searched_term, na=False)
    return df[filtered_df]


def load_data_to_psql():
    engine = create_engine(cred["URL"])
    df = pd.read_csv("/home/chic/deletavel/tik_basketball_reference_scraping/folder/subfolder/20221231-195033_mcgratr01.csv", header=None, sep=r'\s{2,}', engine='python')
    df.to_sql("dados_prova1", engine,if_exists='append', chunksize=1000)
    return True


load_data_to_psql()