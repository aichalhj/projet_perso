import requests
import time

# L'URL de la requête pour Montpellier 
meteo_url = "https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current_weather=true&timezone=Europe%2FBerlin&start_date=2023-10-21&end_date=2023-10-25" 

# Dossier où vous stockerez les images des prévisions
dossier_images = "Image meteo"

'''def obtenir_previsions_meteo():
    try:
        response = requests.get(meteo_url)
        data = response.json()
        # Analysez les données de l'API pour obtenir les informations de prévisions

        # Exemple : Obtenez l'URL de l'image de la prévision pour chaque jour
        images_previsions = [data['jour1']['image'], data['jour2']['image'], data['jour3']['image'], data['jour4']['image'], data['jour5']['image']]

        # Mettez à jour les images dans le dossier local
        for i, image_url in enumerate(images_previsions):
            response = requests.get(image_url)
            with open(f"{dossier_images}/jour{i+1}.png", "wb") as image_file:
                image_file.write(response.content)
        
    except Exception as e:
        print(f"Erreur lors de la récupération des prévisions météo : {e}")'''

if __name__ == "__main__":
    while True:
        obtenir_previsions_meteo()
        print("Images de prévisions mises à jour.")
        
        # Intervalles de mise à jour (par exemple, 6 heures)
        time.sleep(6 * 60 * 60)

 




