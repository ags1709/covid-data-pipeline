import requests
import pandas as pd
from io import StringIO

def fetch_covid_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    data = StringIO(response.text)
    df = pd.read_csv(data)
    return df