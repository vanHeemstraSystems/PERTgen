# PERTgen

Python code to generate a PERT graph and Gantt chart given a task schedule.

## Exigences

Ce projet utilise python3 et les bibliothèques suivantes doivent être installées pour l'exécuter :

-   [RéseauX](https://networkx.github.io/)- Utilisé pour réaliser le graphique PERT.
-   [Matplotlib](https://matplotlib.org/)- Utilisé pour créer le diagramme de Gantt, ainsi que pour afficher et enregistrer le graphique PERT et le diagramme de Gantt.

## Saisie de données

Les données de la tâche doivent être renseignées dans un fichier CSV, au format de ceux donnés en exemple (`tasks.csv`et`tasks2.csv`),
c'est-à-dire que chaque ligne à partir de la seconde doit avoir une tâche, sa durée et toutes ses dépendances séparées par des espaces

## Testez-le

Le projet peut être testé avec la simple interface graphique tkinter en exécutant`gui.py`avec l'interpréteur python3, bien que tout le code important soit dans`pert.py`qui peut également être exécuté après avoir spécifié quel fichier doit être chargé.
