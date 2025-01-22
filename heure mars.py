import datetime
import requests

try:
    # Définir l'URL de l'API qui fournit l'heure de mars
    URL = "https://api.le-systeme-solaire.net/rest/bodies/mars"

    # Faire une requête GET à l'API et récupérer le résultat au format JSON
    response = requests.get(URL)
    data = response.json()

    # Extraire le paramètre sideralRotation qui correspond à l'heure sidérale de mars en heures
    sideral_rotation = data["sideralRotation"]

    # Convertir l'heure sidérale de mars en heures, minutes et secondes
    total_seconds = sideral_rotation * 3600
    hours = int((total_seconds // 3600) % 24)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    # Créer un objet datetime avec l'heure de mars
    mars_time = datetime.time(hours, minutes, seconds)

    # Afficher l'heure de mars (pour comparer l'heure https://www.marsclock.com/)
    print(f"L'heure de mars est : {mars_time}")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")

# Pause pour garder la fenêtre ouverte lors du double clique sur le fichier .py
input("Appuyez sur Entrée pour fermer...")
