# Reporting sur les accidents de la route au Royaume-Uni — SAÉ 1.01

Projet de groupe réalisé au semestre 1 du BUT Science des données (IUT Clermont Auvergne, site d'Aurillac), avec Mame Diarra Ndiaye, Madeleine Alexandrie Matemb et Kenny Alex Iraganje.

## Le contexte

La base *UKSafetyRoads* recense les accidents de la route survenus au Royaume-Uni en 2020. Elle contient 4 tables (`accident`, `vehicle`, `casualty` et `codebook`) reliées par l'identifiant `accident_index`. L'objectif était de transformer ces données brutes en indicateurs clairs, présentés dans un tableau de bord.

## Ce que j'ai fait

- Connexion à la base SQLite et exploration de sa structure
- Écriture des **requêtes SQL** avec des **jointures** sur la table `codebook` pour remplacer les codes par des libellés lisibles (gravité, type de route, météo, zone urbaine ou rurale, type de véhicule…)
- **Automatisation de l'extraction en Python** (pandas) et export des résultats dans un fichier Excel à trois onglets
- Réalisation des visualisations dans LibreOffice Calc : diagrammes, tableaux croisés et indicateurs

## Contenu du dépôt

| Dossier | Contenu |
|---|---|
| `code/requetes.py` | Script Python : requêtes SQL et export Excel |
| `tableau_de_bord/` | Fichier Excel avec les données extraites |
| `rapport/` | Rapport du projet (PDF lisible directement sur GitHub, et version LibreOffice) |

## Outils

SQL · SQLite · Python (pandas, sqlite3) · LibreOffice Calc

## Pour lancer le script

Le fichier `UKSafetyRoads.sqlite` n'est pas inclus. Il faut le placer sur son ordinateur, modifier le chemin dans `sqlite3.connect(...)` au début du script, puis lancer `python code/requetes.py`.
