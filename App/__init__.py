from flask import Flask
from App.database import db

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    return app
