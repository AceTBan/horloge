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

def obtenir_heure_venus():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/venus"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    venus_hours_per_day = 2802.0  # Durée d'un jour vénusien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    venus_time_in_earth_seconds = (current_time % (venus_hours_per_day * 3600))
    venus_hours = int((venus_time_in_earth_seconds // 3600) % 24)
    venus_minutes = int((venus_time_in_earth_seconds % 3600) // 60)
    venus_seconds = int(venus_time_in_earth_seconds % 60)
    venus_time = datetime.time(venus_hours, venus_minutes, venus_seconds)
    return venus_time

def obtenir_heure_jupiter():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/jupiter"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    jupiter_hours_per_day = 9.925  # Durée d'un jour jupitérien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    jupiter_time_in_earth_seconds = (current_time % (jupiter_hours_per_day * 3600))
    jupiter_hours = int((jupiter_time_in_earth_seconds // 3600) % 24)
    jupiter_minutes = int((jupiter_time_in_earth_seconds % 3600) // 60)
    jupiter_seconds = int(jupiter_time_in_earth_seconds % 60)
    jupiter_time = datetime.time(jupiter_hours, jupiter_minutes, jupiter_seconds)
    return jupiter_time

def obtenir_heure_saturne():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/saturn"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    saturn_hours_per_day = 10.656  # Durée d'un jour saturnien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    saturn_time_in_earth_seconds = (current_time % (saturn_hours_per_day * 3600))
    saturn_hours = int((saturn_time_in_earth_seconds // 3600) % 24)
    saturn_minutes = int((saturn_time_in_earth_seconds % 3600) // 60)
    saturn_seconds = int(saturn_time_in_earth_seconds % 60)
    saturn_time = datetime.time(saturn_hours, saturn_minutes, saturn_seconds)
    return saturn_time

def obtenir_heure_uranus():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/uranus"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    uranus_hours_per_day = 17.24  # Durée d'un jour uranien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    uranus_time_in_earth_seconds = (current_time % (uranus_hours_per_day * 3600))
    uranus_hours = int((uranus_time_in_earth_seconds // 3600) % 24)
    uranus_minutes = int((uranus_time_in_earth_seconds % 3600) // 60)
    uranus_seconds = int(uranus_time_in_earth_seconds % 60)
    uranus_time = datetime.time(uranus_hours, uranus_minutes, uranus_seconds)
    return uranus_time

def obtenir_heure_neptune():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/neptune"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    neptune_hours_per_day = 16.11  # Durée d'un jour neptunien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    neptune_time_in_earth_seconds = (current_time % (neptune_hours_per_day * 3600))
    neptune_hours = int((neptune_time_in_earth_seconds // 3600) % 24)
    neptune_minutes = int((neptune_time_in_earth_seconds % 3600) // 60)
    neptune_seconds = int(neptune_time_in_earth_seconds % 60)
    neptune_time = datetime.time(neptune_hours, neptune_minutes, neptune_seconds)
    return neptune_time

def obtenir_heure_pluton():
    URL = "https://api.le-systeme-solaire.net/rest/bodies/pluto"
    response = requests.get(URL)
    data = response.json()
    sideral_rotation = data["sideralRotation"]
    pluto_hours_per_day = 153.2928  # Durée d'un jour plutonien en heures terrestres
    current_time = time.time()
    current_earth_time = datetime.datetime.now().time()
    pluto_time_in_earth_seconds = (current_time % (pluto_hours_per_day * 3600))
    pluto_hours = int((pluto_time_in_earth_seconds // 3600) % 24)
    pluto_minutes = int((pluto_time_in_earth_seconds % 3600) // 60)
    pluto_seconds = int(pluto_time_in_earth_seconds % 60)
    pluto_time = datetime.time(pluto_hours, pluto_minutes, pluto_seconds)
    return pluto_time

while True:
    current_earth_time, mars_time = obtenir_heure_mars()
    mercury_time = obtenir_heure_mercure()
    venus_time = obtenir_heure_venus()
    jupiter_time = obtenir_heure_jupiter()
    saturn_time = obtenir_heure_saturne()
    uranus_time = obtenir_heure_uranus()
    neptune_time = obtenir_heure_neptune()
    pluto_time = obtenir_heure_pluton()

    print(f"L'heure actuelle sur Terre est : {current_earth_time}")
    print(f"L'heure actuelle sur Mars est : {mars_time}")
    print(f"L'heure actuelle sur Mercure est : {mercury_time}")
    print(f"L'heure actuelle sur Vénus est : {venus_time}")
    print(f"L'heure actuelle sur Jupiter est : {jupiter_time}")
    print(f"L'heure actuelle sur Saturne est : {saturn_time}")
    print(f"L'heure actuelle sur Uranus est : {uranus_time}")
    print(f"L'heure actuelle sur Neptune est : {neptune_time}")
    print(f"L'heure actuelle sur Pluton est : {pluto_time}")

    choix = input("Appuyez sur 'r' pour rafraîchir, 'q' pour quitter : ")
    if choix.lower() == 'q':
        break
