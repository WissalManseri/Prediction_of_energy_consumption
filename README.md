# Calcul de la consommation d'énergie dans un bâtiment

Ce programme permet de calculer la consommation d'énergie totale d'un bâtiment en fonction de différents paramètres tels que la surface habitable, l'isolation, le chauffage, la climatisation et l'éclairage.

# Comment utiliser le programme

1. Ouvrir un terminal ou une console Python.

2. Exécuter le programme en tapant python calcul_consommation_energie.py.

3. Entrer les données d'entrée suivantes :

      Surface habitable du bâtiment en m².

      Qualité de l'isolation du bâtiment (bonne, moyenne ou mauvaise).

      Type de chauffage du bâtiment (gaz, électricité ou fioul).

      Présence de climatisation dans le bâtiment (oui ou non).

      Présence d'un éclairage LED dans le bâtiment (oui ou non).

      Le programme affiche la consommation d'énergie totale du bâtiment en kWh/an.

      Paramètres pris en compte
  
4. Le programme utilise les paramètres suivants pour calculer la consommation d'énergie :


     **Surface habitable :** surface habitable du bâtiment en m².

     **Isolation :** qualité de l'isolation du bâtiment (bonne, moyenne ou mauvaise). Un facteur de conversion est appliqué en fonction de la qualité de l'isolation        pour prendre en compte son impact sur la consommation d'énergie.


      **Chauffage :** type de chauffage du bâtiment (gaz, électricité ou fioul). Un facteur de conversion est appliqué en fonction du type de chauffage pour prendre en       compte son impact sur la consommation d'énergie.


      **Climatisation :** présence de climatisation dans le bâtiment (oui ou non). Un facteur de conversion est appliqué en fonction de la présence de climatisation          pour prendre en compte son impact sur la consommation d'énergie.


     **Eclairage :** présence d'un éclairage LED dans le bâtiment (oui ou non). Un facteur de conversion est appliqué en fonction de la présence d'un éclairage LED           pour prendre en compte son impact sur la consommation d'énergie.

# Exemple d'utilisation

              Entrez la surface habitable du bâtiment en m² : 100
              L'isolation du bâtiment est-elle bonne, moyenne ou mauvaise ? bonne
              Le chauffage du bâtiment est-il au gaz, à l'électricité ou au fioul ? gaz
              La climatisation du bâtiment est-elle présente ? (oui ou non) non  
              Le bâtiment est-il équipé d'un éclairage LED ? (oui ou non) oui
              La consommation d'énergie totale du bâtiment est de 8000.0 kWh/an.
  
Dans cet exemple, on a entré une surface habitable de 100 m², une bonne isolation, un chauffage au gaz, pas de climatisation et un éclairage LED. 
Le programme a affiché une consommation d'énergie totale de 8000 kWh/an.
