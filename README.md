# Projet Personnel

## Formulation du problème

L'objectif de ce projet était de créer un site web à l'aide de Quarto et de GitHub Pages. Ce site web devait contenir les prévisions météo de la ville de Montpellier pour 5 jours avec notamment la température minimale et maximale de la journée, la vitesse de vent maximale de la journée, ainsi que la quantité de précipitation.

## Site Web

Mon site est disponible à l'adresse suivante: (https://aichalhj.github.io/projet_perso/)

## Méthodologie

Avec Quarto, il est possible de créer un site en y intégrant du code. J'ai tout d'abord récupérer les données grâce à'une API récupérer sur le site open-meteo.com. 
Les données disponibles sur le site permettent, de connaitre la météo pour une intervalle de 4 jours, or l'objectif était d'avoir les données pour 5 jours. La première étape était de modifier l'url de l'API à l'aide du module datetime, afin d'obtenir les données pour 5 jours.
L'extraction des données de l'API a été effectué avec le package Requests, et je les ai regroupé dans un tableau notamment grâce pandas.

Concernant l'estétique du site et l'insertion d'image à l'aide de chaine de caractère HTML, ainsi que le fichier CSS, qui gère le style et les couleurs du site.