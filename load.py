import pandas as pd
from sqlalchemy import create_engine
import json
import logging
from datetime import date
import os

logging.basicConfig(filename='load.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s' )
logging.info('Starting...')

cred = "credentials.json"
# loading credentials
with open(cred) as c:
    logging.info('Fetching Credentials...')
    cred = json.load(c)
    logging.info('Credential loaded...')

today = date.today()

def load_data_to_psql(folder):
    logging.info('Creating Engine')
    engine = create_engine(cred["URL"])
    logging.info("Avaialble files in folder: " + str(os.listdir(folder)))
    print(os.listdir(folder))
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
    # checking if it is a file
        if os.path.isfile(f):
            print(f)
            df = pd.read_csv(f)
            print(df)
            table = "daily_seasonal_stats"
            df.to_sql(table, engine,if_exists='append', chunksize=1000)
            logging.info(f'Loaded {f} to database in table {table}')
    logging.info('End of loading')
    return True


load_data_to_psql("./folder/subfolder")
logging.info('Finished.')