import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection("api.api-ninjas.com")
headers = {
    'X-Api-Key': os.getenv("API_NINJAS_KEY")
}


def get_joke():
    conn.request("GET", f"/v1/jokes", headers=headers)
    res = conn.getresponse()
    raw = res.read()
    data = json.loads(raw.decode())
    return data[0]["joke"]

def get_joke_of_day():
    conn.request("GET", f"/v1/jokeoftheday", headers=headers)
    res = conn.getresponse()
    raw = res.read()
    data = json.loads(raw.decode())
    return data[0]["joke"]
