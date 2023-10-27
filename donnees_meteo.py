import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import datetime

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
        sunrice=data ["daily"]["sunrise"]
        windspeed=data ["daily"]["windspeed_10m_max"]
        sunset=data ["daily"]["sunset"]
        
        
    else:
        print("Échec de la requête météo. Code d'état :", response.status_code)
get_weather_data()

'''
associer des icones à la méteo
# Supposons que 'data' contienne les données météo avec le code de condition météorologique.
condition_code = data['conditionCode']

# Associez le code de condition météorologique à un fichier d'icône correspondant.
icone_meteo = None
if condition_code == 800:
    icone_meteo = 'soleil.svg'
elif condition_code == 801:
    icone_meteo = 'partiellement-nuageux.svg'
# Ajoutez d'autres cas selon vos besoins.

# Mettez à jour le chemin de l'icône appropriée.
if icone_meteo:
    chemin_icone = icone_meteo
    print(f'Chemin de l\'icône météo : {chemin_icone}')
else:
    print('Code de condition inconnu.')'''

'''import datetime

# Obtenez la date actuelle.
date_actuelle = datetime.date.today()

# Calculez la date de fin (5 jours à partir de la date actuelle).
date_fin = date_actuelle + datetime.timedelta(days=5)

# Formattez les dates au format AAAA-MM-JJ.
date_debut_str = date_actuelle.strftime('%Y-%m-%d')
date_fin_str = date_fin.strftime('%Y-%m-%d')

# Construisez l'URL avec les dates mises à jour.
base_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&timezone=Europe%2FBerlin"
url = f"{base_url}&start_date={date_debut_str}&end_date={date_fin_str}"

print(url)'''








        


