#!/usr/bin/env python
import os
from app import create_app
from app.extensions import db, socketio
from app.seeds.seed_schedules import seed_schedules

app = create_app()

if __name__ == "__main__":
    socketio.run(app)
    with app.app_context():
        seed_schedules()
      
