# PERTgen

Code Python pour générer un graphique PERT et un diagramme de Gantt en fonction d'un calendrier de tâches.

## Exigences

Ce projet utilise python3 et les bibliothèques suivantes doivent être installées pour l'exécuter :

-   [RéseauX](https://networkx.github.io/) - Used to make the PERT graph.
-   [Matplotlib](https://matplotlib.org/)- Utilisé pour créer le diagramme de Gantt, ainsi que pour afficher et enregistrer le graphique PERT et le diagramme de Gantt.

## Saisie de données

Les données de la tâche doivent être renseignées dans un fichier CSV, au format de ceux donnés en exemple (`tasks.csv`et`tasks2.csv`),
i.e. each row starting from the second one should have a task, its duration and all its dependencies seperated by spaces

## Testez-le

Le projet peut être testé avec la simple interface graphique tkinter en exécutant`gui.py`avec l'interpréteur python3, bien que tout le code important soit dans`pert.py`qui peut également être exécuté après avoir spécifié quel fichier doit être chargé.
