import os
from datetime import datetime
import logging

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

logging.basicConfig(filename='player_season_stats.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(levelname)-8s %(message)s' )
logging.info('Starting...')

players_list = ["doncilu01","abdulka01","mcgratr01","poeltja01","johnsma02"]

def get_season_averages_per_player(players_code_input):
    count = 0
    for p in players_code_input:
        logging.info('Starting run...')
        logging.info("Getting season stats for: "+str(p))
        playes_code = players_code_input
        playes_code_first_letter = p[0]
        request_url = f"https://www.basketball-reference.com/players/{playes_code_first_letter}/{p}.html"
        r = requests.get(request_url)
        soup = bs(r.content, "html.parser")
        table = soup.select('table#per_game')[0]
        columns = table.find('thead').find_all('th') 
        table_df = pd.read_html(str(table))[0]
        table_df['extracted+at']= datetime.today().strftime('%Y-%m-%d')
        table_df['players_code']= p
        table_json = table_df.to_json(orient="columns")
        os.makedirs('folder/subfolder', exist_ok=True)
        currentDateAndTime = datetime.now()
        filename1 = datetime.now().strftime("%Y%m%d-%H")+"_"+p
        os.makedirs(f'folder/', exist_ok=True)
        # export_json2 = table_df.to_json(f'folder/subfolder/{filename1}.json')
        export_json2 = table_df.to_csv(f'folder/subfolder/{filename1}.csv')
        logging.info("Extracted Season stats for: "+str(p))
        count +=1
        print(f"{count}.Finished for: "+str(p))
    logging.info("End of run.")
    return table_df

get_season_averages_per_player(players_list)
