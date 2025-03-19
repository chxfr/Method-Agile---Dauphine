Feature: Échelle des diamètres et des distances des astres
  En tant qu'utilisateur, Je souhaite connaître la diamètre des astres et leurs distances à l'échelle d'une tête humaine,
  Afin de mieux comprendre et visualiser ces valeurs astronomiques.

Scenario: Calculer la proportion entre le diamètre du Soleil et la tête humaine
  Given un astre nommé "Soleil" avec un diamètre de 1392700 km
  And une longueur moyenne de tête humaine de 0.22 m
  When je calcule la proportion entre le Soleil et la tête humaine
  Then la proportion devrait être environ 6330000000 avec une marge de 10000000


Scenario: Vérifier la mise à l'échelle du diamètre de la Terre, Mars et la Lune
  Given un astre nommé "Soleil" avec un diamètre de 1392700 km
  And une longueur moyenne de tête humaine de 0.22 m
  And une planète nommée "la Terre" avec diamètre de 12756 km
  And une planète nommée "Mars" avec diamètre de 6779 km
  And une planète nommée "la Lune" avec diamètre de 3474 km
  When je mets à l'échelle les diamètres de ces planètes selon la proportion Soleil-tête
  Then le diamètre mis à l'échelle de la Terre devrait être environ 2.02 mm à 0.1 mm près
  And le diamètre mis à l'échelle de Mars devrait être environ 1.07 mm à 0.1 mm près
  And le diamètre mis à l'échelle de la Lune devrait être environ 0.55 mm à 0.1 mm près
  