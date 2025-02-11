import datetime
import requests
import time

def obtenir_heure_mars():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/mars"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    mars_hours_per_day = 24.6229  
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    mars_time_in_earth_seconds = (current_time % (mars_hours_per_day * 3600))
    mars_hours = int((mars_time_in_earth_seconds // 3600) % 24)
    mars_minutes = int((mars_time_in_earth_seconds % 3600) // 60)
    mars_seconds = int(mars_time_in_earth_seconds % 60)
    mars_time = datetime.time(mars_hours, mars_minutes, mars_seconds)
    return current_earth_time, mars_time

def obtenir_heure_mercure():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/mercury"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    mercury_hours_per_day = 1407.5  # Durée d'un jour mercurien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    mercury_time_in_earth_seconds = (current_time % (mercury_hours_per_day * 3600))
    mercury_hours = int((mercury_time_in_earth_seconds // 3600) % 24)
    mercury_minutes = int((mercury_time_in_earth_seconds % 3600) // 60)
    mercury_seconds = int(mercury_time_in_earth_seconds % 60)
    mercury_time = datetime.time(mercury_hours, mercury_minutes, mercury_seconds)
    return mercury_time

while True:
    current_earth_time, mars_time = obtenir_heure_mars()
    mercury_time = obtenir_heure_mercure()

    print(f"L'heure actuelle sur Terre est : {current_earth_time}")
    print(f"L'heure actuelle sur Mars est : {mars_time}")
    print(f"L'heure actuelle sur Mercure est : {mercury_time}")

    choix = input("Appuyez sur 'r' pour rafraîchir, 'q' pour quitter : ")
    if choix.lower() == 'q':
        break
