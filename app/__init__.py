from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Configurar la clave secreta
    app.secret_key = 'your_secret_key_here'

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app

