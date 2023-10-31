import requests
import json
from PIL import Image
import pandas as pd
from datetime import datetime
import datetime
#from IPython.display import Markdown
import numpy as np
from flask import Flask, render_template


#Obtenez la date actuelle.
date_actuelle = datetime.date.today()

# Calculez la date de fin (5 jours à partir de la date actuelle).
date_fin = date_actuelle + datetime.timedelta(days=5)

# Formattez les dates au format AAAA-MM-JJ.
date_debut_str = date_actuelle.strftime('%Y-%m-%d')
date_fin_str = date_fin.strftime('%Y-%m-%d')

# Construisez l'URL avec les dates mises à jour.
base_url = 'https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,relativehumidity_2m,precipitation,rain,snowfall,weathercode,windspeed_10m&daily=sunrise,sunset&timezone=Europe%2FBerlin&start_date=2023-10-30&end_date=2023-11-03'
meteo_url = f'{base_url}&start_date={date_debut_str}&end_date={date_fin_str}'

response = requests.get(meteo_url)

if response.status_code == 200:
    data = response.json()
    # Traitement des données ici
    print('Données météo mises à jour avec succès.',data)
    #Création Dataframe
    df_data=pd.DataFrame(data)
    pd.set_option('display.max_rows',None)
    #Création d'un CSV associé
    df_data.to_csv('df_data.csv',index=False)
    #Extraction des données
    temp = data[0]['hourly']['temperature_2m']
    windspeed = data[0]['hourly']['windspeed_10m']
    sunset = data[0]['daily']['sunset']
    rain = data[0]['hourly']['precipitation']
    sunrise = data[0]['daily']['sunrise']
    humidity = data[0]['hourly']['relativehumidity_2m']
    snow=data[0]['hourly']['snowfall']

    
print("la taille est de ",len(temp))
tabtemp= np.zeros((5,24))
k=0
for i in range (5):
    for j in range(24):
        tabtemp[i,j]=temp[k]
        k+=1
tempmin=np.zeros(5)
tempmax=np.zeros(5)
for i in range (5):
    tempmin[i]=min(tabtemp[i])
    tempmax[i]=max(tabtemp[i])
print('les températures maxiamals sont,',tempmax)
print('les températures minimals sont,',tempmin)

min_length = min(len(tempmax), len(tempmin), len(windspeed), len(sunrise), len(sunset))
tempmax = tempmax[:min_length]
tempmin = tempmin[:min_length]
windspeed = windspeed[:min_length]
sunset = sunset[:min_length]
rain=rain[:min_length]
sunrise=sunrise[:min_length]

df = pd.DataFrame ({
"Date": [date_debut_str]*min_length,
'Température Maximale (°C)': tempmax,
'Température Minimale (°C)': tempmin,
'Lever du Soleil': sunrise,
'Vitesse du Vent Maximale (km/h)': windspeed,
'Coucher du Soleil': sunset,
'Précipitation (mm)': rain })
print(df)


#Déterminer le jour de la semaine
def inttoday(i):
    if ((datetime.datetime.now().weekday()+ i)%7 ==0):
        return 'Lundi'
    elif ((datetime.datetime.now().weekday()+ i)%7 ==1):
        return 'Mardi'
    elif ((datetime.datetime.now().weekday()+ i)%7 ==2):
        return 'Mercredi'
    elif ((datetime.datetime.now().weekday()+ i)%7 ==3):
        return 'Jeudi'
    elif ((datetime.datetime.now().weekday()+ i)%7 ==4):
        return 'Vendredi'
    elif ((datetime.datetime.now().weekday()+ i)%7 ==5):
        return 'Samedi'
    else:
        return 'Dimanche'
inttoday(i)

code_meteo = data[0]['hourly']['weathercode']
print(code_meteo)

#Code Météo

condition_image = {
    0: {'condition': 'Ciel dégagé', 'image': 'sun.svg'},
    1: {'condition': 'Ciel dégagé', 'image': 'sun.svg'},
    2: {'condition': 'Ciel partiellement nuageux', 'image': 'Nuageux.svg'},
    3: {'condition': 'Ciel couvert', 'image': 'couvert.svg'},
    45: {'condition': 'Brouillard', 'image': 'brouillard.svg'},
    48: {'condition': 'Brouillard givré', 'image': 'brouillard.svg'},
    51: {'condition': 'Bruine : Intensité légère', 'image': 'bruine.svg'},
    53: {'condition': 'Bruine : Intensité modérée', 'image': 'bruine.svg'},
    55: {'condition': 'Bruine : Intensité dense', 'image': 'bruine.svg'},
    56: {'condition': 'Bruine verglaçante : Intensité légère', 'image': 'bruine_verglaçante.svg'},
    57: {'condition': 'Bruine verglaçante : Intensité dense', 'image': 'bruine_verglaçante.svg'},
    61: {'condition': 'Pluie légère', 'image': 'pluie_legere.svg'},
    63: {'condition': 'Pluie modérée', 'image': 'pluie_moderee.svg'},
    65: {'condition': 'Pluie forte', 'image': 'pluie_forte.svg'},
    66: {'condition': 'Pluie verglaçante', 'image': 'pluie_forte.svg'},
    71: {'condition': 'Neige', 'image': 'neige.svg'},
    73: {'condition': 'Neige', 'image': 'neige.svg'},
    75: {'condition': 'Neige', 'image': 'neige.svg'},
    80: {'condition': 'Averse légère', 'image': 'averse_legere.svg'},
    81: {'condition': 'Averse moyenne', 'image': 'averse_moyen.svg'},
    82: {'condition': 'Averse forte', 'image': 'averse_forte.svg'},
    95: {'condition': 'Orage', 'image': 'orage.svg'},
    96: {'condition': 'Orage et grêle', 'image': 'grele.svg'},
    99: {'condition': 'Orage et grêle', 'image': 'grele.svg'}
}

def get_weather_image(code_meteo):
    if code_meteo==0 or code_meteo==1:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/soleil(2).svg"
    elif code_meteo==2 or code_meteo==3:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/couvert.svg"
    elif code_meteo==45 or code_meteo==48: 
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/brouillard.svg"
    elif code_meteo==51 or code_meteo==53 or code_meteo==55 or code_meteo==56  or code_meteo==57: 
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/bruine.svg"
    elif code_meteo==61 or code_meteo==63: 
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/pluie(2).svg"
    elif code_meteo==65 or code_meteo==66: 
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/pluie_forte.svg"
    elif code_meteo==71 or code_meteo==73 or code_meteo==75:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/neige.svg"
    elif code_meteo==80 or code_meteo==81 or code_meteo==82:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/averse.svg"
    elif code_meteo==95:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/orage(2).svg"
    elif code_meteo==96 or code_meteo==99:
        return f"C:/Users/aicha/OneDrive/Bureau/Projet Perso/projet_perso/image_meteo/grele.svg"
    else:
        return "image non trouvée"
get_weather_image(code_meteo)



    

