#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

import datetime

SHEET_API = "https://api.sheety.co/624fb4113e1046b7480d13b38198c1a2/passagensAéreas/página1"



# class DataManager:

response = requests.get(SHEET_API)
sheet_data = response.json()
print(sheet_data)