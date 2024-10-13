# PERTgen

> Code Python pour générer un graphique PERT et un diagramme de Gantt en fonction d'un calendrier de tâches.

Basé sur « Comment structurer une grande application Flask avec des plans Flask et Flask-SQLAlchemy » sur<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Basé sur "Flask SQLAlchemy" sur<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Basé sur le « modèle d'usine » à<https://github.com/vanHeemstraSystems/factory-pattern>

Basé sur les « Diagrammes de relations d'entités basés sur du texte avec Mermaid.js » sur<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

Basé sur "FlowBite" à<https://github.com/themesberg/flowbite>

Ouvrez cette URL avec`https://github.dev/`au lieu de`https://github.dev/`pour utiliser l'EDI Web Visual Studio Code.

Exécutez cette application comme suit :

1) Entrez`flask_app`annuaire:`$ cd flask_app`2) S'il n'existe pas, créez un environnement virtuel à l'intérieur du`flask_app`annuaire:`$ python3 -m venv .venv`(macOS :`$ virtualenv .venv`)

Dans les cas suivants, suivez ses conseils :

L'environnement virtuel n'a pas été créé correctement car Ensurepip n'est pas
disponible.

Sur les systèmes Debian/Ubuntu, vous devez installer le python3-venv
package à l’aide de la commande suivante.

    sudo apt-get update
    sudo apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Sur macOS, voir<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Démarrez l'environnement virtuel et entrez :`. .venv/bin/activate`(macOS :`source .venv/bin/activate`)
4) Courir`$ pip install -r requirements.txt`5) Exécutez :`$ npm install`6) Définissez l'application Flask dans le répertoire des applications :`(.venv) $ export FLASK_APP=app`7) Définissez l'environnement Flask sur True pour le développement :`(.venv) $ export FLASK_DEBUG=True`8) Définissez l'URI de la base de données SQLAlchemy :`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, la valeur par défaut est`sqlite:///app.db`9) Définir les modifications de la piste SQLAlchemy :`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Définir la clé secrète :`(.venv) $ export SECRET_KEY=********`11) Exécutez l'application Flask :`(.venv) $ flask run`12) Ouvrez l'interface Web comme vous y êtes invité
13) Utiliser`CTRL+c`pour quitter le serveur Web.
14) Vous pouvez également exécuter l'interface de ligne de commande flask :`(.venv) $ flask shell`15) Exécutez toutes les commandes du flacon : >>>
16) Utiliser`exit()`pour quitter l'interface de ligne de commande.

## Exigences

Ce projet utilise python3 et les bibliothèques suivantes doivent être installées pour l'exécuter :

-   [RéseauX](https://networkx.github.io/)- Utilisé pour réaliser le graphique PERT.
-   [Matplotlib](https://matplotlib.org/)- Utilisé pour créer le diagramme de Gantt, ainsi que pour afficher et enregistrer le graphique PERT et le diagramme de Gantt.

## Saisie de données

Les données de la tâche doivent être renseignées dans un fichier CSV, au format de ceux donnés en exemple (`tasks.csv`et`tasks2.csv`),
c'est-à-dire que chaque ligne à partir de la seconde doit avoir une tâche, sa durée et toutes ses dépendances séparées par des espaces

## Testez-le

Le projet peut être testé avec la simple interface graphique tkinter en exécutant`gui.py`avec l'interpréteur python3, bien que tout le code important soit dans`pert.py`qui peut également être exécuté après avoir spécifié quel fichier doit être chargé.
