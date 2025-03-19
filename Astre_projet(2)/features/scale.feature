Feature: Échelle des diamètres et des distances des astres
  En tant qu'utilisateur,
  Je souhaite connaître le diamètre des astres et leurs distances à l'échelle d'une tête humaine,
  Afin de mieux comprendre et visualiser ces valeurs astronomiques.

Scenario: Vérifier la mise à l'échelle des diamètres de la Terre, Mars et Lune
  Given un astre nommé "Soleil" avec un diamètre de 1392700 km
  And une planète nommée "Terre" avec un diamètre de 12756 km
  And une planète nommée "Mars" avec un diamètre de 6779 km
  And une planète nommée "Lune" avec un diamètre de 3474 km
  When je mets les planètes à l'échelle d'une tête humaine
  Then le diamètre de "Terre" devrait être environ 2020 mm avec une marge de 100 mm
  And le diamètre de "Mars" devrait être environ 1070 mm avec une marge de 100 mm
  And le diamètre de "Lune" devrait être environ 550 mm avec une marge de 10 mm