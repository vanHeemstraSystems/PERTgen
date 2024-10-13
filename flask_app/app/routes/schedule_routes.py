#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.schedule import Schedule
from app.extensions import db

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedules')
def list_schedules():
   schedules = Schedule.query.all()
   return render_template('schedules.html', schedules=schedules)
