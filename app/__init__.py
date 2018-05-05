import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    if os.getenv("FLASK_CONFIG") == 'production':
        app = Flask(__name__)
        app.config.from_object(app_config[config_name])
       
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from app import models
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
