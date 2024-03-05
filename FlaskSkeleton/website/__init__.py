from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the database
db = SQLAlchemy()
DB_NAME = "mikeshop.db"

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rootadmin1234'
    
    # Set the database URI
    basedir = path.abspath(path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, DB_NAME)
    db.init_app(app)
    
    # Include MVT components and auth
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Create database and intialize models
    from .models import User
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database Successfully Initialized!')
    
    
