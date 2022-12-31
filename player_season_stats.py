import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

players_list = ["doncilu01","abdulka01"]

def get_season_averages_per_player(players_code_input):
    for p in players_code_input:
        print(p)
        playes_code = players_code_input
        playes_code_first_letter = p[0]
        request_url = f"https://www.basketball-reference.com/players/{playes_code_first_letter}/{p}.html"
        r = requests.get(request_url)
        soup = bs(r.content, "html.parser")
        print(soup.prettify)
        table = soup.select('table#per_game')[0]
        columns = table.find('thead').find_all('th') 
        #print(columns)
        table_df = pd.read_html(str(table))[0]
        print(table_df)
        table_json = table_df.to_json(orient="columns")
        os.makedirs('folder/subfolder', exist_ok=True)
        currentDateAndTime = datetime.now()
        print("The current date and time is", currentDateAndTime)
        filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")+"_"+p
        os.makedirs(f'folder/{p}', exist_ok=True)
        export_json2 = table_df.to_json(f'folder/subfolder/{filename1}.json')
        print(table_df)
    return table_df

get_season_averages_per_player(players_list)