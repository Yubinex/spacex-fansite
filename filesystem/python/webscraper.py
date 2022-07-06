# Webscraper that updates the json files

import urllib.request
import json
import os


agencies = os.getcwd() + 'filesystem\json\\agencies.json'
launches = os.getcwd() + 'filesystem\json\launches.json'


def get_data():

    with urllib.request.urlopen('https://launchx.xenfuma.com/api/v1/launches') as launches_url:

        launches_data = json.loads(launches_url.read().decode())

    with urllib.request.urlopen('https://launchx.xenfuma.com/api/v1/agencies') as agencies_url:

        agencies_data = json.loads(agencies_url.read().decode())

    with open(launches, 'w') as f_obj:

        json.dump(launches_data, f_obj, indent=4)

    with open(agencies, 'w') as f_obj:

        json.dump(agencies_data, f_obj, indent=4)


get_data()
