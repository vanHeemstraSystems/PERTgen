#!/usr/bin/env python
from flask import Flask
from config import Config
from app.extensions import db, bcrypt, login_manager, socketio

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Set bycrypt
    bcrypt.init_app(app)

    # Set login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Set socket io
    socketio.init_app(app)
    socketio.cors_allowed_origins = "*"    

    # Register blueprints here
    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    from app.routes.login_routes import login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    from app.routes.registration_routes import registration_bp
    app.register_blueprint(registration_bp, url_prefix='/registration')     

    from app.routes.schedule_routes import schedule_bp
    app.register_blueprint(schedule_bp, url_prefix='/schedules')

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')      
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

