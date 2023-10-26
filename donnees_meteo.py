import requests
import json
import matplotlib.pyplot as plt

def get_weather_data():
    # URL de requête météo
    meteo_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&timezone=Europe%2FBerlin&start_date=2023-10-23&end_date=2023-10-27"

    response = requests.get(meteo_url)

    if response.status_code == 200:
        data = response.json()
        # Traitement des données ici
        print("Données météo mises à jour avec succès.",data)
        #Création Dataframe
        df_data=pd.Dataframe(data)
    else:
        print("Échec de la requête météo. Code d'état :", response.status_code)
get_weather_data()








        


