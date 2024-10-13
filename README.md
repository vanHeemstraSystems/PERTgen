# PERTgen

> Python code to generate a PERT graph and Gantt chart given a task schedule.

Based on "How To Structure a Large Flask Application with Flask Blueprints and Flask-SQLAlchemy" at https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

Based on "Flask SQLAlchemy" at https://github.com/vanHeemstraSystems/flask-sqlalchemy/

Based on "Factory Pattern" at https://github.com/vanHeemstraSystems/factory-pattern

Based on "Text-Based Entity Relationship Diagrams with Mermaid.js" at https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/

Based on "FlowBite" at https://github.com/themesberg/flowbite

Open this URL with ```https://github.dev/``` instead of ```https://github.dev/``` to use the Visual Studio Code web-based IDE.

Run this application as follows:

1) Enter ```flask_app``` directory: ```$ cd flask_app```
2) If non-existent, create a virtual environment inside the ```flask_app``` directory: ```$ python3 -m venv .venv``` (macOS: ```$ virtualenv .venv```)

In case of the following, follow its advice:

The virtual environment was not created successfully because ensurepip is not
available.  

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt-get update
    sudo apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

On macOS see https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

3) Start the virtual environment and enter: ```. .venv/bin/activate``` (macOS: ```source .venv/bin/activate```)
4) Run ```$ pip install -r requirements.txt```
5) Run: ```$ npm install```
6) Set the Flask App to app directory: ```(.venv) $ export FLASK_APP=app```
7) Set the Flask Environment to True for development: ```(.venv) $ export FLASK_DEBUG=True```
8) Set the SQLAlchemy Database URI: ```(.venv) $ export SQLALCHEMY_DATABASE_URI=...```, default is ```sqlite:///app.db```
9) Set SQLAlchemy Track Modifications: ```(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True```
10) Set Secret Key: ```(.venv) $ export SECRET_KEY=********```
11) Run the flask app: ```(.venv) $ flask run```
12) Open the web interface as prompted
13) Use ```CTRL+c``` to exit the web server.
14) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
15) Execute any flask commands: >>>
16) Use ```exit()``` to exit from the command line interface.

## Requirements
This project uses python3, and the following libraries must be installed to run it:
* [NetworkX](https://networkx.github.io/) - Used to make the PERT graph.
* [Matplotlib](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## Data input
The task data must be given in a CSV file, in the format of the sample ones given (```tasks.csv``` and ```tasks2.csv```),
i.e. each row starting from the second one should have a task, its duration and all its dependencies seperated by spaces

## Test it
The project can be tested with the simple tkinter GUI by running ```gui.py``` with the python3 interpreter, although all the important code is in ```pert.py``` which can also be run after specifying which file is to be loaded.
