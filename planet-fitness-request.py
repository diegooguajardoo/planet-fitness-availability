import requests
import json
from datetime import datetime
import csv
import os
import time

key = os.environ["PLANET_KEY"]


def get_data():
    '''Get the current crowd level of the gym.'''
    url = "https://v2.twinoaksadvantage.com/tosdapi/api/MemberInformation/GetCrowdLevel?clubId=3164"
    headers = {
        "Host": "v2.twinoaksadvantage.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://planetfitnessmxestanzuela.thememberspot.com/",
        "api_key": key,
        "content-type": "application/json",
        "Origin": "https://planetfitnessmxestanzuela.thememberspot.com",
        "DNT": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Connection": "keep-alive",
        "Priority": "u=1",
        "TE": "trailers"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data


def main():
    '''Write the data to a csv file.'''
    data = get_data()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('planet-fitness.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([date, data])


while True:
    time.sleep(1800)
    main()
