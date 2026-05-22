from ext.database import db
from domain.base import BaseModel
from sqlalchemy.exc import SQLAlchemyError


class BaseRepo:

    def __init__(self, model:BaseModel):
        self.model = model

    def add(self, model:BaseModel)-> BaseModel:
        """Add a model object to the database"""
        try:
            db.session.add(model)
            db.session.flush([model])
            db.session.refresh(model)
            return model
        except SQLAlchemyError as error:
            db.session.rollback()
            raise error
        