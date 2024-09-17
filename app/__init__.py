from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
socketio = SocketIO()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  migrate.init_app(app, db)
  login.init_app(app)
  socketio.init_app(app)

  from .main import main as main_bp
  app.register_blueprint(main_bp)

  from .auth import auth as auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

  from .api import api as api_bp
  app.register_blueprint(api_bp, url_prefix='/api')

  return app
  