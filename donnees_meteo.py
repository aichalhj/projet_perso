import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

def get_weather_data():
    # URL de requête météo
    meteo_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&timezone=Europe%2FBerlin&start_date=2023-10-23&end_date=2023-10-27"

    response = requests.get(meteo_url)

    if response.status_code == 200:
        data = response.json()
        # Traitement des données ici
        print("Données météo mises à jour avec succès.",data)
        #Création Dataframe
        df_data=pd.DataFrame(data)
        pd.set_option("display.max_rows",None)
        #Création d'un CSV associé
        df_data.to_csv("df_data.csv",index=False)
        #Extraction des données
        tempmax=data["daily"]["temperature_2m_max"]
        tempmin=data["daily"]["temperature_2m_min"]
        sunrice=data ["daily"]["sunrice"]
        windspeed=data ["daily"]["windspeed_10m_max"]
        sunset=data ["daily"]["sunset"]
        
    else:
        print("Échec de la requête météo. Code d'état :", response.status_code)
get_weather_data()








        


