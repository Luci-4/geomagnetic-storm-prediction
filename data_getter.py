import requests
import json
from dotenv import dotenv_values


base_url = "https://api.nasa.gov/DONKI/"
env_vars = dotenv_values()
api_key = env_vars["NASA_API_KEY"]
endpoint = "CME"

start_time = "2010-01-01"
page_size = 500
url = f"{base_url}{endpoint}?api_key={api_key}&startDate={start_time}&page_size={page_size}"

response = requests.get(url)
data = json.loads(response.text)

with open("cme_data.json", "w") as f:
    json.dump(data, f, indent=4)
