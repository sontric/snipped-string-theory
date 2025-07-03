import httpx
import os
import xml.etree.ElementTree as ET

def query_wolfram(query, app_id):
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

def test_e_mc2_query():
    app_id = os.getenv("WOLFRAM_APP_ID", "REPLACE_ME")
    if app_id == "REPLACE_ME":
        assert False, "Set WOLFRAM_APP_ID as an environment variable"

    result = query_wolfram("mass energy equivalence", app_id)
    assert result is not None, "No result returned from WolframAlpha"

    result_norm = result.lower().replace("–", "-").replace("—", "-").strip()

    assert (
        "e = mc" in result_norm
        or "mass-energy equivalence" in result_norm
        or "mass energy equivalence" in result_norm
    ), f"Unexpected result: {result}"
