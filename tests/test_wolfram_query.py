import httpx
import os
import xml.etree.ElementTree as ET
from sympy import symbols, Eq, solve, sqrt, simplify

def test_query_wolfram(query, app_id):
    url = "https://api.wolframalpha.com/v2/query"
    params = {
        "appid": app_id,
        "input": query,
        "format": "plaintext"
    }
    response = httpx.get(url, params=params)
    if response.status_code != 200:
        raise RuntimeError(f"API call failed with status {response.status_code}")

    root = ET.fromstring(response.text)
    plaintext = root.find(".//plaintext")
    return plaintext.text.strip() if plaintext is not None else None
