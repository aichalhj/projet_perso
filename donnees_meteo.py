#Url de l'API:https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&past_days=5
#Cle API : ac7e5560a7b3ec4021bfb9592b708c0e

import requests

api_key=f'ac7e5560a7b3ec4021bfb9592b708c0e'
city:'Montpellier'

#URL de la requête 
url= f'https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&past_days=5'


headers = { 'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    #Les données metéorologiques vont être stokées dans data
    print(data)
else:
    print("Erreur lors de la requête: {response.status_code}")
