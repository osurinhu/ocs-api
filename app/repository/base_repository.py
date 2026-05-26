from ext.database import db
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.pagination import Pagination

class BaseRepo:
    def __init__(self, model):
        self.model = model

    def listar_paginado(self, exato:dict={}, like:dict={}, page:int=1, per_page:int=20)-> Pagination:
        try:
            stmt = db.select(self.model).filter_by(**exato)
            for key, value in like.items():
                if value != None or value != '':
                    stmt = stmt.where(getattr(self.model, key).like("%"+str(value)+"%"))
            pages = db.paginate(stmt, page=page, per_page=per_page)
            return pages
        except SQLAlchemyError as error:
            raise error