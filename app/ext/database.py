from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    import_module("models.models")