#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt
import networkx as nx
import os
from app import create_app
from app.extensions import db, socketio
from app.seeds.seed_schedules import seed_schedules
from collections import defaultdict

# app = create_app()

def main(filename):

    graph = defaultdict(list)
    duration = {}


if __name__ == "__main__":
    # socketio.run(app)
    main('tasks.csv')
    #with app.app_context():
    #    seed_schedules()
      
