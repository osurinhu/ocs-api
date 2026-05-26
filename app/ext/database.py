from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def init_app(app):
    db.init_app(app)
    import_module("models.models")