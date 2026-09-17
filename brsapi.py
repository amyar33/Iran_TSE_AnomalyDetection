import os
import requests
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BRS_API_KEY")


def get_bourse_data():

    url = f"https://Api.BrsApi.ir/Tsetmc/AllSymbols.php?key={API_KEY}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0"
        ),
        "Accept": "application/json, text/plain, */*"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data)

        return df

    else:
        print(f"Error: {response.status_code}")
        return None