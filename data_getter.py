import requests
import json
from dotenv import dotenv_values


base_url = "https://api.nasa.gov/DONKI/"
env_vars = dotenv_values()
api_key = env_vars["NASA_API_KEY"]

start_time = "2023-05-09"
page_size = 500
# CME


def dump_to_json(endpoint, filename=None):

    url = f"{base_url}{endpoint.upper()}?api_key={api_key}&startDate={start_time}&page_size={page_size}"
    response = requests.get(url)
    print(url)
    data = json.loads(response.text)
    if filename is None:
        filename = f"{endpoint.lower()}_data.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


dump_to_json("cme", "current_cme_data.json")
