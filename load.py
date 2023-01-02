import pandas as pd
from sqlalchemy import create_engine
import json
import logging
from datetime import date,datetime
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

def load_data_to_psql(folder,day="2022-01-01"):
    print(day)
    logging.info('Creating Engine')
    engine = create_engine(cred["URL"])
    logging.info("Avaialble files in folder: " + str(os.listdir(folder)))
    print(os.listdir(folder))
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
    # checking if it is a file
        if os.path.isfile(f):
            print(f"Loading {f}")
            shear = f.split('_')[0]
            shear2 = shear.split('/')[3]
            if shear2 == day:
                print(f"File {f} is apropriate for the requested date.")
            else:
                print(f"File {f} is not for requested date.")
            df = pd.read_csv(f)
            df['loaded_at']= datetime.today().strftime('%Y-%m-%d')
            df.columns= df.columns.str.strip().str.lower()
            table = (f"daily_current_seasonal_stats")
            df.to_sql(table, engine,if_exists='replace', chunksize=1000)
            logging.info(f'Loaded {f} to database in table {table}')
    logging.info('End of loading')
    return True


load_data_to_psql("./folder/subfolder",datetime.today().strftime('%Y-%m-%d'))
logging.info('Finished.')
def check_name(folder,day):
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
    # checking if it is a file
        if os.path.isfile(f):
            print(f)
        shear = f.split('_')[0]
        print(shear)    # split the filename and grab the second part
        shear2 = shear.split('/')[3]
        print(shear2)
        if shear2 == day:
            print("feliz")
        else:
            print("ainda nao")
# check_name("./folder/subfolder","2023-01-02")