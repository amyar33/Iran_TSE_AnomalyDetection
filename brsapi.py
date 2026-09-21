import os
import requests
import pandas as pd
from requests.exceptions import RequestException, SSLError

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BRS_API_KEY")
API_URL = "https://api.brsapi.ir/Tsetmc/AllSymbols.php"


def get_bourse_data():
    if not API_KEY:
        raise RuntimeError("BRS_API_KEY is not set in the .env file.")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0"
        ),
        "Accept": "application/json, text/plain, */*"
    }

    try:
        response = requests.get(
            API_URL,
            params={"key": API_KEY},
            headers=headers,
            timeout=(10, 60),
        )
        response.raise_for_status()
        data = response.json()
    except SSLError:
        raise RuntimeError(
            "BrsApi SSL certificate validation failed. "
            "The provider's certificate may be temporarily misconfigured."
        ) from None
    except ValueError:
        raise RuntimeError("BrsApi returned an invalid JSON response.") from None
    except RequestException as exc:
        status = exc.response.status_code if exc.response is not None else None
        detail = f" (HTTP {status})" if status is not None else ""
        raise RuntimeError(f"Could not fetch data from BrsApi{detail}.") from None

    if not isinstance(data, list):
        raise RuntimeError("BrsApi returned an unexpected response format.")

    return pd.DataFrame(data)
