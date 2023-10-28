import requests
import json
from PIL import Image
import pandas as pd
import datetime

def get_weather_data():
    #Obtenez la date actuelle.
    date_actuelle = datetime.date.today()

    # Calculez la date de fin (5 jours à partir de la date actuelle).
    date_fin = date_actuelle + datetime.timedelta(days=5)

    # Formattez les dates au format AAAA-MM-JJ.
    date_debut_str = date_actuelle.strftime('%Y-%m-%d')
    date_fin_str = date_fin.strftime('%Y-%m-%d')

    # Construisez l'URL avec les dates mises à jour.
    base_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m,precipitation,rain&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&timezone=Europe%2FBerlin"
    meteo_url = f"{base_url}&start_date={date_debut_str}&end_date={date_fin_str}"

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
        weather_code = data.get("weather_code", [])
        print("weather_code",weather_code)
        
    else:
        print("Échec de la requête météo. Code d'état :", response.status_code) 
        # Supposons que 'data' contienne les données météo avec la condition météorologique
        condition_meteo = data.get("weather_condition", "Inconnu")

        # Associez la condition météorologique à l'image correspondante
        image_path = get_image_for_weather_condition(condition_meteo)

        if image_path:
            print(f'Chemin de l\'image météo : {image_path}')
            # Affichez l'image ici avec Pillow
            image = Image.open(image_path)
            image.show()
        else:
            print('Image météo non trouvée pour la condition météorologique.')


def get_image_for_weather_condition(condition):
    # Associez les conditions météorologiques aux chemins d'images correspondants
    conditions_images = {
        "Ensoleillé": "projet_perso/image_meteo/sun.svg",
        "Nuageux": "projet_perso/image_meteo/couvert.svg",
        "Pluvieux": "projet_perso/image_meteo/rain.svg",
        "Orage": "thunderstorm.png",
        "Vent": "projet_perso/image_meteo/wind.svg",
        "Inconnu": "unknown.png"  # Image pour les conditions inconnues
    }

    # Récupérez le chemin de l'image en fonction de la condition météorologique
    return conditions_images.get(condition, None)

get_weather_data()
get_image_for_weather_condition(condition='Nuageux')