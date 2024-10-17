import datetime

import requests

SHEET_API = "https://api.sheety.co/624fb4113e1046b7480d13b38198c1a2/passagensAéreas/página1"



# class DataManager:

response = requests.get(SHEET_API)
sheet_data = response.json()["página1"]
value_data = {item["city"]: item["lowestPrice"] for item in sheet_data}
iata_code = {item["city"]: item["code"] for item in sheet_data}
id_data = [item["id"] for item in sheet_data]
city_name = [item["city"] for item in sheet_data]



#FLIGHT DATA

FLIGHT_API = "https://api.tequila.kiwi.com/locations/query"

header = {
    "apikey": "-fTkPYvdjT3ydEKdNoZGnu9FY-_E0wH8"
}

params = {
    "term": ""
}

aita_code = []

for city in city_name:
    params["term"] = city
    response = requests.get(FLIGHT_API, params=params, headers=header)
    city_code = response.json()["locations"]
    aita_code.append(city_code[0]["code"])
# print(aita_code)

#DATA MANAGER

header = {
    "Content-Type": "application/json"
}

params = {
    "página1": {
        "code": ""
    }
}

numero = 0

def next_aita_code():
    global params
    global aita_code
    global numero
    params["página1"]["code"] = aita_code[numero]
    numero += 1


city_keys = list(value_data.keys())
for id in id_data:
    next_aita_code()
    update_sheet = requests.put(
        f"https://api.sheety.co/624fb4113e1046b7480d13b38198c1a2/passagensAéreas/página1/{id}",
        json=params, headers=header)
    # print(update_sheet.text)


#FLIGHT SEARCH

FLIGHT_API = "https://api.tequila.kiwi.com/v2/search"

date = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow = date.strftime("%d/%m/%Y")
six_months_date = datetime.datetime.now() + datetime.timedelta(days=6*30)
six_months_from_now = six_months_date.strftime("%d/%m/%Y")

header = {
    "apikey": "-fTkPYvdjT3ydEKdNoZGnu9FY-_E0wH8"
}

search_params = {
    "fly_from": "LON",
    "fly_to": "",
    "date_from": tomorrow,
    "date_to": six_months_from_now,

}

search_numero = 0

def next_city():
    global search_params
    global search_numero
    search_params["fly_to"] = aita_code[search_numero]
    search_numero += 1


for n in range(0, len(aita_code)):
    next_city()
    response = requests.get(FLIGHT_API, params=search_params, headers=header)
    data = response.json()
    print(f"{data['data'][0]['cityTo']}: £{data['data'][0]['price']}")
    if int(data['data'][0]['price']) < int(sheet_data["lowestPrice"]):
        #SEND EMAIL (não vou mexer com api de mensagem não)
