# Calcul de la consommation d'énergie dans un bâtiment

# Données d'entrée
surface_habitable = float(input("Entrez la surface habitable du bâtiment en m² : "))
isolation = input("L'isolation du bâtiment est-elle bonne, moyenne ou mauvaise ? ")
chauffage = input("Le chauffage du bâtiment est-il au gaz, à l'électricité ou au fioul ? ")
climatisation = input("La climatisation du bâtiment est-elle présente ? (oui ou non) ")
eclairage = input("Le bâtiment est-il équipé d'un éclairage LED ? (oui ou non) ")

# Facteurs de conversion
facteur_isolation = 1.0
if isolation == "bonne":
    facteur_isolation = 0.8
elif isolation == "mauvaise":
    facteur_isolation = 1.2

facteur_chauffage = 1.0
if chauffage == "gaz":
    facteur_chauffage = 0.8
elif chauffage == "fioul":
    facteur_chauffage = 1.2

facteur_climatisation = 1.0
if climatisation == "oui":
    facteur_climatisation = 1.2

facteur_eclairage = 1.0
if eclairage == "oui":
    facteur_eclairage = 0.8

# Calcul de la consommation d'énergie
consommation_par_m2 = 100.0 # kWh/m²/an (valeur moyenne)
consommation_totale = surface_habitable * consommation_par_m2 * facteur_isolation * facteur_chauffage * facteur_climatisation * facteur_eclairage

# Affichage des résultats
print("La consommation d'énergie totale du bâtiment est de", consommation_totale, "kWh/an.")
