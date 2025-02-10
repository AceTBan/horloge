import datetime
import requests
import time

def obtenir_heure_mars():
    # Définir l'URL de l'API qui fournit les données de Mars
    URL = "https://api.le-systeme-solaire.net/rest/bodies/mars"

    # Faire une requête GET à l'API et récupérer le résultat au format JSON
    response = requests.get(URL)
    data = response.json()

    # Extraire le paramètre sideralRotation qui correspond à l'heure sidérale de Mars en heures
    sideral_rotation = data["sideralRotation"]

    # Calculer l'heure martienne 
    mars_hours_per_day = 24.6229  # Durée d'un jour martien en heures terrestres

    # Obtenir l'heure actuelle sur Terre
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()

    # Conversion du temps actuel terrestre en temps martien
    mars_time_in_earth_seconds = (current_time % (mars_hours_per_day * 3600))
    mars_hours = int((mars_time_in_earth_seconds // 3600) % 24)
    mars_minutes = int((mars_time_in_earth_seconds % 3600) // 60)
    mars_seconds = int(mars_time_in_earth_seconds % 60)

    # Créer un objet datetime avec l'heure de mars
    mars_time = datetime.time(mars_hours, mars_minutes, mars_seconds)

    return current_earth_time, mars_time

while True:
    current_earth_time, mars_time = obtenir_heure_mars()

    print(f"L'heure actuelle sur Terre est : {current_earth_time}")
    print(f"L'heure actuelle sur Mars est : {mars_time}")

    choix = input("Appuyez sur 'r' pour rafraîchir, 'q' pour quitter : ")
    if choix.lower() == 'q':
        break
