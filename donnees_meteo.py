import requests

def get_weather_data():
    # URL de requête météo
    meteo_url = "https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current_weather=true&timezone=Europe%2FBerlin&start_date=2023-10-21&end_date=2023-10-25"

    response = requests.get(meteo_url)

    if response.status_code == 200:
        data = response.json()
        # Traitement des données ici
        print("Données météo mises à jour avec succès.")
    else:
        print("Échec de la requête météo. Code d'état :", response.status_code)

if __name__ == "__main__":
    while True:
        get_weather_data()

        


