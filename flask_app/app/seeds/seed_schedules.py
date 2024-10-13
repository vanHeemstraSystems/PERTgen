#!/usr/bin/env python
from app.extensions import db
from app.models.schedule import Schedule

def seed_schedules():
    # Clear existing data (optional)
    db.session.query(Schedule).delete()
    db.session.commit()

    # Create a new schedule
    new_schedule = Schedule(title="My Schedule", content="Scheduled tasks go here")
    db.session.add(new_schedule)
    db.session.commit()

    print("Schedules seeded!")

