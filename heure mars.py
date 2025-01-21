# Importer les modules nécessaires
import datetime
import requests

# Définir l'URL de l'API qui fournit l'heure de mars
URL = "https://api.le-systeme-solaire.net/rest/bodies/mars"

# Faire une requête GET à l'API et récupérer le résultat au format JSON
response = requests.get(URL)
data = response.json()

# Extraire le paramètre siderealTime qui correspond à l'heure sidérale de mars en degrés
sidereal_time = data["siderealTime"]

# Convertir l'heure sidérale de mars en heures, minutes et secondes
hours = int(sidereal_time // 15)
minutes = int((sidereal_time % 15) * 4)
seconds = int(((sidereal_time % 15) * 4 - minutes) * 60)

# Créer un objet datetime avec l'heure de mars
mars_time = datetime.time(hours, minutes, seconds)

# Afficher l'heure de mars
print(f"L'heure de mars est : {mars_time}")
